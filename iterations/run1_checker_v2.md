Research Brief Accuracy Report: demonstrations/run1_brief.md (Checker V2)
I pulled every source abstract the brief cites through AlphaSearch, plus one extra search to test the brief's claim about gaps in the library. All five arXiv IDs and author attributions match the database. I did not modify or create any files.

Evidence that the premium exists: Miao & Sorokina (arXiv:2609.01183)
1. Uses CRSP and OptionMetrics data for 2000–2024 to build a systematic cash-secured short-put strategy on nuclear-related firms.
Status: SUPPORTED. Source: 2609.01183. Evidence: the abstract says this almost word for word ("curated universe of nuclear-related firms").

2. Compares ATM put implied volatility with GARCH realized-volatility forecasts.
Status: SUPPORTED. Source: 2609.01183. Evidence: "compares at-the-money put implied volatility with GARCH-based realized volatility forecasts."

3. Reports positive average option premia, high win rates, and much lower volatility than an equal-weight stock benchmark.
Status: SUPPORTED. Source: 2609.01183. Evidence: the abstract says "positive average option premia, high win rates, and substantially lower volatility than an equal-weight stock benchmark."

4. "This supports a harvestable premium, but only within that sector."
Status: SUPPORTED. Source: 2609.01183. Evidence: the paper asks whether the premium is harvestable and reports positive premia. The brief limits the conclusion to that sector and states the cost caveat right after.

Risks that limit the strategy
5. Miao & Sorokina measure performance before transaction costs and on a fixed universe.
Status: SUPPORTED. Source: 2609.01183. Evidence: "performance is measured before transaction costs and with a fixed universe."

6. "…so the reported premia are an upper bound." The heading also calls this "selection bias."
Status: OVERSTATED. Source: 2609.01183. Evidence: pre-cost figures do overstate net returns. But the abstract does not say the fixed universe causes selection or survivorship bias, and it does not call the results an upper bound. Those are the brief's own inferences.

7. Zhuang shows that finitely many S&P 500 option quotes cannot identify physical crash probabilities.
Status: SUPPORTED. Source: "The Physical Crash Frontier" (2608.23274). Evidence: the abstract says the risk-neutral distribution is one "that finitely many bid and ask quotes do not identify."

8. Even with extra put quotes, the upper end of the crash-probability range stays two to three times the lower end.
Status: SUPPORTED. Source: 2608.23274. Evidence: the extra quotes shrink the range by about 80%, "yet its upper end remains two to three times its lower end." The brief leaves out the 80% figure, but what it says is accurate.

9. Heading: "Drawdowns are understated by Gaussian assumptions."
Status: OVERSTATED. Source: "Drawdown Risk Beyond Brownian Motion" (2608.00127). Evidence: the abstract says the four drawdown measures "move differently, so a single Gaussian table mis-warns." It does not say which way the error goes. It also says the apparent extra drawdown risk under persistence is largely a calibration artifact, not "intrinsic danger."

10. Skewness, fat tails and volatility clustering change drawdown measures, so "a single Gaussian table mis-warns."
Status: SUPPORTED. Source: 2608.00127. Evidence: the quote is accurate and the abstract lists those same factors.

11. "This matters for return streams that are negatively skewed."
Status: UNVERIFIABLE. Source: 2608.00127. Evidence: the abstract varies skewness across strategy types, but it says nothing specific about negatively skewed or short-option return streams. The link to option selling is the brief's own.

12. Zernikov: learned S&P 500 option hedges lost money in adverse states in 2022.
Status: SUPPORTED. Source: "What Does Deep Hedging Actually Learn?" (2605.21696). Evidence: "2022 exposes losses in adverse daily states," and the abstract calls the hedges "regime-fragile."

13. Kumar: "transaction costs dominate the comparison of Bitcoin option hedging methods."
Status: OVERSTATED. Source: "Deep Hedging Under Realistic Market Frictions…" (2608.29025). Evidence: the abstract reports one significant cost saving (Whalley-Wilmott saves $1.79 per episode). It never says costs dominate the comparison. Its main finding, which the brief leaves out, is that none of the deep hedging models beat any classical benchmark on any metric.

14. Kumar: the P&L edge depends on the market regime.
Status: SUPPORTED. Source: 2608.29025. Evidence: in the calmer period, "Whalley-Wilmott's P&L edge shrinks or disappears… so the result depends on market regime."

Limitations and bottom line
15. "Only one retrieved paper tests a VRP-harvesting strategy directly… No retrieved abstract tested broad index put-writing."
Status: UNVERIFIABLE. Source: none (the original run's search results aren't available). Evidence: I can't see what the original six queries returned. However, one search now returns Wysocki, "Harvesting the Volatility Risk Premium: A Learning-to-Rank Approach" (arXiv:2608.24786). That paper tests short-put strategies on S&P 500 weekly options and compares them against the CBOE PUT and WPUT indices. So the gap comes from the brief's retrieval, not from the library.

16. The risk papers are indirect: none measures the losses of a short-option strategy.
Status: SUPPORTED. Sources: 2608.23274, 2608.00127, 2605.21696, 2608.29025. Evidence: they cover crash-probability bounds, drawdown modelling, and hedging methods. None reports the P&L of a short-option strategy.

17. All sources are 2026 arXiv preprints.
Status: SUPPORTED. Sources: all five cited papers. Evidence: every record has year 2026 and an arXiv ID.

18. "Classic VRP literature did not appear in the library."
Status: UNVERIFIABLE. Source: none. Evidence: none of my searches returned pre-2026 VRP papers, but search results can't prove something is absent from the library.

19. "A premium appears harvestable in at least one setting."
Status: SUPPORTED. Source: 2609.01183. Evidence: see claims 3 to 5.

20. "The library does not show it generalizes."
Status: CONTRADICTED. Source: Wysocki (2608.24786). Evidence: the library has a paper that harvests the volatility risk premium on the S&P 500 index, outside the nuclear sector. It is evaluated after fees and margin, and reports out-of-sample Sharpe ratios of 4.31–5.76 that beat the CBOE PUT and WPUT indices. The evidence is limited: there is one hold-out year and a model-selected strategy. Even so, the library does contain evidence of the premium in another setting.

I didn't score the brief's statements about its own method ("six queries", "abstracts only"), since they describe the process rather than make factual claims.

Summary
Category	Claims	Count
SUPPORTED	1, 2, 3, 4, 5, 7, 8, 10, 12, 14, 16, 17, 19	13
OVERSTATED	6, 9, 13	3
CONTRADICTED	20	1
UNVERIFIABLE	11, 15, 18	3
Total		20
The counts add up: 13 + 3 + 1 + 3 = 20.

Highest-priority issues
Claims 20 and 15: the bottom line misses relevant evidence. Wysocki (2608.24786) tests short-put harvesting on the S&P 500 index and is benchmarked against CBOE PUT and WPUT. That undercuts both "the library does not show it generalizes" and the "only one paper" limitation.
Claim 9: the direction of drawdown error is invented. Landolfi says Gaussian tables "mis-warn," not that they understate drawdowns.
Claims 13 and 6: two sources are pushed beyond what they say. Kumar never says costs "dominate," and the brief skips Kumar's main finding that deep hedging failed. For Miao & Sorokina, the "upper bound" and "selection bias" framing goes past what the abstract states.
Overall assessment
Moderately reliable. The citations are accurate, and most descriptions of individual papers closely match their abstracts. The main weakness is coverage: the search missed a paper that directly tests the premium on the index, so the bottom line rules out generalization when the library has evidence for it. Several risk headings also make stronger claims than their sources do. The paper-by-paper findings hold up; the bottom line and limitations need rechecking before submission.