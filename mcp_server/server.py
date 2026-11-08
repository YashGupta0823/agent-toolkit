"""AlphaSearch MCP server (stdio).

Exposes one tool, ``search_quant_papers``, that runs semantic search over the
AlphaSearch ChromaDB research collection by reusing ``ResearchDatabase`` from
the AlphaSearch project. Nothing is generated here: every returned field is
read from the database.

AlphaSearch location: $ALPHASEARCH_REPO if set, otherwise ../VectorDatabase
relative to this project. The Chroma folder is AlphaSearch's own default
(its chroma_db/ folder, or $ALPHASEARCH_DB if set).

stdout carries the MCP protocol, so all diagnostics go to stderr.
"""

from __future__ import annotations

import contextlib
import logging
import os
import sys
from pathlib import Path

from pydantic import BaseModel

from mcp.server.mcpserver import MCPServer
from mcp.server.mcpserver.exceptions import ToolError

logging.basicConfig(stream=sys.stderr, level=logging.INFO, format="[alphasearch-mcp] %(levelname)s %(message)s")
log = logging.getLogger("alphasearch-mcp")

PROJECT_ROOT = Path(__file__).resolve().parent.parent
ALPHASEARCH_REPO = Path(os.environ.get("ALPHASEARCH_REPO") or PROJECT_ROOT.parent / "VectorDatabase").expanduser().resolve()

DEFAULT_LIMIT = 5
MAX_LIMIT = 10

mcp = MCPServer("alphasearch")

_db = None  # ResearchDatabase, opened on first use


class Paper(BaseModel):
    title: str
    authors: str
    abstract: str
    arxiv_id: str
    url: str
    year: str
    similarity: float


class SearchResponse(BaseModel):
    query: str
    count: int
    results: list[Paper]


def _open_database():
    """Import AlphaSearch's ResearchDatabase and open its existing collection."""
    global _db
    if _db is not None:
        return _db

    if not (ALPHASEARCH_REPO / "database.py").is_file():
        raise ToolError(
            f"AlphaSearch project not found at {ALPHASEARCH_REPO} (no database.py). "
            "Set ALPHASEARCH_REPO to the AlphaSearch repository path."
        )

    # Import from the AlphaSearch repo without writing .pyc files into it.
    sys.dont_write_bytecode = True
    if str(ALPHASEARCH_REPO) not in sys.path:
        sys.path.insert(0, str(ALPHASEARCH_REPO))
    try:
        import database  # AlphaSearch's database.py
    except ImportError as exc:
        raise ToolError(f"Could not import AlphaSearch database.py from {ALPHASEARCH_REPO}: {exc}") from exc

    db_path = Path(database.DEFAULT_DB_PATH)
    # ResearchDatabase() creates a missing folder, so check first rather than
    # silently creating an empty database.
    if not (db_path / "chroma.sqlite3").is_file():
        raise ToolError(
            f"AlphaSearch database not found at {db_path}. "
            "Build it in the AlphaSearch repo first (python app.py import)."
        )

    # Keep any library output (e.g. first-run model download) off stdout.
    with contextlib.redirect_stdout(sys.stderr):
        _db = database.ResearchDatabase(db_path)
    log.info("Opened AlphaSearch database at %s (%d documents)", db_path, _db.count())
    return _db


@mcp.tool()
def search_quant_papers(query: str, limit: int = DEFAULT_LIMIT) -> SearchResponse:
    """Semantic search over the AlphaSearch library of quantitative finance research papers (arXiv).

    Use this tool when you need real, citable research on quantitative finance topics such as
    trading strategies, factor models, volatility, options pricing, portfolio construction, risk
    management or market microstructure: for example, to find papers on a topic, to fetch the
    abstract a claim relies on, or to check whether a research claim is supported by the literature.
    Cite results by title and arXiv ID. Do not use it for live market data, prices or news.

    Results are ranked by cosine similarity of meaning, not keyword match, so phrase the query as a
    topic or a question (e.g. "volatility risk premium options"). Every field returned comes from the
    database. If nothing relevant comes back, say so rather than inventing a source.

    Args:
        query: Natural-language description of the research topic to search for.
        limit: Number of papers to return, from 1 to 10 (default 5).

    Returns:
        The query, the number of results, and for each paper its title, authors, abstract,
        arXiv ID, URL, year and similarity score (higher means more relevant, max 1.0).
    """
    if not query or not query.strip():
        raise ToolError("Query is empty. Provide a research topic, e.g. 'volatility risk premium options'.")
    if isinstance(limit, bool) or not isinstance(limit, int) or not 1 <= limit <= MAX_LIMIT:
        raise ToolError(f"Invalid limit {limit!r}: must be an integer from 1 to {MAX_LIMIT}.")

    db = _open_database()

    with contextlib.redirect_stdout(sys.stderr):
        if db.count("arxiv") == 0:
            raise ToolError(
                f"The AlphaSearch research collection at {db.path} contains no papers. "
                "Import papers in the AlphaSearch repo first (python app.py import)."
            )
        hits = db.search(query, k=limit, source_type="arxiv")

    papers = [
        Paper(
            title=h.title,
            authors=h.authors,
            abstract=h.abstract,
            arxiv_id=h.metadata.get("arxiv_id", ""),
            url=h.url,
            year=h.year,
            similarity=round(h.similarity, 4),
        )
        for h in hits
    ]
    log.info("search_quant_papers query=%r limit=%d -> %d results", query, limit, len(papers))
    return SearchResponse(query=query.strip(), count=len(papers), results=papers)


if __name__ == "__main__":
    log.info("Starting AlphaSearch MCP server (stdio); AlphaSearch repo: %s", ALPHASEARCH_REPO)
    mcp.run(transport="stdio")
