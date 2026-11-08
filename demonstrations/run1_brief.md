# Research Brief: Harvesting the Volatility Risk Premium by Selling Options

**Question:** Can selling options systematically earn a volatility risk premium (VRP), and what risks limit this strategy?

**Source:** AlphaSearch MCP (`search_quant_papers`), six queries. All claims below come from retrieved abstracts only.

## Evidence that the premium exists

The most directly relevant paper retrieved is **Miao & Sorokina (2026), "Harvesting the Variance Risk Premium in Nuclear and Energy Equities" (arXiv:2609.01183)**. Using CRSP and OptionMetrics data for 2000–2024, the authors build a systematic cash-secured short-put strategy on nuclear-related firms. Comparing ATM put implied volatility with GARCH realized-volatility forecasts, they report positive average option premia, high win rates, and much lower volatility than an equal-weight stock benchmark. This supports a harvestable premium, but only within that sector.

## Risks that limit the strategy

- **Costs and selection bias.** Miao & Sorokina state that performance is measured *before transaction costs* and on a *fixed universe*, so the reported premia are an upper bound.
- **Tail risk is hard to pin down.** **Zhuang (2026), "The Physical Crash Frontier" (arXiv:2608.23274)** shows that finitely many S&P 500 option quotes cannot identify physical crash probabilities. Even with extra put quotes, the upper end of the admissible crash-probability range stays two to three times the lower end.
- **Drawdowns are understated by Gaussian assumptions.** **Landolfi (2026), "Drawdown Risk Beyond Brownian Motion" (arXiv:2608.00127)** finds that skewness, fat tails and volatility clustering change drawdown measures, so "a single Gaussian table mis-warns." This matters for return streams that are negatively skewed.
- **Hedging is regime-fragile.** **Zernikov (2026, arXiv:2605.21696)** finds that learned S&P 500 option hedges lost money in adverse states in 2022. **Kumar (2026, arXiv:2608.29025)** finds that transaction costs dominate the comparison of Bitcoin option hedging methods, and that the P&L edge depends on the market regime.

## Limitations of this brief

- Only **one** retrieved paper tests a VRP-harvesting strategy directly, and it covers a narrow sector. No retrieved abstract tested broad index put-writing, straddle selling, or VIX-futures shorting.
- The risk papers are **indirect**: none of them measures the losses of a short-option strategy.
- All sources are 2026 arXiv preprints; classic VRP literature did not appear in the library.
- Abstracts only: magnitudes, Sharpe ratios and crisis losses were unavailable.

**Bottom line:** A premium appears harvestable in at least one setting, limited by crash risk, non-Gaussian drawdowns, costs and regime dependence. The library does not show it generalizes.
