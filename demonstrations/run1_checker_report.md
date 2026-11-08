Research Brief Accuracy Report
Brief reviewed: demonstrations/run1_brief.md
Method: I ran 8 AlphaSearch queries: one aimed at each cited paper, plus broader checks on VRP strategies, classic VRP literature and losses from selling options. No files were modified or created.

Claim 1: Miao & Sorokina use CRSP and OptionMetrics data for 2000–2024 to build a systematic cash-secured short-put strategy on nuclear-related firms. They compare ATM put implied volatility with GARCH realized-volatility forecasts, and report positive average option premia, high win rates and much lower volatility than an equal-weight stock benchmark.
Status: SUPPORTED
Source: "Harvesting the Variance Risk Premium in Nuclear and Energy Equities: A Short-Put Portfolio Derisking Strategy" (arXiv:2609.01183)
Evidence: The abstract matches on data, period, strategy, the IV-vs-GARCH comparison and all three results. One minor gap: the abstract says the universe is "curated" and covers "nuclear and energy-adjacent" firms, and the brief drops "curated."

Claim 2: Performance is measured before transaction costs and on a fixed universe, "so the reported premia are an upper bound."
Status: OVERSTATED
Source: arXiv:2609.01183
Evidence: The abstract does state both caveats. The "upper bound" conclusion and the "selection bias" label are the brief's own inference, though. Missing costs would lower returns. The abstract doesn't say which way the fixed-universe effect cuts or how big it is.

Claim 3: Finitely many S&P 500 option quotes cannot identify physical crash probabilities. Even with extra put quotes, the upper end of the admissible crash-probability range stays two to three times the lower end.
Status: SUPPORTED
Source: "The Physical Crash Frontier: What Finite Option Quotes Can and Cannot Reveal" (arXiv:2608.23274)
Evidence: The abstract says quotes do not identify the pricing kernel or the risk-neutral distribution. It also says extra quotes "shrink the range... by about 80 percent, yet its upper end remains two to three times its lower end." The brief leaves out the 80% narrowing and the model's conditions (power utility, risk aversion of 2, a cap on the index level). That makes the result look more pessimistic than it is, but it doesn't misstate it.

Claim 4: "Drawdowns are understated by Gaussian assumptions." Skewness, fat tails and volatility clustering change drawdown measures, so "a single Gaussian table mis-warns."
Status: OVERSTATED
Source: "Drawdown Risk Beyond Brownian Motion" (arXiv:2608.00127)
Evidence: The quote is accurate. The abstract says "the four measures move differently," which means Gaussian tables err in different directions, not that they always understate drawdowns. The abstract also never discusses negatively skewed or short-option return streams, so the follow-on point that "this matters for negatively skewed streams" is the brief's own extension.

Claim 5: Learned S&P 500 option hedges lost money in adverse states in 2022, so hedging is regime-fragile.
Status: SUPPORTED
Source: "What Does Deep Hedging Actually Learn? Delta Corrections, Regime Fragility, and Symbolic Distillation" (arXiv:2605.21696)
Evidence: The abstract says "2022 exposes losses in adverse daily states" and calls the correction "regime-fragile." Context: these are TD3 deep-hedging agents compared against Black-Scholes delta, not a strategy that harvests VRP.

Claim 6: Transaction costs dominate the comparison of Bitcoin option hedging methods.
Status: OVERSTATED
Source: "Deep Hedging Under Realistic Market Frictions... Bitcoin Options" (arXiv:2608.29025)
Evidence: The abstract reports that Whalley-Wilmott saves a significant $1.79 per episode in costs, and that its P&L and tail-risk gains are "not quite significant." It never says costs "dominate." Its headline finding is that none of the deep-hedging models beat any classical benchmark, and the brief leaves that out.

Claim 7: In the Kumar paper, the P&L edge depends on the market regime.
Status: SUPPORTED
Source: arXiv:2608.29025
Evidence: The abstract says "Whalley-Wilmott's P&L edge shrinks or disappears there while its cost edge holds, so the result depends on market regime."

Claim 8: Only one retrieved paper tests a VRP-harvesting strategy directly. No retrieved abstract tested broad index put-writing.
Status: CONTRADICTED (at the library level)
Source: "Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach," Wysocki (arXiv:2608.24786)
Evidence: The library holds a second direct VRP-harvesting paper that the brief doesn't mention. It tests delta-targeted short puts on S&P 500 zero-day (SPXW) options over 2021–2024, plus a 2025 holdout. It reports out-of-time Sharpe ratios of 4.31–5.76 against CBOE PUT and WPUT benchmarks, with margin, fees and execution assumptions built in. I can't check whether the brief's six queries returned it, but it came back for a basic "volatility risk premium index put writing" query. Either the search missed it or the brief left it out.

Claim 9: "The library does not show it generalizes." The premium is harvestable "in at least one setting."
Status: CONTRADICTED
Source: arXiv:2608.24786; arXiv:2609.01183
Evidence: Wysocki gives library evidence for a second setting: index options, with costs included. That evidence has limits: it's one ML-selected strategy, and the holdout is a single year. So the brief's conclusion needs revising, not just softening. Wysocki also cuts against the brief's cost caveat, because it is a cost-aware test.

Claim 10: The risk papers are indirect, and none measures the losses of a short-option strategy.
Status: SUPPORTED
Source: arXiv:2608.23274, 2608.00127, 2605.21696, 2608.29025
Evidence: None of the four abstracts evaluates P&L from selling options. They cover identifying crash probabilities, a general drawdown framework, and hedging studies.

Claim 11: All sources are 2026 arXiv preprints, and classic VRP literature did not appear in the library.
Status: SUPPORTED
Source: All cited records (year 2026, with arXiv IDs). I also ran a "variance risk premium implied minus realized variance swaps" query.
Evidence: Every cited record lists the year as 2026. My classic-literature query returned only 2026 preprints and no foundational VRP papers.

Claim 12: Six queries were run, and magnitudes and Sharpe ratios were unavailable from abstracts.
Status: UNVERIFIABLE (query count) / OVERSTATED (availability)
Source: The query count can't be checked; arXiv:2608.24786 for availability
Evidence: I can't check how many queries the brief ran. Sharpe ratios and drawdowns are available in at least one relevant abstract: Wysocki reports Sharpe 4.31–5.76 and a maximum drawdown of −2.28%.

Summary
Total claims reviewed: 12
SUPPORTED: 5 (claims 1, 3, 5, 7, 10, 11, counting claim 11 as one; the Kumar paper's points are split across claims 6 and 7)
OVERSTATED: 3 (claims 2, 4, 6), plus the availability part of claim 12
CONTRADICTED: 2 (claims 8, 9)
UNVERIFIABLE: 1 (the query count in claim 12)
Strictly, the counts are: 6 SUPPORTED (1, 3, 5, 7, 10, 11), 3 OVERSTATED (2, 4, 6), 2 CONTRADICTED (8, 9) and 1 mixed (12, UNVERIFIABLE/OVERSTATED).

Highest-priority issues
A directly relevant paper is missing. Wysocki (arXiv:2608.24786) is a cost-aware test of selling index puts. Leaving it out invalidates the claim that "only one paper" exists and weakens the "does not generalize" conclusion (claims 8, 9, 12).
The Landolfi paper is described in one direction. The abstract says Gaussian tables mis-warn in different ways depending on the measure. The brief turns that into Gaussian assumptions "understating" drawdowns (claim 4).
Inferences are stated as findings. "Transaction costs dominate" (Kumar) and "premia are an upper bound" (Miao & Sorokina) aren't in the abstracts (claims 2, 6).
Overall assessment
The brief is partly reliable. Citations, IDs, data descriptions and quotes are accurate, there are no invented sources, and its caveats are generally honest. Its main weakness is missing literature: it overlooks a second, directly relevant VRP-harvesting paper in the same library, which undercuts its bottom line. Several risk points also go a step past what their abstracts say. It needs revision before submission.