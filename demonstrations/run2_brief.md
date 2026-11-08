# Research Brief: Stochastic Volatility and Jump Models vs. Black-Scholes

**Question:** How do stochastic volatility (SV) and jump models compare with Black-Scholes (BS) for option pricing?
**Source:** AlphaSearch MCP (arXiv abstracts only), retrieved 2026-11-08.

## Key Findings

**1. Stochastic volatility gives the largest gain over BS.** On S&P 500 index options across three maturities, a Heston specification reduced implied-volatility RMSE by 39% relative to Black-Scholes. The authors attribute "the dominant share of pricing improvement" to stochastic volatility (Mensah et al., arXiv:2605.30562).

**2. Jumps add only a little, mostly at the edges.** In the same study, adding Merton or CGMY jumps gave "marginal improvements" concentrated at short maturities and deep out-of-the-money strikes (arXiv:2605.30562). Separately, a Bates calibration found jump intensities "effectively equal to zero" at 60-day maturities, and the authors conclude that continuous SV dominates near-term pricing (Putri et al., arXiv:2605.27945).

**3. Jump models explain the smile in theory and contain BS as a special case.** One derivation shows that Merton jump-diffusion produces an implied-volatility smile through a risk-neutral mixture of lognormals, and that it reduces to Black-Scholes when jumps vanish (Abedi, arXiv:2607.06355).

**4. BS can still work as a leading-order approximation.** For short-maturity barrier options under continuous SV, the leading price term is a time-inhomogeneous BS price. An SV-dependent correction "materially improves" accuracy (Fukasawa, arXiv:2610.00340).

**5. Richer models cost more to compute.** Standard Euler discretization for SV models "exhibit[s] high biases and potential unreliability," which has led to specialized simulation schemes (Hu et al., arXiv:2609.21301).

## Limitations

- **Small evidence base.** Only two retrieved papers (arXiv:2605.30562, arXiv:2605.27945) report empirical comparisons. Both are recent and both focus on equity index options.
- **Abstracts only.** Full methods, sample periods, and robustness checks were not reviewed. Figures such as the 39% RMSE reduction cannot be checked here.
- **Mixed evidence on jumps.** One study finds jump benefits at short maturities; the other finds jump intensities near zero at 60 days. The abstracts do not resolve this.
- **Pricing fit is not hedging or forecasting.** The findings concern calibration fit. Out-of-sample hedging performance is not established by these sources.
- **Retrieval bias.** Search returned mostly 2026 papers; foundational studies are underrepresented.

## Bottom Line

The retrieved abstracts suggest that stochastic volatility captures most of what Black-Scholes misses in index option prices. Jumps appear to add modest, regime-specific value, mainly at short maturities and in the deep out-of-the-money wings. These conclusions are tentative given the small, abstract-level evidence base.
