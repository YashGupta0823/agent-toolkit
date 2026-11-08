Research Brief Accuracy Report
Brief reviewed: demonstrations/run2_brief.md
Sources: I ran five AlphaSearch queries and got back all five cited abstracts. The arXiv IDs, author names and quoted phrases all match the records. No files were modified or created.

Claim 1: "Stochastic volatility gives the largest gain over BS… a Heston specification reduced implied-volatility RMSE by 39%… 'the dominant share of pricing improvement'" (S&P 500, three maturities)
Status: SUPPORTED
Source: Option Pricing under Stochastic Volatility and Jumps: A PIDE Framework with Empirical Evidence (Mensah et al., arXiv:2605.30562)
Evidence: The abstract says it uses "S&P500 index option contracts across three maturities." It also says "stochastic volatility accounts for the dominant share of pricing improvement… the Heston specification reduces implied-volatility RMSE by 39%."

Claim 2: Merton or CGMY jumps give "marginal improvements" concentrated at short maturities and deep out-of-the-money strikes.
Status: SUPPORTED
Source: arXiv:2605.30562
Evidence: The abstract matches almost word for word: "marginal improvements concentrated at short maturities and in the deep out-of-the-money region."

Claim 3: Bates jump intensities are "effectively equal to zero" at 60-day maturities, and continuous SV dominates near-term pricing.
Status: SUPPORTED
Source: Stochastic Volatility, Jumps, and Rates: A Unified Framework for Option Pricing and Term-Structure Simulation (Putri et al., arXiv:2605.27945)
Evidence: The abstract says "jump intensities converge to values effectively equal to zero for 60-day maturities" and "continuous stochastic volatility dominates near-term pricing dynamics."

Claim 4: Merton jump-diffusion produces an implied-volatility smile through a risk-neutral mixture of lognormals, and it reduces to BS when jumps vanish.
Status: SUPPORTED
Source: Entropic Dynamics of Jump-Diffusion Option Pricing (Abedi, arXiv:2607.06355)
Evidence: The abstract says "the risk neutral mixture of lognormal distributions generates the implied volatility smile. The Black Scholes results are recovered when jumps vanish." One small point: the heading says "jump models," but the paper derives only Merton.

Claim 5: "For short-maturity barrier options under continuous SV, the leading price term is a time-inhomogeneous BS price," and the correction "materially improves" accuracy.
Status: OVERSTATED (scope)
Source: Short-term barrier option price expansion (Fukasawa, arXiv:2610.00340)
Evidence: The quoted result is accurate, but the abstract covers less ground than the brief suggests:

It covers only up-and-out put barrier options.
It requires the strike and barrier to approach the spot "at the diffusive scale."
It rests on stated weak-convergence and uniform-integrability assumptions.
The brief's wording reads as if the result holds for barrier options in general. The "materially improves" finding comes from the paper's numerical experiments.

Claim 6: "Richer models cost more to compute." The brief quotes Euler schemes as "exhibit[ing] high biases and potential unreliability."
Status: OVERSTATED
Source: Simulation of stochastic volatility models via operator splitting schemes (Hu et al., arXiv:2609.21301)
Evidence: The quote is accurate. However, the abstract is about the bias and reliability of simulation schemes for SV models. It never compares computational cost with Black-Scholes, so the heading's cost claim is the brief's own inference. The abstract does call exact methods "tedious," which hints at a cost burden but does not establish the comparison.

Claim 7 (Limitations): "Only two retrieved papers… report empirical comparisons… both focus on equity index options."
Status: OVERSTATED
Source: arXiv:2605.30562; arXiv:2605.27945
Evidence: Mensah et al. do use S&P 500 index options. Putri et al. describe only "short and medium-maturity equity options," with no index named. Their abstract also reports calibration and model extension, not an explicit comparison with Black-Scholes.

Claim 8 (Limitations): "Mixed evidence on jumps. One study finds jump benefits at short maturities; the other finds jump intensities near zero at 60 days."
Status: OVERSTATED
Source: arXiv:2605.30562; arXiv:2605.27945
Evidence: Mensah et al. call the jump gains "marginal." Putri et al. say their result echoes "findings that jumps contribute marginally to short-term smile fitting." The two abstracts largely agree that jumps add little. Calling them "mixed" overstates the tension. It also conflicts with Finding 2 of the brief, which presents the same two papers as consistent.

Claim 9 (Limitations): "Out-of-sample hedging performance is not established by these sources."
Status: SUPPORTED
Source: All five abstracts
Evidence: None of the five abstracts reports hedging or out-of-sample forecasting results. The empirical work in them is calibration fit only.

Claim 10 (Limitations): "Search returned mostly 2026 papers."
Status: SUPPORTED
Source: All five records
Evidence: All five cited papers have year 2026 in the database.

Claim 11 (Bottom Line): "Stochastic volatility captures most of what Black-Scholes misses in index option prices."
Status: OVERSTATED
Source: arXiv:2605.30562
Evidence: "Dominant share of pricing improvement" means SV accounts for most of the improvement among the models the paper tested. It does not mean SV removes most of Black-Scholes' error. A 39% RMSE reduction leaves about 61% of Black-Scholes' implied-volatility error in place. That evidence comes from one study.

Claim 12 (Bottom Line): "Jumps appear to add modest, regime-specific value, mainly at short maturities and in the deep out-of-the-money wings."
Status: SUPPORTED
Source: arXiv:2605.30562; arXiv:2605.27945
Evidence: This matches Mensah et al.'s "marginal improvements," and Putri et al.'s near-zero jump intensities are consistent with it. The brief also hedges it as tentative.

Minor note: the brief says "the 39% RMSE reduction cannot be checked here." The figure does appear in the abstract. What can't be checked is the method behind it. This doesn't change any classification.

Summary
Total claims reviewed: 12
Status	Count
SUPPORTED	7
OVERSTATED	5
CONTRADICTED	0
UNVERIFIABLE	0
Highest-priority issues:

Bottom line overstates what SV achieves (Claim 11). "Captures most of what Black-Scholes misses" goes beyond the source. The abstract supports SV giving the largest share of improvement, with a 39% RMSE cut in one study, not most of Black-Scholes' error removed.
The "mixed evidence on jumps" limitation (Claim 8) is overstated and inconsistent. Both abstracts describe jump contributions as marginal, and Finding 2 of the brief already treats them as agreeing.
Claims are broader than their sources (Claims 5–7).
The Fukasawa result covers only up-and-out puts near the spot, not barrier options in general.
The "richer models cost more" heading isn't in the Hu et al. abstract.
The Putri et al. paper is described as an index-option empirical comparison, which its abstract doesn't say.
Overall assessment: The brief is reliable at the citation level. All five sources exist, the IDs and authors are correct, every direct quote matches its abstract, and nothing is fabricated or contradicted. The problems are interpretive: the headings, limitations and bottom line read the abstracts more broadly or more strongly than they support. The brief is fine as a tentative overview of abstracts, and the five overstated points should be tightened before submission.