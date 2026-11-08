# Demonstration: AlphaSearch Agent Toolkit

For this assignment, I tested my toolkit on two finance research tasks using Claude Code. My MCP server connects Claude to the AlphaSearch vector database I built for HW6. The `research-brief-check` skill independently reviews research briefs and identifies claims that go beyond their cited sources. I used one Claude Code session to retrieve papers and write a research brief. I then started a separate session with fresh context to run the checker. 

## Run 1: Volatility Risk Premium
My first research question was: "Can selling options systematically earn a volatility risk premium, and what risks limit this strategy?"

I asked Claude to use the AlphaSearch MCP tool to retrieve academic research and write a 300–400 word brief in `demonstrations/run1_brief.md`.

### MCP Tool Usage

Claude made six AlphaSearch searches and produced a research brief of approximately 388 words. The main paper was Miao and Sorokina (arXiv:2609.01183)

**Actual MCP transcript excerpt:**
I wrote the brief to demonstrations/run1_brief.md. It's about 388 words, not counting markdown symbols, and every claim comes from an abstract the AlphaSearch tool returned.
I ran six searches, and only one paper actually tests a strategy that earns the premium by selling options:
Direct evidence: Miao & Sorokina (arXiv:2609.01183) wrote cash-secured puts on nuclear and energy stocks from 2000–2024.
Risks: four papers support the risk section only indirectly:
Zhuang (2608.23274)
Landolfi (2608.00127)
Zernikov (2605.21696)
Kumar (2608.29025)

### Independent Checker Results

I started a new Claude Code session and ran `research-brief-check` on the completed brief. The checker performed eight AlphaSearch queries and reviewed 12 numbered claims.

The most significant finding was that the research agent had missed Wysocki's paper (arXiv:2608.24786), which studies volatility risk premium harvesting using S&P 500 index options.

**Checker transcript excerpt:**

Claim 8: Only one retrieved paper tests a VRP-harvesting strategy directly.

Status: CONTRADICTED (at the library level)

The checker explained that another directly relevant paper was present in the database but had not been included in the brief.

### My Evaluation

I agreed with the checker's main findings. The missing Wysocki paper was especially important because it challenged the original brief's assessment of the available evidence. However, Its final numbered claim received two classifications, making the summary counts inconsistent. 

## Run 2: Stochastic Volatility and Option Pricing

### Task
My second research question was: "How do stochastic volatility and jump models compare with Black-Scholes for option pricing?" I asked Claude to create another research brief in `demonstrations/run2_brief.md`.

### MCP Tool Usage

Claude performed three AlphaSearch searches and produced a brief of approximately 400 words. Its main finding came from Mensah et al. (arXiv:2605.30562).

**Actual MCP transcript excerpt:**
I've written the brief to demonstrations/run2_brief.md. It's 404 words by wc -w, which counts headings and markdown symbols, so the text itself falls inside the 300–400 range.
I ran three AlphaSearch queries. Every claim in the brief comes from the returned abstracts and cites an arXiv ID.
Main findings:
Stochastic volatility gives most of the improvement (arXiv:2605.30562).
Jumps add little (arXiv:2605.27945).
Merton jump-diffusion produces the volatility smile (arXiv:2607.06355).
Black-Scholes remains the main term for certain short-maturity barrier options (arXiv:2610.00340).
Standard simulation of stochastic volatility models can be biased (arXiv:2609.21301).

### Independent Checker Results

I opened another fresh Claude Code session and reviewed the second brief using my checker skill. The checker retrieved the five cited abstracts and evaluated 12 claims.

One important issue involved the interpretation of the 39% pricing-error reduction. The checker explained that this went beyond the evidence because a 39% reduction still leaves a substantial portion of the original error.

**Checker transcript excerpt:**
Claim 11: "Stochastic volatility captures most of what Black-Scholes misses in index option prices."
 Status: OVERSTATED

### My Evaluation

I agreed with most of the checker's findings. The citations and numerical results were generally accurate, but the checker identified several instances where the conclusions were stronger than the underlying abstracts justified.

## Retesting After the Skill Revision

After noticing the classification problem in Run 1, I updated my checker instructions to require exactly one classification per numbered claim.
I then started a fresh session and reviewed the original Run 1 brief again.
Unlike Version 1, the updated checker assigned each claim one classification and produced totals that added up correctly.

## Conclusion

Both demonstrations showed that the MCP server could provide Claude Code with access to actual research records and that an independent checker could identify problems in AI-generated research briefs. The biggest lesson for me was that accurate citations do not necessarily mean accurate conclusions. 