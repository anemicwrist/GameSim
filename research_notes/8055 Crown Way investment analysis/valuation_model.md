# Valuation and projection model: 8055 Crown Way, Jonesboro, GA 30238

Model date 2026-10-19 (today's date for the brief: 2026-10-18; every figure below carries the date of its source). Subject: parcel 13211D B011, 1968 four-sided brick ranch, 4 bed / 3 bath per MLS (county card 3/3), 2,117 sq ft per MLS (county 2,119 = 1,575 main block + 544 frame addition), listed 2026-10-13 at $200,000 by Burnie King, Keller Williams Realty Signature Partners (GAMLS #10872111 / FMLS #7853457), estate sale by two out-of-state co-executors, 5 days on market and 0 price drops as of 2026-10-18. It is NOT bank-owned or REO (verification.md claims 1-2 override the scout brief).

Model files (re-run with `python3 valuation_model.py`; numpy 2.5.3):
- Script: `/tmp/claude-0/-home-user-GameSim/5bfe0ab3-48c3-50bc-a339-6dfe509a3a76/scratchpad/valuation_model.py`
- Machine-readable outputs: `/tmp/claude-0/-home-user-GameSim/5bfe0ab3-48c3-50bc-a339-6dfe509a3a76/scratchpad/valuation_outputs.json` (every input carries a `src` and `date` field)

Source precedence: `verification.md` agreed facts and section 5 reconciliations first; then the gap-fill notes; then the raw notes. Where the model makes a judgment that is not in the notes it is labelled "model judgment".

---

## 0. Headline numbers (all ranges, no point forecasts without a band)

| Item | Low | Mid | High | Basis |
|---|---|---|---|---|
| Reconciled as-is market value (Oct 2026) | $186,000 | **$205,000** | $221,000 | 50% sales comparison / 30% AVM / 20% income (section A4) |
| Investor as-is value (what a rental buyer can pay) | $143,000 | $158,000 | $182,000 | investor-tier comp grid; gapfill_5 says $160K-$185K |
| After-repair value (full cosmetic renovation) | $280,000 | $290,000 | $295,000 | verification.md 5c; model's time-adjusted grid mean $280,000 |
| List price vs reconciled mid | | $200,000 = -2.5% | | at market, not a distressed discount |
| Base-case value, year 5 / year 10 (nominal) | | **$233,000 / $273,000** | | momentum + mean reversion mean path (B2) |
| Monte Carlo value, year 5 (p5 / p50 / p95) | $123,000 | $225,000 | $425,000 | 20,000 paths, crash regime on (B3) |
| Monte Carlo value, year 10 (p5 / p50 / p95) | $92,000 | $244,000 | $715,000 | (B3) |
| 2008-replay bear value, year 7 / year 10 | | $106,000 / $137,000 | | FHFA Clayton 2006-2015 replay (B5) |
| Year-1 cash flow at list, fully loaded, 75% LTV at 7.40% | | **-$149/month** | | cap rate 5.34%, cash-on-cash -2.1%, lender DSCR 1.42, NOI coverage 0.86 (C1) |
| Walk-away (max) price for an investor | | **$149,000** ($153,000 if the inspection is clean) | | binding hurdle: base 10-yr levered IRR >= 12% (D) |
| Price that also survives a 2008 replay with cash-on-cash >= 6% | | $119,000 | | all-hurdles price (D) |
| Recommended opening offer | | **$145,000** with 3% seller concessions | | 27.5% below list (D) |

Reading guide: the house is fairly priced for an owner-occupant and roughly $50,000 over-priced for a leveraged rental investor on fully loaded numbers. The gap is not a mispricing to argue about; it is the structural spread between what an FHA buyer will pay and what a 7.4% investor loan can carry.

---

## 1. Inputs (dated, sourced)

| Input | Value | Source (notes file, section) | As of |
|---|---|---|---|
| List price, status | $200,000, Active, 5 DOM, 0 cuts | verification.md claim 1 | 2026-10-18 |
| Living area | 2,117 sf MLS; 2,119 county (1,575 + 544 addition) | verification.md claim 3; gapfill_2 KQ2 | 2026-10-19 |
| 2026 county notice value | $200,500 | verification.md claim 6 | 2026-06-30 |
| 2026 millage, tax district 8 | 39.552 mills (15.052 + 4.500 + 20.000) + $35 streetlight | gapfill_6 KQ1; verification.md 5a | 2026-10-05 |
| Non-homestead tax formula | tax = 0.40 x FMV x 0.039552 + $35 = $3,199/yr at $200,000 | verification.md 5a | 2026 |
| Achieved rent (base / range) | $2,025 / $1,950-$2,100 (lightly refreshed $1,850-$1,950) | gapfill_4 KQ1; verification.md claim 7 | 2026-10-19 |
| AVM rents (unverified) | Zillow $1,994; Redfin $1,876 | property_record.md KQ4 | 2026-10-18 |
| HUD FY2027 SAFMR 4BR, 30238 | $2,320; payment-standard range $2,088-$2,552 | verification.md claim 7 | 2026-10-01 |
| Section 8 contract rent | $2,100 (rent reasonableness cap $2,050-$2,150) | gapfill_4 KQ2 | 2026-10-19 |
| Vacancy and credit loss | 8% | rental_and_operating_costs.md KQ2 | 2026-10-18 |
| Management | 9% of collected + $510/yr leasing | rental_and_operating_costs.md KQ4 | 2026 |
| Maintenance / capex reserve | 7.5% / 10% of gross rent | rental_and_operating_costs.md KQ4 | 2026 |
| Insurance (DP-3) | $1,500/yr, +8%/yr | gapfill_6 KQ3; rental KQ4 (7-10%/yr) | 2026-10-19 |
| Owner utilities | $210/yr | rental_and_operating_costs.md KQ7 | 2026 |
| Rent growth (base) | 2.5%/yr | valuation_methods.md KQ4 (INVH Atlanta +2.8%, ZORI metro +2.1%, county +1.6%) | 2026-09 |
| Tax growth / other opex growth | 3% / 3% per year | rental KQ3 inference (2-6%); model judgment | 2026 |
| Conventional investor rate | 7.40% PMMS + 2.125% LLPA paid as points on a 75% LTV loan | gapfill_6 KQ4 | 2026-10-15 |
| DSCR loan alternative | 6.75% par at 75% LTV; 7.00% at 80% LTV | gapfill_6 KQ4 (HomeAbroad 2026-10-06; Griffin from 7.125% 2026-10-14) | 2026-10-06 |
| Buyer closing costs | 3% of price | rental_and_operating_costs.md KQ7 | 2026 |
| Make-ready (Tier A rent-ready) | $16,500 (range $12,000-$24,500) | gapfill_3 KQ4 | 2026-10-19 |
| Systems contingency | $10,000 base; $25,000 bad inspection | gapfill_3 KQ4 | 2026-10-19 |
| Retail-flip renovation (Tier A+B) | $50,000 (range $37,500-$77,500) | gapfill_3 KQ4; verification.md 5c uses $45,000 | 2026-10-19 |
| Selling costs at exit | 8% (6% commission + 2% closing); flip uses 10% (adds 3% concessions) | comparable_sales.md KQ1 (concessions 2.6-4.1%) | 2026 |
| Eviction event cost | $5,000 | rental_and_operating_costs.md KQ2 ($2,500-$7,000) | 2026 |
| Inflation for real view | 2.6%/yr | market_history KQ1 line 27 | 2026 |
| FHFA Clayton annual index 2000-2025 | 26 values (2000 = 100 ... 2024 = 227.42, 2025 = 222.18) | market_history KQ1; verification.md 5b | 2026-03-31 file |
| Zillow ZHVI ZIP 30238 | $227,054 (Sep 2026); peak $260,568 (May 2024) | market_history KQ2; verification.md claim 8 | 2026-09-30 |
| Beta ZIP to metro | base 1.5, stress 1.8 | verification.md 5b | 2026 |
| Metro drift / sd / AR(1) | 3.5% / 6.5% / 0.65 | valuation_methods.md KQ2, KQ3, KQ5 | 2026 |
| ZIP drift / idiosyncratic sd | 3.0% / 5.6% | verification.md 5b; valuation_methods KQ3 | 2026 |
| Property-level sd | 6%/yr (model judgment; Case-Shiller individual-home residual was 14%) | valuation_methods.md KQ1 | 2026 |
| Crash-regime hazard | 2%/yr (one 2008-type episode in ~50 years of FHFA metro history) | model judgment on market_history KQ1 | 2026 |
| Dynamics coefficients | Capozza alpha 0.33 / beta 0.25 / gamma 0.52 (panel), 0.55 / 0.15 (repeat sales); local AR(1) 0.644; Gallin 0.169 | valuation_methods.md KQ2 | 2002-2026 |

---

## A. Current value

### A1. Sales comparison (adjusted comp grid)

Adjustment conventions (each a stated judgment, from comparable_sales.md KQ5 unless noted): time -6%/yr from sale month to Oct 2026 (verification.md claim 9: Redfin ZIP -8.4% YoY, Zillow ZIP -3.8%, county -3.7%); size $40/sf; age 0.25% of price per year the comp is newer than 1968; $2,000 per bedroom (model judgment); $3,000 per full bath; +$5,000 when the comp has no garage, -$3,000 when it has an attached 2-car; +$5,000 brick over siding; condition: "TLC"/investor-tier comps +$10,000 (subject is county quality A with roof, windows and panel done), refreshed comps -$15,000 (Tier A cost), fully renovated -$45,000 (Tier A+B), renovated with new systems -$60,000; finished basement -$15/sf. Investor-tier comps (buyer mailing address out of area, $56-$74/sf) are weighted 0.5 and every comp is weighted by 1/(1 + gross adjustment %).

| Comp | Sale (net of concessions) | Date | sf / yr / bd / ba | Condition | Net adjustment | Indicated as-is value | Tier | Source |
|---|---|---|---|---|---|---|---|---|
| 9542 Canvasback Ct | $235,000 | 2025-11 | 2,284 / 1992 / 3 / 2.5 | as-is | -$20,205 | $214,795 | owner | comparable_sales KQ1 |
| 1206 Village Path | $233,000 ($243,000 - $10,000) | 2026-05 | 1,817 / 2003 / 4 / 3 | as-is | -$12,212 | $220,788 | owner | comparable_sales KQ1 |
| 8427 Fredericksburg Ct | $205,000 | 2026-05 | 1,825 / 1965 / 4 / 2 | refreshed | +$1,092 | $206,092 | owner | value_add KQ2 |
| 657 Utoy Ct | $197,000 | 2026-07 | 1,775 / 1965 / 3 / 2 | as-is | +$22,202 | $219,202 | owner | gapfill_5 KQ1 |
| 295 River Chase Dr | $238,500 | 2026-05 | 2,060 / 1978 / 3 / 2 | as-is | -$4,645 | $233,855 | owner | gapfill_5 KQ1 |
| 9396 Forest Knoll Dr | $188,000 | 2026-06 | 1,790 / 1979 / 3 / 2.5 | as-is | +$7,650 | $195,650 | owner | gapfill_5 KQ1 |
| 8762 E Bourne Dr | $258,000 | 2025-10 | 1,829 / 1970 / 4 / 4 | unknown | -$8,250 | $249,750 | owner | gapfill_5 KQ1 |
| 8229 Kendrick Rd | $135,000 | 2026-09 | 1,404 / 1969 / 4 / 1.5 | TLC | +$47,008 | $182,008 | investor | value_add KQ2 |
| 7990 Devonshire Dr | $150,000 | 2026-05 | 2,040 + 1,000 bsmt / 1967 / 3 / 1 | TLC | +$7,705 | $157,705 | investor | gapfill_5 KQ1 |
| 45 Royce Dr | $165,000 | 2026-02 | 2,844 / 1970 / 4 / 3 | TLC (estate) | -$21,505 | $143,495 | investor | gapfill_5 KQ1 |

Results: owner-occupant tier (n = 7) min $195,650 / median $219,202 / mean $220,019 / p75 $227,322 / max $249,750 (sd $17,756). Investor tier (n = 3) $143,495 / $157,705 / $182,008. Weighted all-comp indication (owner tier weight 1, investor tier 0.5, each divided by 1 + gross adjustment) $210,969. The owner tier sits at the upper half of the notes' $185,000-$225,000 owner-occupant range (comparable_sales.md KQ5); the investor tier reproduces gapfill_5's $160,000-$185,000 investor range at its low end. No Crown Way or Rosewood Estates sale since 2023 exists to anchor the grid (gapfill_5 KQ1), which is why the gross adjustments run 8-36%.

ARV grid (same adjustments, to "fully renovated" condition): 1692 Pheasant Dr $285,000 (2026-03, the paired comp) -> $277,520 after -$9,975 time; 9383 Woodknoll Way resale $255,000 net (2026-06, light cosmetic flip) -> $294,008; 20 Skylark Ln $265,000 (2026-06, full systems renovation; 1970 vintage assumed) -> $267,055. Mean $279,528. The notes' agreed ARV is $285,000-$295,000, mid $290,000 (verification.md 5c); the model's time-adjusted mean is $280,000 because Pheasant closed seven months ago in a ZIP now down 8.4% YoY. The report carries $290,000 as the mid and $280,000 as the figure a flip should be underwritten on.

### A2. Income approach

Formula (closed form because the tax bill depends on the value being solved): V = (EGI - opex excluding tax - $35) / (cap rate + 0.40 x 39.552/1000). EGI = 12 x rent x (1 - 8%); opex = 9% of EGI + $510 leasing + 7.5% maintenance + 10% capex (both on gross) + $1,500 insurance + $210 utilities. At $200,000 and $2,025 rent: GPR $24,300; vacancy $1,944; EGI $22,356; management $2,522; maintenance $1,822; capex $2,430; insurance $1,500; utilities $210; tax $3,199; opex $11,684 (48.1% of GPR, 55.6% including vacancy); NOI $10,672; cap rate 5.34%; GRM 8.2; rent-to-price 1.01%/month.

Cap-rate range: 5.5% (institutional: INVH 5.1% stabilised acquisition cap Q2 2026; Gordon cross-check 5.4-5.9%; valuation_methods KQ4), 6.5% (model midpoint), 7.4% (Arbor national SFR cap rate Q1 2026, the only published SFR cap-rate series; no Clayton-specific survey exists, valuation_methods KQ4 gap).

| Rent | Cap 7.4% (Arbor) | Cap 6.5% | Cap 5.5% (institutional) |
|---|---|---|---|
| $1,950 (low achieved) | $147,410 | $163,825 | $186,958 |
| $2,025 (base) | **$154,045** | **$171,199** | **$195,373** |
| $2,100 (high / Section 8 contract) | $160,680 | $178,573 | $203,788 |

The income approach is $5,000-$46,000 below list at every rent, which is the whole investment story: the house earns a 5.3% going-in yield against 7.4% debt.

### A3. AVMs with published error bands

| AVM | Value | vs list | Median-error band (+/-1.94%) | 77%-coverage band (+/-5%) | 90%-coverage band (+/-10%) | Date / source |
|---|---|---|---|---|---|---|
| Zestimate | $208,700 | +4.4% | $204,651-$212,749 | $198,265-$219,135 | $187,830-$229,570 | 2026-10-18, property_record KQ4 |
| Redfin Estimate | $201,887 | +0.9% | $197,970-$205,804 | $191,793-$211,981 | $181,698-$222,076 | 2026-10-18, property_record KQ4 |
| Trulia Estimate | $209,000 | +4.5% | $204,945-$213,055 | $198,550-$219,450 | $188,100-$229,900 | 2026-10-18, comparable_sales |
| Movoto | $222,000 | +11.0% | $217,693-$226,307 | $210,900-$233,100 | $199,800-$244,200 | 2026-10-18 (via search), comparable_sales |

Error bands: Redfin's published on-market accuracy for the Clayton County row is a 1.94% median error, 76.7% within 5%, 89.5% within 10% (valuation_methods KQ1, data updated 2026-10-18). Zillow's accuracy table could not be retrieved (valuation_methods KQ1 gap), so the Redfin band is applied to all four as a proxy. For any resale value projected years out, the relevant band is the off-market one: 7.57% median error, only 38% within 5%. AVM range used in reconciliation: low $191,793 (Redfin -5%), mid $205,294 (mean of Zillow and Redfin), high $226,307 (Movoto +1.94%).

### A4. Reconciled current market value

| Approach | Low | Mid | High | Weight |
|---|---|---|---|---|
| Sales comparison (owner tier min / median / p75) | $195,650 | $219,202 | $227,322 | 50% |
| AVMs | $191,793 | $205,294 | $226,307 | 30% |
| Income (cap 7.4% / 6.5% / 5.5% at $2,025 rent) | $154,045 | $171,199 | $195,373 | 20% |
| **Reconciled (rounded to $1,000)** | **$186,000** | **$205,000** | **$221,000** | |
| vs list price $200,000 | -7.0% | +2.5% | +10.5% | |

Rationale: the sales comparison carries half the weight because it is the only approach built on closed transactions, but every comp needed 8-36% of gross adjustment and none is on the subject's street, so it cannot carry more. The AVMs get 30% because two of them have published on-market error bands under 2% and all four, plus the county's 2026 notice value of $200,500, land within a few percent of the list price; that convergence is strong evidence that $200,000 is the market's number for an owner-occupant, not a distressed discount (market_history KQ6 inferred a discount from $/sf alone; the deed-record comps in gapfill_5 and the AVMs do not support it). The income approach gets 20% because the marginal buyer for a dated 4/3 brick ranch in a 73%-renter census tract is as likely an investor as an FHA family (city_and_county_outlook 0, 6), and investor pricing in this ZIP ($56-$74/sf for 2,000+ sf 1960s ranches, gapfill_5) is far below owner-occupant pricing. The mid of $205,000 coincides exactly with comparable_sales.md's own reconciled mid, and the $186,000-$221,000 band brackets the county notice value, the list price and all four AVMs. An investor should not confuse this market value with the price that works for a rental: that is $143,000-$182,000 (investor tier) and, on the hurdles in section D, $149,000.

---

## B. Appreciation projection

### B1. Repeat-sales index trend (FHFA Clayton County, computed from the index values in market_history KQ1)

| Statistic | Value | Formula / note |
|---|---|---|
| CAGR 2000-2025 | **3.24%/yr** | (222.18/100)^(1/25) - 1; verification.md 5b: 3.42% is the 1975-2025 window and is not mixed in |
| CAGR 2000-2024 | 3.48%/yr | to the all-time high |
| Mean / sd of annual returns 2001-2025 | 3.76% / **10.46%** | sample sd of 25 annual changes |
| 2005 peak to 2012 trough | **-48.5%** | 120.86 -> 62.28; prior peak regained 2019 |
| 2025 vs 2024 all-time high | -2.3% | 227.42 -> 222.18 |
| Worst 3-yr / 5-yr window | -31.5% / -46.8% | 2007-2010 / 2007-2012 |
| Negative 5-yr windows | 7 of 21 (33%) | from the 26 annual values 2000-2025 |
| Real CAGR 2000-2025 at 2.6% CPI | +0.6%/yr | |
| FHFA ZIP 30238: CAGR 2000-2025 / 2006-2012 drawdown / 2025 | 3.14% / -54.8% / -9.6% | thin "developmental" index (market_history KQ1) |
| FHFA Atlanta MSA (Q2): CAGR 2000-2026 / 2007-2012 drawdown | 3.99% / -27.3% | |
| Zillow ZHVI 30238: CAGR Dec 2000-Dec 2025 / drawdown from May 2024 peak | 3.06% / -12.9% | |

Trend projection: V_T = V_0 x (1 + 3.24%)^T from V_0 = $205,000, with a +/-1 sd band of 10.46% x sqrt(T) in logs (no autocorrelation; this band understates tail risk because annual returns are serially correlated).

| Horizon | Central (nominal) | -1 sd | +1 sd | Central (real, 2.6% CPI) | At ZIP FHFA 3.25% | At Zillow ZIP 2.86% |
|---|---|---|---|---|---|---|
| 1 yr | $211,652 | $190,634 | $234,987 | $206,288 | $211,663 | $210,863 |
| 3 yr | $225,610 | $188,229 | $270,415 | $208,889 | $225,642 | $223,114 |
| 5 yr | $240,489 | $190,339 | $303,851 | $211,523 | $240,544 | $236,074 |
| 7 yr | $256,349 | $194,382 | $338,069 | $214,190 | $256,429 | $249,786 |
| 10 yr | $282,121 | $202,675 | $392,710 | $218,254 | $282,236 | $271,920 |

This is the "nothing special happens" path. It ignores the fact that the ZIP is 12.9% below its peak with negative 12-month momentum, which the next model handles.

### B2. Momentum plus mean reversion (published coefficients, valuation_methods KQ2)

Specification (Capozza, Hendershott, Mack and Mayer, NBER w9262): dp_t = alpha x dp_(t-1) + beta x (p*_(t-1) - p_(t-1)) + gamma x dp*_t, where p is log price, p* is log fundamental value, dp* is fundamental growth. Three parameterisations are run and averaged: (a) panel estimates alpha 0.33, beta 0.25, gamma 0.52; (b) repeat-sales estimates alpha 0.55, beta 0.15, gamma 0.52; (c) local calibration alpha = ZIP AR(1) 0.644, beta = Gallin's 0.169 on the rent-price ratio, gamma = 1 - alpha. Inputs: last 12-month ZIP log change -3.87% (valuation_methods KQ2); fundamental growth 2.5%/yr (rent growth).

Fundamental anchor (blended 50/50 rent and income):
- Rent: the ZIP's gross rent yield is 9.45% vs a 2016-2026 mean of 8.38% (valuation_methods KQ2) -> log gap +0.120, i.e. prices are 11.4% below the rent-based fundamental ($256,045 for the ZIP's $227,054 ZHVI).
- Income: ZIP ZHVI / Clayton SAIPE household income was 2.91 (2019), 3.38, 4.14, 4.38, 4.41, 4.18 (2024); now 3.56 (ZHVI $227,054 / income $63,715 est. = $59,825 x 1.032^2). Against the 2019-2024 mean of 3.90 the gap is +0.090; against the 2019 pre-pandemic anchor it is -0.201. The two are averaged (-0.055) because Gallin 2003 found prices and income are not cointegrated and the window choice dominates.
- Blended fundamental gap: **+0.032** (prices about 3% below fundamentals; roughly fair value).

| Parameterisation | Yr 1 | Yr 2 | Yr 5 | Yr 10 | Value yr 1 | yr 3 | yr 5 | yr 7 | yr 10 |
|---|---|---|---|---|---|---|---|---|---|
| (a) Capozza panel 0.33 / 0.25 / 0.52 | +0.83% | +2.80% | +3.13% | +2.51% | $206,714 | $219,885 | $234,585 | $248,138 | $267,903 |
| (b) Capozza repeat-sales 0.55 / 0.15 / 0.52 | -0.34% | +2.02% | +4.13% | +2.74% | $204,299 | $215,678 | $233,988 | $252,415 | $276,201 |
| (c) local AR(1) 0.644 + Gallin 0.169 | -1.05% | +1.36% | +4.51% | +2.62% | $202,849 | $212,111 | $231,255 | $251,655 | $275,829 |
| **Mean (base path)** | **-0.19%** | **+2.06%** | **+3.92%** | **+2.62%** | **$204,614** | **$215,868** | **$233,271** | **$250,729** | **$273,284** |

Cross-check: the base path's year-1 change (-0.2%) matches Zillow's ZHVF of -0.5% for 30238 to Sep 2027 (market_history KQ2) within noise, and the 10-year average of 2.9%/yr sits between the FHFA (3.24%) and Zillow (2.86-3.06%) long-run CAGRs. The mechanism is the one valuation_methods KQ2 describes: momentum points down in 2027, the high rent yield pulls prices up from 2028, and growth settles near 2.5-3%.

### B3. Monte Carlo (20,000 paths, annual steps, 10 years)

Structure: ZIP log return in year t = base path drift (B2 mean) + 1.5 x metro shock + ZIP idiosyncratic shock; metro shock is a zero-mean AR(1) with phi 0.65 and unconditional sd 6.5%; ZIP idiosyncratic sd 5.6%; property-level shock sd 6% on top. Crash regime: each year with probability 2% a crash starts that replaces the next ten ZIP returns with the FHFA Clayton 2006-2015 replay (-48.5% at year 7, -33% at year 10, with 2% noise); 18% of paths contain one. Implied annual sd: 11.2% ZIP, 12.7% property (the FHFA county sd is 10.5%, FHFA ZIP 12.6%, Zillow ZIP 15.4%). V_0 = $205,000.

| Horizon | p5 | p25 | p50 | p75 | p95 |
|---|---|---|---|---|---|
| Year 1 | $171,066 | $189,980 | $204,574 | $220,041 | $245,312 |
| Year 3 | $142,745 | $180,248 | $214,121 | $253,099 | $324,883 |
| Year 5 | **$122,702** | $173,614 | **$225,303** | $291,902 | **$425,173** |
| Year 7 | $105,252 | $166,772 | $236,497 | $332,178 | $537,412 |
| Year 10 | **$92,252** | $155,153 | **$244,345** | $383,485 | **$714,809** |

Real (2.6% CPI) percentiles: year 5 $107,924 / $152,703 / $198,167 / $256,744 / $373,963; year 10 $71,368 / $120,029 / $189,030 / $296,671 / $552,989. In real terms the median path is flat to slightly down over ten years, consistent with the county's +0.6%/yr real CAGR since 2000.

Distribution statistics: 40% of paths are below V_0 at year 5 (36.5% with the crash regime off) against the 20-27% historical share of negative 5-year windows cited in valuation_methods KQ3; the model is deliberately more conservative because the historical windows are dominated by the 2012-2022 recovery. 25% of paths see a peak-to-trough drawdown of 40% or more (18% without the crash regime). The 1-year 5th/95th percentiles (-16.6% / +19.7%) are narrower than the Zillow ZIP history (-23.4% / +26.3%) which includes 2008-2009. With the stress beta of 1.8 the year-5 p5 falls to $113,896 and 30% of paths have a 40%+ drawdown. The median at year 10 ($244,345) is below the deterministic base path ($273,284) because the crash paths pull it down; the two should be read together.

### B4. Published forecasts (cross-check)

| Source | Horizon | Forecast | Date / notes file |
|---|---|---|---|
| Zillow ZHVF, ZIP 30238 | to 2027-09-30 | -0.5% | 2026-09-30; market_history KQ2 |
| Zillow ZHVF, Atlanta MSA | to 2027-09-30 | -1.0% | market_history KQ2 |
| Zillow ZHVF, U.S. | to 2027-09-30 | +1.1% | market_history KQ2 |
| Cotality (CoreLogic) HPI forecast, U.S. | to Aug 2027 | +1.6% to +1.7% | 2026-10-06; market_history KQ5 / valuation_methods KQ6 |
| Fannie Mae expectations panel, U.S. | 2027 | about +2% | 2026-07-17 (secondary); market_history KQ5 |
| Federal Reserve baseline, U.S. | Q1 2026 to Q4 2028 | +1.2% total | 2026-02-04 (stale on rates); valuation_methods KQ3 |
| Federal Reserve severely adverse, U.S. | to Q4 2027 trough | -30% | valuation_methods KQ3; times beta 1.8 = -45% to -55% for the ZIP |
| UGA Selig Center, Georgia | 2026 | prices "begin to fall, though not sharply" | 2025-12-16; market_history KQ5 |

The model's base year 1 (-0.2%) and the Monte Carlo median year 1 (-0.2%) agree with Zillow's ZIP forecast; no public model goes beyond 12 months, so years 2-10 rest on the mean-reversion mechanics and the long-run index drift, not on a published number.

### B5. Scenario values and dollar gain or loss

Scenario definitions: Bear (2008 replay) = FHFA Clayton actual annual changes 2006-2015 applied from year 1 (-1.1%, -2.1%, -12.8%, -14.5%, -8.2%, -7.7%, -15.9%, +6.0%, +9.4%, +11.4%). Bear (moderate) = the Monte Carlo 10th percentile value at each horizon. Base = B2 mean path. Bull = +2% year 1, +8% years 2-3, +6%, +5%, +4%, +4%, then +3.5%: rates easing to Zillow's 6.5% end-2027 path and a 2013-2015-type rebound (ZIP +14-28%/yr then) scaled to today's 13% drawdown. Values start from the $205,000 reconciled mid; gains are gross (value minus price) and net of 8% selling costs; real values deflate at 2.6%/yr.

Purchase at the list price, $200,000:

| Scenario | Yr 1 value / gross gain / net gain | Yr 3 | Yr 5 | Yr 7 | Yr 10 | Yr 10 real value |
|---|---|---|---|---|---|---|
| Bear, 2008 replay | $202,829 / +$2,829 / -$13,397 | $173,265 / -$26,735 / -$40,597 | $136,067 / -$63,933 / -$74,818 | $105,638 / -$94,362 / -$102,813 | $136,610 / -$63,390 / -$74,319 | $105,684 |
| Bear, MC p10 | $177,984 / -$22,016 / -$36,255 | $155,552 / -$44,448 / -$56,892 | $139,073 / -$60,927 / -$72,053 | $123,802 / -$76,198 / -$86,103 | $111,022 / -$88,978 / -$97,860 | $85,888 |
| Base | $204,614 / +$4,614 / -$11,755 | $215,868 / +$15,868 / -$1,402 | $233,271 / +$33,271 / +$14,610 | $250,729 / +$50,729 / +$30,671 | $273,284 / +$73,284 / +$51,421 | $211,417 |
| Bull | $209,100 / +$9,100 / -$7,628 | $243,894 / +$43,894 / +$24,383 | $271,454 / +$71,454 / +$49,738 | $293,605 / +$93,605 / +$70,117 | $325,525 / +$125,525 / +$99,483 | $251,832 |

Purchase at the recommended walk-away price, $149,000 (opening offer $145,000 adds $4,000 to every gain):

| Scenario | Yr 1 gross / net gain | Yr 3 | Yr 5 | Yr 7 | Yr 10 | Yr 10 real gain (gross) |
|---|---|---|---|---|---|---|
| Bear, 2008 replay | +$53,829 / +$37,603 | +$24,265 / +$10,403 | -$12,933 / -$23,818 | -$43,362 / -$51,813 | -$12,390 / -$23,319 | -$43,316 |
| Bear, MC p10 | +$28,984 / +$14,745 | +$6,552 / -$5,892 | -$9,927 / -$21,053 | -$25,198 / -$35,103 | -$37,978 / -$46,860 | -$63,112 |
| Base | +$55,614 / +$39,245 | +$66,868 / +$49,598 | +$84,271 / +$65,610 | +$101,729 / +$81,671 | +$124,284 / +$102,421 | +$62,417 |
| Bull | +$60,100 / +$43,372 | +$94,894 / +$75,383 | +$122,454 / +$100,738 | +$144,605 / +$121,117 | +$176,525 / +$150,483 | +$102,832 |

At list the base case does not cover selling costs until year 4 and the real base-case gain at year 10 is +$11,417 before transaction costs; at $149,000 the discount itself is the return, and even the 2008 replay is a $23,000 net loss rather than a $74,000 one.

---

## C. Cash flow

### C1. Monthly pro forma, long-term rental, year 1 (stabilised, after Tier A make-ready)

| Line | Basis | At list $200,000 | At walk-away $149,000 |
|---|---|---|---|
| Gross scheduled rent | $2,025 achieved (gapfill_4) | $2,025 | $2,025 |
| Vacancy and credit loss | 8% | -$162 | -$162 |
| Effective gross income | | $1,863 | $1,863 |
| Property tax | 0.40 x price x 39.552 mills + $35 (2027 FMV capped at price) | -$267 | -$199 |
| Insurance (DP-3) | $1,500/yr | -$125 | -$125 |
| Management + leasing | 9% of EGI + $510/yr | -$210 | -$210 |
| Maintenance | 7.5% of gross | -$152 | -$152 |
| Capex reserve | 10% of gross | -$202 | -$202 |
| Owner utilities / stormwater | $210/yr | -$18 | -$18 |
| Operating expenses | 48.1% / 44.7% of gross | -$974 | -$906 |
| **NOI** | | **$889** | **$957** |
| Debt service, 75% LTV, 30-yr, 7.40% | $150,000 loan / $111,750 loan | -$1,039 | -$774 |
| **Pre-tax cash flow** | | **-$149** | **+$183** |
| Cash invested | 25% down + 3% closing + 2.125% points + $16,500 make-ready + $10,000 contingency | $85,688 | $70,595 |
| Cap rate (NOI / price) | | 5.34% | 7.70% |
| Cash-on-cash | | -2.1% | +3.1% |
| Lender DSCR (gross rent / PITIA) | the ratio DSCR lenders test (gapfill_6 KQ5) | 1.42 | 1.84 |
| NOI coverage (NOI / debt service) | the ratio the owner's bank account tests | 0.86 | 1.24 |
| GRM | | 8.2 | 6.1 |

Both coverage ratios are reported, as verification.md 5c requires: the house qualifies easily for a DSCR loan at list (1.42 > 1.10-1.25 minimums) and still loses $149 a month after reserves. Year-1 cash flow is slightly better than modelled because the 2026 tax bill is prorated at the seller's exempt level (about $1,408, gapfill_6 KQ1); the first full non-homestead bill is tax year 2027. Financing alternatives at list: DSCR loan at 6.75% par with no points, P&I $973, cash flow -$84/mo, cash-on-cash -1.2%; 80% LTV at 7.00%, P&I $1,064, cash flow -$175/mo.

Ten-year base projection at list (rent +2.5%/yr, tax +3%, insurance +8%, other opex +3%): NOI rises from $10,672 to $11,984 while insurance climbs from $1,500 to $2,999 and tax from $3,199 to $4,174; cash flow stays negative every year (-$1,791 in year 1 to -$479 in year 10). Exit at year 10 on the base index path: value $289,781 (V_0 $205,000 + 75% of the $16,500 make-ready, grown by the base path), loan balance $129,904, net proceeds after 8% selling costs $136,695, total profit $39,999 on $85,688 invested.

### C2. Levered IRR by scenario, 5- and 10-year holds, with sale costs

Scenario operating assumptions: bear 2008 replay = rent growth 0%, vacancy 10%, evictions in years 2 and 7, $25,000 contingency; bear MC p10 = rent growth 1%, vacancy 10%, one eviction, $25,000 contingency; base = as above; bull = rent growth 3.5%, vacancy 6%.

| Purchase price | Scenario | IRR 5-yr | IRR 10-yr | Equity multiple 10-yr |
|---|---|---|---|---|
| $200,000 (list) | Bear, 2008 replay | n/a (equity wiped out) | n/a | -0.41 (sale does not repay the loan) |
| | Bear, MC p10 | n/a | n/a | -0.54 |
| | Base | -1.7% | **3.7%** | 1.47 |
| | Bull | 6.8% | 8.2% | 2.22 |
| $149,000 (walk-away) | Bear, 2008 replay | -19.7% | -9.0% | 0.38 |
| | Bear, MC p10 | -17.7% | -15.3% | 0.23 |
| | Base | 14.5% | **12.0%** | 2.83 |
| | Bull | 21.1% | 15.7% | 3.75 |
| $145,000 (opening offer) | Base | 15.7% | 12.7% | 2.96 |

Monte Carlo levered IRR distribution, 10-year hold, base operations (IRR set to -100% where the sale cannot repay the loan): at list p5 -100% / p25 -15.1% / p50 **+1.2%** / p75 +10.1% / p95 +20.1%; 47% of paths return less than zero, 20% beat 12%, 21.5% end with the equity wiped out. At $149,000: p25 +2.2% / p50 **+10.3%** / p75 +17.0% / p95 +25.7%; 20% below zero, 43.5% above 12%, 1.4% wiped out.

### C3. Section 8 variant

Contract rent $2,100 (rent reasonableness caps it near $2,050-$2,150 regardless of the $2,088-$2,552 payment-standard range; gapfill_4 KQ2), vacancy 4% (HAP share paid reliably; 2-4 week lease-up), +$300/yr inspection and administration, no voucher-side rent growth (FY2027 SAFMR fell 4.1%). At list: NOI $990/mo, cash flow **-$48/mo**, cash-on-cash -0.7%, base 10-yr IRR 5.0%. At $149,000: cash flow **+$284/mo**, cash-on-cash 4.8%, base 10-yr IRR 13.4%. The voucher adds about $100/mo of cash flow over the market case through lower vacancy and a slightly higher rent; it does not change the price conclusion. Two cautions from gapfill_4: JHA's actual payment standard is unpublished (call 770-478-7282) and at a $2,088 standard the tenant's share may price out most 4BR voucher holders.

### C4. Flip variant

Assumptions: Tier A+B renovation $50,000 + $10,000 contingency; 2% buyer closing; 6 months holding (tax, insurance, $150/mo utilities); opportunity cost of capital at 7.40% on price plus renovation (no hard-money quote exists in the notes); selling costs 10% of ARV (7% commission and closing + 3% concessions, gapfill_5 shows $6,500-$10,000 concessions on four of five sales).

| Purchase price | ARV $290,000: all-in cost / profit / ROI on cost | ARV $280,000: profit |
|---|---|---|
| $200,000 (list) | $276,500 / **-$15,500** / -5.6% | -$24,500 |
| $185,000 | $260,000 / +$474 / 0.2% | -$8,526 |
| $172,500 (75% rule) | $247,215 / +$13,785 / 5.6% | +$4,785 |
| $158,000 (70% rule) | $231,773 / +$29,227 / 12.6% | +$20,227 |
| $149,000 (walk-away) | $222,189 / +$38,811 / 17.5% | +$29,811 |

Benchmarks: ATTOM Q2 2026 typical gross flip ROI 21.5% U.S., 25.3% Georgia (value_add KQ5). Maximum allowable offer: 70% x $290,000 - $50,000 = $153,000 (75% rule $167,500); at the $280,000 ARV, $146,000. A flip clears the Georgia benchmark only below about $140,000; at $149,000 it is a 17.5% ROI with no margin for a $280,000 outcome plus a cost overrun.

---

## D. Price to buy

### D1. Maximum price by hurdle (base inputs: $2,025 rent, 7.40% + points, 75% LTV, $10,000 contingency)

| Hurdle | Max price | Notes |
|---|---|---|
| Cap rate >= 7.4% (Arbor national SFR, Q1 2026) | $154,045 | the notes' only published market cap rate |
| Cap rate >= 6.5% | $171,199 | |
| Cash-on-cash >= 6% | $127,712 | cash invested includes $26,500 of make-ready and contingency |
| Cash-on-cash >= 8% | $115,082 | |
| Base-case 10-yr levered IRR >= 12% | **$149,149** | binding return hurdle |
| Base-case 10-yr levered IRR >= 10% | $161,036 | |
| NOI coverage >= 1.2 | $152,724 | |
| NOI coverage >= 1.0 (cash-flow break-even) | $177,084 | |
| 2008-replay bear: 10-yr equity multiple >= 1.0 | $118,788 | survives the FHFA 2006-2015 replay with two evictions and a $25,000 contingency |
| MC p10 bear: 10-yr equity multiple >= 1.0 | $111,514 | |
| **Binding return hurdles (cap 7.4% / IRR 12% / NOI cov 1.2)** | **$149,000** | three independent hurdles converge at $149,000-$154,000 |
| **All hurdles incl. cash-on-cash 6% and 2008 survival** | **$119,000** | |
| Clean inspection (no contingency): binding return hurdles / all hurdles | $153,000 / $133,000 | |
| DSCR loan at 6.75%, no points: binding return / all | $154,000 (cap 7.4%) / $123,000 | |
| 80% LTV at 7.00%: binding return / all | $150,000 / $120,000 | |

### D2. Sensitivity of the max price

| Case | Binding return hurdle price | Cap >= 7.4% | CoC >= 6% | IRR >= 12% | NOI cov >= 1.2 | 2008 survival |
|---|---|---|---|---|---|---|
| Base | $149,149 (IRR) | $154,045 | $127,712 | $149,149 | $152,724 | $118,788 |
| Rent -10% ($1,823) | $134,963 (NOI cov) | $136,130 | $110,931 | $138,743 | $134,963 | $109,845 |
| Rent +10% ($2,228) | $159,555 (IRR) | $171,960 | $144,493 | $159,555 | $170,485 | $127,731 |
| Rate -1 pt (6.40%) | $154,045 (cap) | $154,045 | $136,265 | $155,475 | $165,954 | $124,143 |
| Rate +1 pt (8.40%) | $141,045 (NOI cov) | $154,045 | $119,896 | $143,202 | $141,045 | $113,830 |

Exit-cap sensitivity (exit valued as year-11 NOI / exit cap instead of the index path; IRR >= 12% hurdle): 6.0% -> $130,415; 6.5% -> $125,455; 7.0% -> $121,144; 7.5% -> $117,361; 8.0% -> $114,015. A pure-rental exit is worth far less than an owner-occupant exit (year-11 NOI of about $12,300 / 7% = $176,000 against the index path's $290,000), so the recommended price assumes the house is resold to an owner-occupant or at least to a buyer who prices it off comps; if that buyer pool does not exist in 2036, the right price today is $115,000-$130,000. Every $200 of monthly rent moves the max price by about $25,000; every point of rate by about $7,000-$13,000.

### D3. Price ladder

| Price | vs list | Cash in | CF / mo | Cap | CoC | Lender DSCR | NOI cov | IRR 10 base | EM 10 base | IRR 10 bull | EM 10 2008 | Flip profit at $290K ARV |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| $200,000 | 0% | $85,688 | -$149 | 5.34% | -2.1% | 1.42 | 0.86 | 3.7% | 1.47 | 8.2% | -0.41 | -$15,500 |
| $190,000 | -5.0% | $82,728 | -$84 | 5.70% | -1.2% | 1.48 | 0.91 | 5.3% | 1.70 | 9.6% | -0.28 | -$4,850 |
| $185,000 | -7.5% | $81,248 | -$52 | 5.90% | -0.8% | 1.52 | 0.95 | 6.1% | 1.82 | 10.3% | -0.20 | +$474 |
| $172,500 | -13.7% | $77,549 | +$30 | 6.44% | +0.5% | 1.62 | 1.03 | 8.1% | 2.14 | 12.1% | -0.02 | +$13,785 |
| $158,000 | -21.0% | $73,258 | +$124 | 7.18% | +2.0% | 1.75 | 1.15 | 10.5% | 2.55 | 14.3% | 0.22 | +$29,227 |
| $153,000 | -23.5% | $71,778 | +$157 | 7.46% | +2.6% | 1.80 | 1.20 | 11.3% | 2.70 | 15.1% | 0.31 | +$34,551 |
| **$149,000** | -25.5% | $70,595 | +$183 | 7.70% | +3.1% | 1.84 | 1.24 | **12.0%** | 2.83 | 15.7% | 0.38 | +$38,811 |
| **$145,000** | -27.5% | $69,411 | +$209 | 7.96% | +3.6% | 1.89 | 1.28 | 12.7% | 2.96 | 16.3% | 0.46 | +$43,070 |
| $119,000 | -40.5% | $61,717 | +$378 | 10.05% | +7.4% | 2.24 | 1.61 | 17.4% | 3.94 | 20.8% | 1.00 | +$70,758 |

### D4. Recommendation

- **Opening offer: $145,000** (27.5% below list), with a 3% seller concession toward closing, a 10-day due-diligence period (inspection with panel-cover removal, receptacle sampling for aluminum, sewer scope, HVAC and water-heater data plates, radon test) and no financing-appraisal contingency if the buyer can close on a DSCR loan or cash. It sits inside the investor-tier comp indications ($143,000-$182,000), under the 70%-rule MAO ($153,000), and leaves $4,000 of room to the walk-away.
- **Walk-away price: $149,000**, rising to **$153,000** only if the inspection retires the $10,000 systems contingency (HVAC and water heater under 10 years, copper branch wiring, no galvanized supply). Above $153,000 the deal fails every return hurdle in D1 at once.
- **Strictly defensible price: $119,000** if the buyer requires a 6% cash-on-cash and a positive outcome in a full 2008 replay. That is a Q1-2027, aged-listing or off-market number, not a day-one offer.
- The notes' "realistic day-one" band of $185,000-$190,000 (gapfill_5 KQ2, verification.md 5c) is an owner-occupant price: at $185,000 the base 10-year IRR is 6.1%, cash flow is -$52/month and the 2008 replay wipes out the equity. An investor should not pay it.
- Context for the negotiation: the listing is five days old with no price cut; 35.8% of 30238 listings have taken a cut, sale-to-list is 98.5%, median DOM 61, the pending ratio has fallen from 0.50 to 0.35 in a year, and deep discounts ($150,000-$165,000) have only been achieved on listings that aged 5-7 months (gapfill_5 KQ2). The seller is an estate run by two executors 850 miles away after a 2.2-year contested probate, with a still-serviced mortgage of unknown balance and no personal-knowledge disclosure (gapfill_1): speed, certainty and as-is terms are the levers, not the list price being high. Expect the $145,000 offer to be refused now; keep it on the table, re-submit on the first price reduction or at 60-90 days, and let the executors' carrying costs (about $1,408 of 2026 tax, insurance on a vacant house, the mortgage) do the work. The 8088 Dauphin Dr estate transfer (2,204 sf 5/3, $0 deed 2026-04-27, gapfill_5) could become a competing listing and should be watched.

---

## E. Value-add ranking (2026 costs; lifts from the 30238 condition tiers)

Tier evidence (value_add KQ2, gapfill_5 KQ1): dated "TLC" brick ranches $96-$99/sf; cosmetically refreshed $112-$127/sf; fully renovated $133-$148/sf. For 2,117 sf against the $205,000 as-is value: a refresh moves the house to $237,000-$269,000 (lift $32,000-$64,000); a full renovation to $280,000-$295,000 (lift $75,000-$90,000). Package costs: Tier A rent-ready $12,000-$24,500 (central $15,000-$18,000), rent $1,900-$2,025; Tier A+B retail flip $37,500-$77,500 (central $45,000-$55,000), rent $2,025-$2,100 (gapfill_3 KQ4, gapfill_4 KQ1). Each item below is allocated a share of its package's lift; ROI = (value lift - cost) / cost; rent yield = annual rent lift / cost. Ranked by ROI plus five times the rent yield.

| Rank | Improvement | 2026 cost | Expected value lift | Rent lift / mo | Value ROI | Rent yield on cost | Flag |
|---|---|---|---|---|---|---|---|
| 1 | After-the-fact permits / licensed-electrician letter for the panel and the 544 sf addition | $500-$3,000 | $5,000-$20,000 (removes lender-overlay risk) | 0 | +614% | 0% | financeability, do first |
| 2 | Interior paint, ~2,100 sf incl. wallpaper removal | $4,500-$7,500 | $11,000-$22,000 | $25-$50 | +180% | 8% | core refresh |
| 3 | LVP over ~1,170 sf of carpet | $3,500-$7,000 | $10,000-$19,000 | $25-$50 | +174% | 9% | core refresh |
| 4 | Haul-out, deep clean, hardware, smoke/CO, blinds | $2,000-$4,000 | $5,000-$10,000 | $25-$50 | +140% | 15% | core refresh |
| 5 | Bath touch-ups x3 (regrout, vanity, lights, GFCI) | $1,200-$2,500 | $3,000-$6,000 | $0-$25 | +159% | 8% | core refresh |
| 6 | Curb appeal (pressure wash, doors, landscaping) | $2,000-$6,000 | $3,000-$6,000 | $0-$25 | +20% | 4% | core refresh |
| 7 | Kitchen refresh (reface/paint, counters, sink, appliances) | $10,000-$20,000 | $12,000-$19,000 | $50-$100 | +4% | 6% | retail-flip tier only |
| 8 | Two original baths: new surrounds, floors, vanities | $7,000-$16,000 | $9,000-$15,000 | $25-$75 | +5% | 5% | retail-flip tier only |
| 9 | Lighting package, doors/trim, mid-grade LVP upgrade | $3,000-$6,000 | $3,000-$4,000 | $0-$25 | -23% | 3% | retail-flip tier only |
| 10 | Attic insulation top-up, air/duct sealing (net of Georgia Power rebates) | $1,200-$2,500 | $500-$2,000 | $0-$15 | -32% | 5% | defensive; helps a voucher tenant's utility allowance |
| 11 | Primary bath full refresh | $3,500-$6,000 | $3,000-$4,000 | $0-$25 | -27% | 3% | retail-flip tier only |
| 12 | Electric water heater (if over 10 years) | $900-$1,800 | $500-$1,500 | 0 | -26% | 0% | defensive |
| 13 | HVAC as heat pump if end of life (net of $1,500 rebate) | $3,500-$11,000 | $2,000-$6,000 | $0-$25 | -45% | 2% | defensive; 25C credit expired for 2026 work |
| 14 | High-end kitchen (stone, custom cabinets) | $30,000-$65,000 | $16,000-$21,000 | $50-$100 | -61% | 2% | **over-improvement** (ZIP p90 $200/sf; 1955-79 cohort p75 $148/sf) |
| 15 | Primary suite / bath addition | $35,000-$80,000 | $8,000-$24,000 | $25-$50 | -72% | 1% | **over-improvement** (22-30% recovery) |
| 16 | Wood privacy fence replacing chain-link | $2,100-$9,400 | $0-$2,000 | $0-$25 | -83% | 3% | amenity only |
| 17 | Sewer camera scope + lateral repair if needed | $100-$5,300 | 0 | 0 | n/a | n/a | risk mitigation; expected loss avoided ~$1,000-$2,000 |
| 18 | Detached garage to apartment / ADU | $20,000-$50,000 | 0 | 0 | -100% | 0% | **not permitted**: ADU conditional use only in AG/ER/RS-180 (subject RS-110); investor whole-house STR also barred (gapfill_8 KQ4) |
| 19 | Paint the brick exterior | $3,000-$9,000 | -$5,000 to +$2,000 | 0 | -125% | 0% | **not recommended** |

The ranking says the same thing as the comps: the first $16,500 (items 2-6) buys most of the refresh tier and is worth doing under any strategy; items 7-9 only pay if the exit is a retail sale at the full-renovation tier; everything from item 10 down is defensive or an over-improvement. Over-improvement threshold: all-in cost above about $150/sf ($318,000) is not recovered (value_add KQ2).

---

## F. Risk register (probability and impact where the notes allow it)

| Risk | Probability | Impact | Mitigation | Source |
|---|---|---|---|---|
| 2008-style drawdown (>= 40% peak-to-trough) within 10 years | 25% of Monte Carlo paths (18% with the crash regime off); FHFA county fell 48.5% 2005-12; ZIP share of negative 5-yr windows 20-27% | at 75% LTV the equity ($37,250 at $149,000) is wiped out and the loan is under water; 2008-replay 10-yr equity multiple 0.38 at $149,000, -0.41 at list | buy at or below $149,000, hold 10+ years, no forced sale, keep 9 months of PITIA in reserve | valuation_methods KQ3/KQ5; market_history KQ1; model B3 |
| Eviction, non-payment, vacancy | Clayton 38.9 filings per 100 renter households (2023, serial filings inflate); ~10-15%/yr event chance for a screened SFR tenant | $2,500-$7,000 per event plus 1-3 months rent; expected $500-$1,000/yr on top of the 8% vacancy allowance; Clayton courts understaffed | 3x-income screening (needs $73,800 vs $42,403 renter median), voucher tenant, 2-month deposit cap under HB 404 | rental_and_operating_costs KQ2, KQ5 |
| Insurance and property-tax escalation | high (80%+): GA premiums +7-10%/yr; millage above rollback three years running; no HOME Act cap for investors | insurance $1,500 to $2,999 by year 10; tax $2,392 to $3,121 at a $149,000 basis; NOI growth lags rent growth by ~0.5 pt/yr | appeal the 2027 notice to the purchase price within 45 days; DP-3 with 1-2% wind/hail deductible | gapfill_6 KQ1-KQ3 |
| 1968 systems: HVAC, water heater, aluminum branch wiring, galvanized supply, sewer lateral, crawl moisture | HVAC/WH ages unknown (50% replacement within 5 yrs); aluminum wiring ~25% (1965-73 window); galvanized ~50%; lateral ~20%; crawl moisture ~30% | expected $9,000-$12,000 over 5 yrs; bad case $25,000; insurer surcharge or decline on aluminum wiring / FPE panel | inspection with panel cover off, receptacle sampling, sewer scope, data plates; price findings into the offer | gapfill_3 KQ4; builder_and_construction KQ2, KQ4 |
| Airport noise / 65 DNL contour | < 5%: 7.1 mi from the runway complex, no airport overlay on the parcel; ambient noise scores moderate | none on value; no NIP eligibility; Tara Blvd noise may lengthen owner-occupant DOM slightly | confirm with the ATL Department of Aviation noise office before resale | gapfill_8 KQ1; property_record KQ5 |
| Flood | FEMA Zone X, Flood Factor 1/10, county floodplain NO (~1% over 30 yrs) | negligible; no flood insurance required | check drainage at the slab-to-crawl transition | property_record KQ5 |
| Corporate-landlord supply and rent competition | high (70%): 15-16 of 61 subdivision parcels entity-owned; institutional 4BR asks $1,781-$1,985; INVH net seller | achieved rent $115-$140/mo below private asks (already in the $2,025 base); resale competes with institutional dispositions | underwrite $2,000-$2,050; compete on condition; voucher tenancy | gapfill_4 KQ1; valuation_methods KQ4; builder KQ3 |
| School and crime perception capping the owner-occupant exit | persistent (90%): Swint ES 4/10, Jonesboro HS 3-4/10, district #199 of 222; tract 73% renter with $27,500 median income; county Part One crime -22% (2024), -17% (2025) but burglary +19% in 2026 | thin FHA/first-time pool; exit liquidity depends on rate-sensitive buyers; DOM 61; 35.8% of listings cut | plan a 10-year hold; exit as a tenanted asset to an investor if needed (which is why the exit-cap sensitivity matters) | property_record KQ6; city_and_county_outlook 4-6; gapfill_8 KQ3 |
| Property-specific: unpermitted 544 sf addition, panel, roof, windows; garage not on the county record; county 3BR vs MLS 4BR; slab vs crawl | near-certain that no permits exist (none in 2016-2025 exports; assessor permit tab empty); 20-30% that an exit lender's appraiser discounts the addition | value on the 1,575 sf main block alone is $30,000-$50,000 lower; after-the-fact permits $500-$3,000; insurer may require an electrical letter | pull EnerGov history, obtain invoices, after-the-fact permits (item 1 in section E) | gapfill_2; gapfill_7 KQ3; verification claims 3-4 |
| Estate execution: two out-of-state executors, no disclosure, unknown payoff, 2.2-year contested probate | medium (30-40%) of delay or title friction; low (10%) that the payoff exceeds net proceeds at $145,000-$149,000 | closing delay; as-is terms; both executors must sign; certified Letters Testamentary (2026-06-24) | due-diligence period, owner's title policy, ask for lender name and payoff before offering | gapfill_1 |
| Radon (EPA Zone 1; 15-21% of Clayton tests >= 4 pCi/L) and lead paint (pre-1978) | radon 15-21%; lead paint very likely on original trim | mitigation ~$1,000-$2,500 (not locally sourced); lead-safe work practices | radon test during inspection | builder_and_construction KQ2 |
| Rate and exit-financing risk | 30-yr rate 7.40% (3-yr high); Zillow expects 7.1% end-2026 and 6.5% end-2027 | +1 pt on the rate lowers the max price by about $8,000; buyer pool shrinks above 7% | DSCR loan at 6.75% par with a 3-2-1 prepay; refinance if rates fall | valuation_methods KQ6; gapfill_6 KQ4; section D2 |
| Voucher payment standard and rent reasonableness | JHA schedule unpublished; DCA proposed 90% of FMR (June 2026); FY2027 SAFMR -4.1% | contract rent capped near $2,050-$2,150 regardless of a $2,552 ceiling; standard could be $2,088 | call JHA for the standard, utility allowance and RFTA timing before relying on Section 8 | gapfill_4 KQ2 |

---

## G. Limitations

1. No closed sale on Crown Way or in Rosewood Estates since July 2023 and no closed lease in 30238 is public; the comp grid needs 8-36% gross adjustments and the rent is an inference from institutional asking rents. A GAMLS/FMLS agent can pull closed sheets (DOM, concessions, financing) and leased 4BR comps; both would tighten sections A and C materially.
2. The condition of the subject's mechanical systems is unknown; the $10,000-$25,000 contingency band is the model's largest single swing after price and rent.
3. The sales-comparison time adjustment (-6%/yr) and the condition adjustments are judgments; halving the time adjustment raises the owner-tier median by about $4,000 and the ARV by about $5,000.
4. The Zestimate accuracy table was not retrievable; the Redfin Clayton on-market band is used as a proxy for all AVMs.
5. The momentum and mean-reversion coefficients are national or metro estimates from 1979-2015 panels; the fundamental anchor depends on the income window (the 2019 anchor says 20% over-valued, the 2019-2024 mean says 9% under-valued). The Monte Carlo is a reduced-form model with a 2%/yr crash hazard that is a judgment, not an estimate; it is more conservative than the 2000-2026 history (40% vs 20-27% negative five-year windows).
6. Exit values on the index path assume an owner-occupant buyer in year 5 or 10; the exit-cap sensitivity shows a pure-investor exit is worth 35-40% less. Selling costs (8%) and the 75%-of-make-ready value credit are assumptions.
7. Tax is modelled at the adopted 2026 rate with the 2027 FMV capped at the purchase price and 3%/yr growth thereafter; the school board's 20.000-mill vote is confirmed only through secondary reports (gapfill_6 gap). The 2026 bill proration benefit is ignored (conservative).
8. The Fannie Mae 2.125% LLPA and the DSCR par rates are from secondary or lender-marketing sources; no scenario-specific loan quote exists.
9. Depreciation (about $5,800/yr of paper loss on $160,000 of improvements), income taxes and principal paydown are not in the IRRs except through the loan balance at sale; adding depreciation would raise after-tax returns for a high-bracket owner without changing the price conclusion.
10. The flip financing cost is an opportunity cost at the PMMS rate because no hard-money quote is in the notes; a 10-12% hard-money loan would cut the flip profit by roughly $3,000-$5,000 at each price.

## Appendix: formulas used

- Non-homestead tax: 0.40 x FMV x 0.039552 + $35.
- Income value: V = (EGI - opex_ex_tax - 35) / (cap + 0.0158208).
- Comp indication: net price + time + size + age + beds + baths + garage + brick + condition + basement (section A1 conventions).
- Repeat-sales trend: V_T = V_0 (1 + g)^T, band exp(+/- sd sqrt(T)).
- Momentum + mean reversion: dp_t = alpha dp_(t-1) + beta (p* - p)_(t-1) + gamma dp*; gap_t = gap_(t-1) + dp* - dp_t.
- Monte Carlo: r_zip,t = drift_t + beta u_m,t + e_z,t; u_m,t = phi u_m,t-1 + e_m,t with sd(u_m) = 6.5%; r_prop,t = r_zip,t + e_p,t; crash regime replaces r_zip with the FHFA 2006-2015 log changes.
- Pro forma: NOI_t = GPR_t (1 - v) - [9% EGI + 510 (1.03)^(t-1) + 17.5% GPR + tax_t + ins_t + util_t]; CF_t = NOI_t - 12 x PMT - eviction_t.
- Hold return: proceeds_N = V_N (1 - 8%) - balance_N; IRR solves sum CF_t/(1+r)^t = cash invested; equity multiple = (sum CF + proceeds) / cash invested.
- Max price: largest P such that hurdle(P) >= target, by bisection on P in [$40,000, $320,000].
