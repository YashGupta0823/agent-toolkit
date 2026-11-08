"""Minimal MCP client smoke test for the AlphaSearch server.

Launches server.py over stdio as a real MCP subprocess, lists its tools, and
calls search_quant_papers (plus two invalid calls to check error handling).

Run from the project root:  .venv/bin/python mcp_server/smoke_test.py
"""

import asyncio
import os
import sys
from pathlib import Path

from mcp import Client, StdioServerParameters

SERVER = Path(__file__).resolve().parent / "server.py"


async def main() -> int:
    # The stdio client only passes a minimal default environment to the server,
    # so forward the AlphaSearch overrides explicitly.
    env = {k: v for k, v in os.environ.items() if k.startswith("ALPHASEARCH_")}
    params = StdioServerParameters(command=sys.executable, args=[str(SERVER)], env=env or None)
    async with Client(params) as client:
        tools = (await client.list_tools()).tools
        print("Tools:", [t.name for t in tools])
        assert [t.name for t in tools] == ["search_quant_papers"], "expected exactly one tool"

        result = await client.call_tool("search_quant_papers", {"query": "volatility risk premium options"})
        if result.is_error:
            print("Tool call FAILED:", result.content[0].text)
            return 1
        data = result.structured_content
        print(f"\nQuery: {data['query']!r} -> {data['count']} results")
        for i, p in enumerate(data["results"], 1):
            print(f"\n{i}. {p['title']}  (similarity {p['similarity']})")
            print(f"   arXiv {p['arxiv_id']} | {p['year']} | {p['url']}")
            print(f"   Authors: {p['authors']}")
            print(f"   Abstract: {p['abstract'][:200]}...")

        print("\nError handling:")
        for args in ({"query": "   "}, {"query": "momentum", "limit": 11}):
            r = await client.call_tool("search_quant_papers", args)
            print(f"  {args} -> is_error={r.is_error}: {r.content[0].text}")
            assert r.is_error
    return 0


if __name__ == "__main__":
    sys.exit(asyncio.run(main()))
