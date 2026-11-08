I built an agent toolkit to make AI-assisted quantitative finance research more accurate and easier to verify. It consists of two components: a checker skill called `research-brief-check` and an MCP server called `alphasearch-mcp`.

The MCP server connects Claude Code to the AlphaSearch research database I built. The checker reviews AI-generated research briefs against their cited abstracts and identifies unsupported or overstated claims without modifying the original work.

## 1. The Checker Skill
**Name:** `research-brief-check`
**Location:** `.claude/skills/research-brief-check/SKILL.md`

This skill reviews research briefs and checks whether their claims are supported by the underlying academic abstracts.

It activates when Claude Code is asked to review a research brief for source accuracy, or it can be manually triggered using `/research-brief-check`.

For each claim, the checker assigns one of four classifications:

- **SUPPORTED:** The source supports the claim.
- **OVERSTATED:** The claim goes beyond what the source establishes.
- **CONTRADICTED:** The source conflicts with the claim.
- **UNVERIFIABLE:** There is not enough evidence to verify the claim.

The checker provides evidence and source references for its findings. It never edits the original research brief.

## 2. The MCP Server
**Name:** `alphasearch-mcp`
**Location:** `mcp_server/server.py`
The MCP server gives Claude Code direct access to my existing AlphaSearch vector database.

The tool performs semantic searches across stored arXiv research abstracts and returns relevant papers with their titles, authors, arXiv IDs, URLs, abstracts, and similarity scores.


Both components came from problems I encountered while building AlphaSearch.
I repeatedly asked the AI to keep its research analysis from real sources.

The checker skill addresses this by reviewing claims independently rather than assuming the original agent's conclusions are correct.

My original AlphaSearch repository is:
https://github.com/YashGupta0823/VectorDatabase