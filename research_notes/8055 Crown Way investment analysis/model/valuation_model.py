#!/usr/bin/env python3
"""
Valuation and projection model for 8055 Crown Way, Jonesboro, GA 30238 (parcel 13211D B011).
Built 2026-10-19 from the research notes in
  /home/user/GameSim/research_notes/8055 Crown Way investment analysis/
Every input carries a 'src' tag naming the notes file (and section) it came from.
verification.md 'agreed facts' and 'Corrections' override the raw notes where they conflict.

Sections:
  A. Current value (sales comparison, income, AVMs, reconciliation)
  B. Appreciation (FHFA repeat-sales trend, momentum+mean-reversion, Monte Carlo, published forecasts)
  C. Cash flow (pro forma, DSCR two ways, 5/10-yr levered IRR by scenario, Section 8, flip)
  D. Price to buy (hurdle-based max price, sensitivities, offer / walk-away)
  E. Value-add ranking
  F. Risk register
Outputs: valuation_outputs.json next to this script, plus a printed summary.
"""
import json, math, os, sys
import numpy as np

OUT_DIR = os.path.dirname(os.path.abspath(__file__))
RNG = np.random.default_rng(20261019)

# ----------------------------------------------------------------------------------------------
# 0. INPUTS (every figure dated and sourced)
# ----------------------------------------------------------------------------------------------
I = {}
def inp(key, value, src, date):
    I[key] = {"value": value, "src": src, "date": date}
    return value

# --- subject / listing (verification.md claims 1-6, agreed facts) ---
LIST_PRICE   = inp("list_price", 200000, "verification.md claim 1; property_record.md KQ1", "2026-10-13 listed; status 2026-10-18")
SF           = inp("sf_mls", 2117, "verification.md claim 3 (MLS 2,117 per appraisal; county 2,119 = 1,575 main + 544 frame addition)", "2026-10-19")
SF_MAIN      = inp("sf_main_block", 1575, "verification.md claim 3 / gapfill_2 KQ2 (A0 MAIN polygon)", "2026-10-19")
YEAR_BUILT   = inp("year_built", 1968, "verification.md claim 3", "2026-10-19")
BEDS, BATHS  = inp("beds_mls", 4, "verification.md claim 4 (county card says 3)", "2026-10-19"), inp("baths_full", 3, "verification.md claim 4", "2026-10-19")
NOTICE_2026  = inp("county_notice_value_2026", 200500, "verification.md claim 6 (notice 06/30/2026)", "2026-06-30")
MILLS_2026   = inp("millage_2026_district8", 39.552, "gapfill_6 KQ1 (15.052 county M&O + 4.500 fire + 20.000 school), adopted 2026-09-24 / 2026-10-05", "2026-10-05")
STREETLIGHT  = inp("streetlight_fee", 35, "property_record.md KQ2 tax-by-authority tab", "2025")
ASSESS_RATIO = inp("assessment_ratio", 0.40, "rental_and_operating_costs.md KQ3 (O.C.G.A. 48-5-7)", "2026")
TAX_GROWTH   = inp("tax_growth_pa", 0.03, "rental_and_operating_costs.md KQ3 inference (2-6%/yr; county adopted above rollback 2024-2026); model uses 3%", "2026")

# --- rent (verification.md claim 7 + gapfill_4) ---
RENT_BASE    = inp("rent_base_achieved", 2025, "gapfill_4 KQ1 (achieved $1,950-$2,100, base $2,000-$2,050; model uses midpoint $2,025)", "2026-10-19")
RENT_LOW     = inp("rent_low", 1950, "gapfill_4 KQ1 low end of achieved range", "2026-10-19")
RENT_HIGH    = inp("rent_high", 2100, "gapfill_4 KQ1 high end of achieved range", "2026-10-19")
RENT_LIGHT   = inp("rent_lightly_refreshed", 1900, "gapfill_4 KQ1 ($1,850-$1,950 lightly refreshed)", "2026-10-19")
RENT_ZEST    = inp("rent_zestimate", 1994, "property_record.md KQ4 (unverified per verification.md claim 7)", "2026-10-18")
RENT_REDFIN  = inp("rent_redfin_estimate", 1876, "property_record.md KQ4 (unverified per verification.md claim 7)", "2026-10-18")
SAFMR_4BR    = inp("hud_fy2027_safmr_4br_30238", 2320, "verification.md claim 7 (HUD FY27_safmrs.xlsx, effective 2026-10-01)", "2026-10-01")
VOUCHER_STD  = inp("voucher_payment_standard_range", [2088, 2320, 2552], "gapfill_4 KQ2 (90/100/110% of SAFMR; JHA table not published)", "2026-10-19")
S8_CONTRACT  = inp("section8_contract_rent", 2100, "gapfill_4 KQ2 (rent reasonableness caps contract rent near $2,050-$2,150)", "2026-10-19")
RENT_GROWTH  = inp("rent_growth_base_pa", 0.025, "valuation_methods.md KQ4 (INVH Atlanta blended +2.8%, ZORI metro +2.1%, county +1.6%; Rental Beast SFR -3%)", "2026-09/10")

# --- operating costs (rental_and_operating_costs.md KQ4/KQ7, corrected by verification.md 5a) ---
VACANCY      = inp("vacancy_credit_loss", 0.08, "rental_and_operating_costs.md KQ2 inference (8% defensible; 5% aggressive)", "2026-10-18")
MGMT_PCT     = inp("management_pct_of_collected", 0.09, "rental_and_operating_costs.md KQ4 (8-10% metro Atlanta)", "2026")
LEASING_FEE  = inp("leasing_fee_pa", 510, "rental_and_operating_costs.md KQ4 (half-month fee over 2-yr tenancy)", "2026")
MAINT_PCT    = inp("maintenance_pct_gross", 0.075, "rental_and_operating_costs.md KQ4 (1968 house)", "2026")
CAPEX_PCT    = inp("capex_reserve_pct_gross", 0.10, "rental_and_operating_costs.md KQ4 (10-15% for >25-yr-old property)", "2026")
INSURANCE    = inp("insurance_dp3_pa", 1500, "gapfill_6 KQ3 (Steadily Atlanta SFR $1,200-$1,700; GA median $1,433)", "2026-10-19")
INS_GROWTH   = inp("insurance_growth_pa", 0.08, "rental_and_operating_costs.md KQ4 (7-10%/yr; Insurify +10% 2026)", "2026")
UTIL_OWNER   = inp("owner_utilities_pa", 210, "rental_and_operating_costs.md KQ7 (CCWA stormwater $5/mo + ~$150 turnover utilities)", "2026")
OPEX_GROWTH  = inp("other_opex_growth_pa", 0.03, "model assumption (CPI-type growth for management/maintenance/utilities)", "2026")

# --- financing (gapfill_6 KQ4) ---
RATE_PMMS    = inp("pmms_30yr", 0.0740, "gapfill_6 KQ4 / market_history KQ3 (Freddie Mac PMMS Oct 15, 2026)", "2026-10-15")
LLPA_PTS     = inp("llpa_investment_70_75ltv", 0.02125, "gapfill_6 KQ4 (Fannie LLPA 2.125% of loan at 70.01-75% LTV; secondary source)", "2026-09-30")
RATE_DSCR    = inp("dscr_par_rate_75ltv", 0.0675, "gapfill_6 KQ4 (HomeAbroad Oct 6, 2026; Griffin 'from 7.125%' Oct 14)", "2026-10-06")
LTV_BASE     = inp("ltv_base", 0.75, "task spec 20-25% down; gapfill_6 (75% LTV conventional/DSCR purchase)", "2026")
LTV_ALT      = inp("ltv_alt", 0.80, "gapfill_6 KQ4 (80% LTV DSCR purchase available)", "2026")
CLOSING_PCT  = inp("buyer_closing_pct", 0.03, "rental_and_operating_costs.md KQ7 (about 3%)", "2026")
MAKE_READY   = inp("make_ready_tier_a", 16500, "gapfill_3 KQ4 (Tier A rent-ready $12,000-$24,500, central $15,000-$18,000)", "2026-10-19")
SYS_CONTING  = inp("systems_contingency_base", 10000, "gapfill_3 KQ4 ($10,000 clean inspection to $25,000 bad inspection)", "2026-10-19")
SYS_CONTING_BAD = inp("systems_contingency_bad", 25000, "gapfill_3 KQ4", "2026-10-19")
RENO_FLIP    = inp("renovation_flip_tier_ab", 50000, "gapfill_3 KQ4 (Tier A+B $37,500-$77,500, central $45,000-$55,000); verification.md 5c uses $45,000", "2026-10-19")
SELL_COST    = inp("selling_cost_pct", 0.08, "comparable_sales.md KQ1 (concessions 2.6-4.1%) + 6% commission; model uses 8% all-in at sale", "2026")
EVICTION_COST= inp("eviction_event_cost", 5000, "rental_and_operating_costs.md KQ2 ($2,500-$7,000 per event)", "2026")

# --- value anchors (verification.md 5c, gapfill_5, comparable_sales.md KQ5) ---
ARV_MID      = inp("arv_mid", 290000, "verification.md 5c / gapfill_5 KQ1 (1692 Pheasant Dr $285,000 2026-03-12; ARV $285K-$295K)", "2026-03-12")
ARV_LOW      = inp("arv_low", 280000, "verification.md 5c (records-verifier cap kept as downside)", "2026-10-19")
ARV_HIGH     = inp("arv_high", 295000, "verification.md 5c", "2026-10-19")
INVESTOR_ASIS= inp("investor_asis_range", [160000, 185000], "gapfill_5 KQ1 inference (investor as-is $160K-$185K)", "2026-10-19")
OWNER_ASIS   = inp("owner_occupant_asis_range", [185000, 205000, 225000], "comparable_sales.md KQ5 (low/mid/high; verification.md 5c calls it an owner-occupant range)", "2026-10-18")

# --- AVMs (property_record.md KQ4; valuation_methods.md KQ1 for error bands) ---
AVM = {
    "Zestimate":       {"value": 208700, "date": "2026-10-18", "src": "property_record.md KQ4"},
    "Redfin Estimate": {"value": 201887, "date": "2026-10-18", "src": "property_record.md KQ4 / value_add KQ2"},
    "Trulia Estimate": {"value": 209000, "date": "2026-10-18", "src": "comparable_sales.md subject baseline"},
    "Movoto":          {"value": 222000, "date": "2026-10-18", "src": "comparable_sales.md subject baseline (via search)"},
}
REDFIN_ERR_ONMKT_CLAYTON = inp("redfin_onmarket_median_error_clayton", 0.0194, "valuation_methods.md KQ1 (Clayton County row: 1.94% median; 76.7% within 5%, 89.5% within 10%)", "2026-10-18")
REDFIN_ERR_OFFMKT_CLAYTON= inp("redfin_offmarket_median_error_clayton", 0.0757, "valuation_methods.md KQ1 (7.57%; 38.2% within 5%, 59.1% within 10%)", "2026-10-18")

# --- index history (market_history_and_forecasts.md KQ1; FHFA hpi_at_county.xlsx last updated 2026-03-31) ---
FHFA_CLAYTON = {2000:100.00,2001:107.16,2002:112.32,2003:115.03,2004:118.19,2005:120.86,2006:119.58,2007:117.08,
                2008:102.15,2009:87.35,2010:80.22,2011:74.03,2012:62.28,2013:66.04,2014:72.27,2015:80.54,2016:86.08,
                2017:95.99,2018:111.17,2019:124.24,2020:132.29,2021:159.42,2022:202.62,2023:222.67,2024:227.42,2025:222.18}
FHFA_ZIP = {2000:100.00,2005:119.74,2006:120.47,2007:117.35,2008:103.09,2009:91.56,2010:78.88,2011:74.27,2012:54.48,
            2013:55.71,2014:66.62,2015:78.72,2016:86.19,2017:93.94,2018:110.56,2019:125.60,2020:131.10,2021:161.52,
            2022:201.69,2023:230.03,2024:239.35,2025:216.44}
FHFA_MSA_Q2 = {2000:135.4,2005:171.8,2007:182.8,2009:168.1,2011:138.1,2012:132.8,2014:155.1,2016:179.0,2018:207.5,
               2020:231.2,2021:262.5,2022:329.3,2023:347.4,2024:363.1,2025:370.7,2026:374.5}
ZHVI_ZIP_DEC = {2000:109197,2005:133098,2007:127394,2008:94705,2009:61832,2011:48804,2012:48078,2014:77304,2016:96083,
                2018:132214,2019:147894,2020:166674,2021:212932,2022:252260,2023:255839,2024:249827,2025:232129}
ZHVI_ZIP_NOW = inp("zhvi_zip30238_sep2026", 227054, "market_history KQ2 (Zillow ZHVI mid-tier SA, 2026-09-30)", "2026-09-30")
ZHVI_ZIP_PEAK= inp("zhvi_zip30238_peak", 260568, "verification.md claim 8 (May 2024)", "2024-05-31")
ZHVI_COUNTY  = inp("zhvi_clayton_sep2026", 228970, "market_history KQ2", "2026-09-30")
ZIP_12MO_LOG = inp("zip_last12mo_log_change", -0.0387, "valuation_methods.md KQ2 inference (ZIP ZHVI 12-month log change)", "2026-09-30")
MSA_12MO     = inp("atlanta_msa_zhvi_1yr", -0.015, "market_history KQ2 (Atlanta metro ZHVI 1-yr -1.5%)", "2026-09-30")
ZORI_ZIP     = inp("zori_zip30238_sep2026", 1788, "valuation_methods.md KQ4 (Zillow ZORI)", "2026-09-30")
GROSS_YIELD_NOW  = inp("zip_gross_rent_yield_now", 0.0945, "valuation_methods.md KQ2 (12 x ZORI / ZHVI)", "2026-09-30")
GROSS_YIELD_MEAN = inp("zip_gross_rent_yield_mean_2016_2026", 0.0838, "valuation_methods.md KQ2", "2016-2026")
INCOME_SAIPE = {2013:40606,2019:50737,2020:49370,2021:51422,2022:57625,2023:57974,2024:59825}   # market_history KQ4 (FRED SAIPE)
INCOME_GROWTH= inp("county_income_growth_pa", 0.032, "market_history KQ4 (SAIPE 2024 +3.2% y/y)", "2024")
CPI          = inp("inflation_pa", 0.026, "market_history KQ1 line 27 (~2.6%/yr CPI used for real appreciation); FOMC PCE 2.3% 2027 / 2.1% 2028", "2026-09-16")

# --- dynamics coefficients (valuation_methods.md KQ2/KQ3) ---
CAPOZZA_PANEL = inp("capozza_alpha_beta_gamma_panel", [0.33, 0.25, 0.52], "valuation_methods.md KQ2 (Capozza-Hendershott-Mack-Mayer NBER w9262: alpha 0.33, beta 0.25, gamma 0.52)", "2002")
CAPOZZA_RS    = inp("capozza_alpha_beta_repeat_sales", [0.55, 0.15, 0.52], "valuation_methods.md KQ2 (repeat-sales data: alpha 0.55, beta 0.15; gamma as panel)", "2002")
LOCAL_AR1     = inp("zip_ar1_log_changes", 0.644, "valuation_methods.md KQ2 (Zillow ZHVI 30238 2001-2026 AR(1) 0.644)", "2026")
GALLIN_BETA   = inp("gallin_rent_price_coeff", 0.169, "valuation_methods.md KQ2 (Gallin FEDS 2004-50: 0.169/yr on log rent-price ratio)", "2004")
GN_LAGS       = inp("glaeser_nathanson_autocorr", [0.67,0.26,-0.10,-0.26,-0.28], "valuation_methods.md KQ2 (NBER w21037 lags 1-5)", "2015")
BETA_ZIP_BASE = inp("beta_zip_to_metro_base", 1.5, "verification.md 5b (FHFA 1.33-1.48; Zillow 2013-2026 1.47-1.55; base 1.3-1.5; stress 1.8)", "2026")
BETA_ZIP_STRESS=inp("beta_zip_to_metro_stress", 1.8, "verification.md 5b / valuation_methods KQ3 (full-cycle Zillow 1.82)", "2026")
MU_METRO      = inp("metro_long_run_log_drift", 0.035, "valuation_methods.md KQ5 (Zillow 2000-26 3.35%; CS 3.70%; FHFA 4.03-4.58%) -> 3.5%", "2026")
SD_METRO      = inp("metro_annual_sd", 0.065, "valuation_methods.md KQ3 (metro sd 5-8%: FHFA 5.04%, CS 6.50%, Zillow 7.86%)", "2026")
PHI_METRO     = inp("metro_ar1", 0.65, "valuation_methods.md KQ2 (Atlanta AR(1) 0.54-0.72)", "2026")
MU_ZIP        = inp("zip_long_run_log_drift", 0.030, "verification.md 5b (FHFA county 2000-25 3.24%; FHFA ZIP 1980-2025 3.25%; Zillow ZIP 2.86%) -> 3.0%", "2026")
SD_ZIP_IDIO   = inp("zip_idiosyncratic_sd", 0.056, "valuation_methods.md KQ3 (residual sd 5.58% of ZIP on metro regression)", "2026")
SD_PROPERTY   = inp("property_idiosyncratic_sd", 0.06, "valuation_methods.md KQ1/KQ3 (Case-Shiller individual-home residual ~14% 1970-86; 'lower if the AVM band is trusted'); model uses 6%", "2026")
CRASH_HAZARD  = inp("crash_regime_hazard_pa", 0.02, "model assumption: one 2008-type episode in ~50 years of FHFA metro history (1976-2026) -> 2%/yr", "2026")
N_PATHS       = 20000
HORIZONS      = [1,3,5,7,10]

# --- published forecasts (market_history KQ5 / valuation_methods KQ6) ---
FORECASTS = [
    {"source":"Zillow ZHVF ZIP 30238","horizon":"to 2027-09-30","pct":-0.005,"date":"2026-09-30","src":"market_history KQ2"},
    {"source":"Zillow ZHVF Atlanta MSA","horizon":"to 2027-09-30","pct":-0.010,"date":"2026-09-30","src":"market_history KQ2"},
    {"source":"Zillow ZHVF United States","horizon":"to 2027-09-30","pct":0.011,"date":"2026-09-30","src":"market_history KQ2"},
    {"source":"Cotality (CoreLogic) HPI Forecast, U.S.","horizon":"to 2027-08","pct":0.016,"date":"2026-10-06","src":"market_history KQ5 (+1.6%; valuation_methods KQ6 cites +1.7%)"},
    {"source":"Fannie Mae Home Price Expectations panel, U.S.","horizon":"calendar 2027","pct":0.02,"date":"2026-07-17","src":"market_history KQ5 (secondary: Ramsey Solutions)"},
    {"source":"Federal Reserve 2026 baseline scenario, U.S.","horizon":"Q1 2026 to Q4 2028 (3 yrs)","pct":0.012,"date":"2026-02-04","src":"valuation_methods KQ3/KQ6 (stale on rates)"},
    {"source":"Federal Reserve 2026 severely adverse, U.S.","horizon":"to Q4 2027 trough","pct":-0.30,"date":"2026-02-04","src":"valuation_methods KQ3"},
    {"source":"UGA Selig Center (Georgia)","horizon":"2026","pct":None,"date":"2025-12-16","src":"market_history KQ5 ('prices begin to fall, though not sharply')"},
]

# ----------------------------------------------------------------------------------------------
# helpers
# ----------------------------------------------------------------------------------------------
def pmt(principal, annual_rate, n_months=360):
    r = annual_rate/12
    return principal * r / (1 - (1+r)**-n_months)

def loan_balance(principal, annual_rate, months_paid, n_months=360):
    r = annual_rate/12
    p = pmt(principal, annual_rate, n_months)
    return principal*(1+r)**months_paid - p*((1+r)**months_paid - 1)/r

def irr(cashflows, lo=-0.99, hi=2.0, tol=1e-7):
    cf = np.asarray(cashflows, dtype=float)
    t = np.arange(len(cf))
    def npv(r): return np.sum(cf/(1+r)**t)
    f_lo, f_hi = npv(lo), npv(hi)
    if f_lo*f_hi > 0:
        return float('nan')
    for _ in range(200):
        mid = (lo+hi)/2
        f_mid = npv(mid)
        if abs(f_mid) < tol: return mid
        if f_lo*f_mid < 0: hi, f_hi = mid, f_mid
        else: lo, f_lo = mid, f_mid
    return (lo+hi)/2

def irr_vec(cf_matrix, lo=-0.99, hi=2.0, iters=80):
    """cf_matrix: (n_paths, T+1). Vectorised bisection IRR."""
    cf = np.asarray(cf_matrix, dtype=float)
    t = np.arange(cf.shape[1])
    lo_a = np.full(cf.shape[0], lo); hi_a = np.full(cf.shape[0], hi)
    def npv(r): return (cf/(1+r[:,None])**t[None,:]).sum(axis=1)
    f_lo = npv(lo_a); f_hi = npv(hi_a)
    bracketed = (f_lo > 0) & (f_hi < 0)          # a root exists only where early flows are repaid by later ones
    for _ in range(iters):
        mid = (lo_a+hi_a)/2
        f_mid = npv(mid)
        left = f_lo*f_mid < 0
        hi_a = np.where(left, mid, hi_a)
        lo_a = np.where(left, lo_a, mid)
        f_lo = np.where(left, f_lo, f_mid)
    r = (lo_a+hi_a)/2
    return np.where(bracketed, r, -1.0)          # -100%: the sale proceeds do not repay the loan (total loss of equity or worse)

def tax_nonhomestead(fmv):
    return ASSESS_RATIO*fmv*MILLS_2026/1000 + STREETLIGHT

def cagr(v0, v1, years): return (v1/v0)**(1/years) - 1

# ----------------------------------------------------------------------------------------------
# A. CURRENT VALUE
# ----------------------------------------------------------------------------------------------
A = {}

# A1. Sales comparison grid. Adjustment conventions (stated judgments, all from comparable_sales.md KQ5 unless noted):
ADJ = {
    "time_pa": inp("adj_time_pa", -0.06, "verification.md claim 9 (Redfin ZIP -8.4% YoY Sep 2026; Zillow ZIP -3.8%; county ZHVI -3.7%) -> -6%/yr applied from sale date to Oct 2026", "2026-10-19"),
    "size_per_sf": inp("adj_size_per_sf", 40, "comparable_sales.md KQ5 ($40/sf marginal)", "2026-10-18"),
    "age_per_year": inp("adj_age_pct_per_year", 0.0025, "comparable_sales.md KQ5 (-5% for 24 yrs, -10% for 35 yrs -> ~0.25%/yr)", "2026-10-18"),
    "bath": inp("adj_full_bath", 3000, "comparable_sales.md KQ5", "2026-10-18"),
    "bed": inp("adj_bedroom", 2000, "model judgment (comparable_sales used +$3,000 for bed/bath combined)", "2026-10-19"),
    "garage_none": inp("adj_garage_vs_none", 5000, "comparable_sales.md KQ5 (detached 2-car + workshop vs none)", "2026-10-18"),
    "garage_attached": inp("adj_garage_vs_attached", -3000, "comparable_sales.md KQ5", "2026-10-18"),
    "brick": inp("adj_brick_vs_siding", 5000, "comparable_sales.md KQ5", "2026-10-18"),
    "cond_tlc": inp("adj_condition_tlc", 10000, "model judgment: county quality F / 'needs TLC' comps vs subject (quality A, roof/windows/panel done)", "2026-10-19"),
    "cond_refreshed": inp("adj_condition_refreshed", -15000, "gapfill_3 KQ4 (Tier A rent-ready $12,000-$24,500) -> -$15,000 for paint/floor/appliance comps", "2026-10-19"),
    "cond_renovated": inp("adj_condition_renovated", -45000, "verification.md 5c / gapfill_3 KQ4 (Tier A+B central $45,000-$55,000)", "2026-10-19"),
    "cond_renovated_systems": inp("adj_condition_renovated_systems", -60000, "gapfill_3 KQ4 (Tier A+B plus new roof/HVAC/plumbing/electrical ~ +$15,000)", "2026-10-19"),
    "basement_per_sf": inp("adj_finished_basement_per_sf", -15, "model judgment: finished below-grade area at $15/sf in this ZIP", "2026-10-19"),
}
# months from sale date to 2026-10-19
def months_ago(y, m): return (2026 - y)*12 + (10 - m)

# comp: (name, price, concessions, sf, year, beds, baths, garage, brick, condition, (y,m), basement_sf, tier, src)
COMPS = [
    ("9542 Canvasback Ct", 235000, 0, 2284, 1992, 3, 2.5, "none", False, "asis", (2025,11), 0, "owner", "comparable_sales.md KQ1 (Loyal Home Realty; sold 3.7% below final list)"),
    ("1206 Village Path", 243000, 10000, 1817, 2003, 4, 3, "attached", False, "asis", (2026,5), 0, "owner", "comparable_sales.md KQ1 (Compass; $10,000 concessions; original finishes)"),
    ("8427 Fredericksburg Ct", 205000, 0, 1825, 1965, 4, 2, "none", None, "refreshed", (2026,5), 0, "owner", "value_add KQ2 (Redfin; 'new paint, new floor')"),
    ("657 Utoy Ct", 197000, 0, 1775, 1965, 3, 2, "none", None, "asis", (2026,7), 0, "owner", "gapfill_5 KQ1 (county GIS; quality F; mailing Jonesboro)"),
    ("295 River Chase Dr", 238500, 0, 2060, 1978, 3, 2, None, None, "asis", (2026,5), 0, "owner", "gapfill_5 KQ1 (county GIS; quality A)"),
    ("9396 Forest Knoll Dr", 188000, 0, 1790, 1979, 3, 2.5, None, None, "asis", (2026,6), 0, "owner", "gapfill_5 KQ1 (county GIS; H1)"),
    ("8762 E Bourne Dr", 258000, 0, 1829, 1970, 4, 4, None, None, "asis", (2025,10), 0, "owner", "gapfill_5 KQ1 (county GIS; quality A; condition unknown)"),
    ("8229 Kendrick Rd", 135000, 0, 1404, 1969, 4, 1.5, "none", True, "tlc", (2026,9), 0, "investor", "value_add KQ2 (Redfin; four-sided brick 'Needs TLC')"),
    ("7990 Devonshire Dr", 150000, 0, 2040, 1967, 3, 1, "none", None, "tlc", (2026,5), 1000, "investor", "gapfill_5 KQ1 (county GIS; quality F; Lawrenceville buyer; $130K deed 5 wks earlier)"),
    ("45 Royce Dr", 165000, 0, 2844, 1970, 4, 3, "none", None, "tlc", (2026,2), 0, "investor", "gapfill_5 KQ1 (county GIS; quality F; H3T estate seller)"),
]
ARV_COMPS = [
    ("1692 Pheasant Dr", 285000, 0, 2144, 1970, 4, 3, "none", True, "renovated", (2026,3), 0, "owner", "gapfill_5 KQ1 (GAMLS #10668549; 96.6% of $294,900 list)"),
    ("9383 Woodknoll Way (resale)", 265000, 10000, 1764, 1979, 3, 2, "attached", False, "refreshed", (2026,6), 0, "owner", "gapfill_5 KQ3 (FMLS #7741258; 'updated' cosmetics; $10,000 concessions)"),
    ("20 Skylark Ln", 265000, 0, 1600, 1970, 4, 2, None, None, "renovated_systems", (2026,6), 0, "owner", "value_add KQ2 (Redfin; full renovation incl. roof/HVAC/plumbing/electrical; vintage 'similar' -> 1970 assumed)"),
]

def adjust_comp(c, to_condition="asis"):
    name, price, conc, sf, yr, bd, ba, gar, brick, cond, (sy, sm), bsmt, tier, src = c
    net = price - conc
    adj = {}
    adj["time"] = net * ADJ["time_pa"] * months_ago(sy, sm)/12
    adj["size"] = (SF - sf) * ADJ["size_per_sf"]
    adj["age"]  = -net * ADJ["age_per_year"] * (yr - YEAR_BUILT)        # comp newer -> negative
    adj["beds"] = (BEDS - bd) * ADJ["bed"]
    adj["baths"]= (BATHS - ba) * ADJ["bath"]
    adj["garage"] = ADJ["garage_none"] if gar == "none" else (ADJ["garage_attached"] if gar == "attached" else 0)
    adj["brick"] = ADJ["brick"] if brick is False else 0
    cond_map = {"asis":0, "tlc":ADJ["cond_tlc"], "refreshed":ADJ["cond_refreshed"], "renovated":ADJ["cond_renovated"], "renovated_systems":ADJ["cond_renovated_systems"]}
    adj["condition"] = cond_map[cond] if to_condition == "asis" else (cond_map[cond] - cond_map["renovated"])
    adj["basement"] = bsmt * ADJ["basement_per_sf"]
    total = sum(adj.values())
    ind = net + total
    gross_pct = sum(abs(v) for v in adj.values())/net
    return {"comp": name, "sale_price": price, "concessions": conc, "net_price": net, "sf": sf, "year": yr, "beds": bd, "baths": ba,
            "sale_ym": f"{sy}-{sm:02d}", "condition": cond, "tier": tier, "adjustments": {k: round(v) for k,v in adj.items()},
            "net_adjustment": round(total), "gross_adj_pct": round(gross_pct,3), "indicated_value": round(ind), "src": src}

grid = [adjust_comp(c) for c in COMPS]
owner_ind = np.array([g["indicated_value"] for g in grid if g["tier"]=="owner"])
inv_ind   = np.array([g["indicated_value"] for g in grid if g["tier"]=="investor"])
w = np.array([1.0 if g["tier"]=="owner" else 0.5 for g in grid]); ind = np.array([g["indicated_value"] for g in grid])
# weight also by 1/(1+gross adjustment) so heavily adjusted comps count less
wg = w / (1 + np.array([g["gross_adj_pct"] for g in grid]))
sc_weighted = float(np.sum(wg*ind)/np.sum(wg))
A["sales_comparison"] = {
    "grid": grid,
    "owner_tier": {"n": int(len(owner_ind)), "min": float(owner_ind.min()), "median": float(np.median(owner_ind)), "mean": float(owner_ind.mean()), "max": float(owner_ind.max()), "sd": float(owner_ind.std(ddof=1))},
    "investor_tier": {"n": int(len(inv_ind)), "min": float(inv_ind.min()), "median": float(np.median(inv_ind)), "mean": float(inv_ind.mean()), "max": float(inv_ind.max())},
    "weighted_all": sc_weighted,
    "range_low_mid_high": [float(owner_ind.min()), float(np.median(owner_ind)), float(np.percentile(owner_ind, 75))],
    "notes_range_owner": OWNER_ASIS, "notes_range_investor": INVESTOR_ASIS,
    "method": "indication = net price + time(-6%/yr) + size($40/sf) + age(0.25%/yr) + beds($2,000) + baths($3,000) + garage + brick + condition + basement; weights = 1 (owner tier) / 0.5 (investor tier), divided by (1 + gross adjustment %)",
}
arv_grid = [adjust_comp(c, to_condition="renovated") for c in ARV_COMPS]
arv_ind = np.array([g["indicated_value"] for g in arv_grid])
A["arv_grid"] = {"grid": arv_grid, "mean": float(arv_ind.mean()), "min": float(arv_ind.min()), "max": float(arv_ind.max()),
                 "notes_arv": [ARV_LOW, ARV_MID, ARV_HIGH], "unverified_upper_bracket": "8919 Saddlewood $325,000 (2,210 sf, 1975, 2026-06-03); 229 Deerfield $316,000 (2,468 sf, 1978, 2026-08-05); 9268 Choctaw $310,000 (gapfill_5; condition unverified)"}

# A2. Income approach: V = NOI / cap, with tax depending on V (closed form)
def year1_opex_ex_tax(rent, vacancy=VACANCY, ins=INSURANCE):
    gpr = 12*rent; egi = gpr*(1-vacancy)
    return {"gpr": gpr, "vacancy": gpr*vacancy, "egi": egi, "mgmt": MGMT_PCT*egi + LEASING_FEE, "maint": MAINT_PCT*gpr,
            "capex": CAPEX_PCT*gpr, "insurance": ins, "utilities": UTIL_OWNER}
def noi_at_price(price, rent, vacancy=VACANCY, ins=INSURANCE):
    o = year1_opex_ex_tax(rent, vacancy, ins); tax = tax_nonhomestead(price)
    opex = o["mgmt"]+o["maint"]+o["capex"]+o["insurance"]+o["utilities"]+tax
    return o["egi"] - opex, {**o, "tax": tax, "opex_total": opex}
TAX_RATE_ON_VALUE = ASSESS_RATIO*MILLS_2026/1000      # 0.0158208
def income_value(rent, cap, vacancy=VACANCY):
    o = year1_opex_ex_tax(rent, vacancy)
    noi_ex_tax = o["egi"] - (o["mgmt"]+o["maint"]+o["capex"]+o["insurance"]+o["utilities"]) - STREETLIGHT
    return noi_ex_tax/(cap + TAX_RATE_ON_VALUE)
CAP_RATES = {"low_cap_institutional_gordon": inp("cap_rate_low", 0.055, "valuation_methods.md KQ4 (INVH 5.1% stabilised acquisition cap Q2 2026; Gordon cross-check 5.4-5.9% at $200K)", "2026-07-29"),
             "mid_cap": inp("cap_rate_mid", 0.065, "model midpoint between the institutional 5.5% and Arbor's 7.4%", "2026"),
             "high_cap_arbor_national_sfr": inp("cap_rate_high", 0.074, "valuation_methods.md KQ4 (Arbor SFR cap rate 7.4%, Q1 2026, +210 bps since 2021)", "2026-06-12")}
inc = {}
for rent_label, rent in [("rent_low", RENT_LOW), ("rent_base", RENT_BASE), ("rent_high", RENT_HIGH), ("section8_contract", S8_CONTRACT)]:
    inc[rent_label] = {k: round(income_value(rent, c)) for k, c in CAP_RATES.items()}
noi_list, det_list = noi_at_price(LIST_PRICE, RENT_BASE)
A["income_approach"] = {"values": inc, "cap_rates": {k: I[f"cap_rate_{'low' if 'low' in k else ('high' if 'high' in k else 'mid')}"]["value"] for k in CAP_RATES},
    "noi_year1_at_list_price": round(noi_list), "cap_rate_at_list_price": noi_list/LIST_PRICE, "opex_detail_at_list": {k: round(v) for k,v in det_list.items()},
    "opex_ratio_at_list": det_list["opex_total"]/det_list["gpr"], "grm_at_list": LIST_PRICE/(12*RENT_BASE), "rent_to_price_monthly": RENT_BASE/LIST_PRICE,
    "range_low_mid_high": [inc["rent_base"]["high_cap_arbor_national_sfr"], inc["rent_base"]["mid_cap"], inc["rent_base"]["low_cap_institutional_gordon"]],
    "formula": "V = (EGI - opex_ex_tax - $35) / (cap + 0.40 x 39.552/1000); EGI = 12 x rent x (1 - 8%); opex = 9% mgmt of EGI + $510 leasing + 7.5% maint + 10% capex + $1,500 insurance + $210 utilities + tax(V)"}

# A3. AVMs with error bands
avm_out = {}
for k, v in AVM.items():
    val = v["value"]
    band_med = REDFIN_ERR_ONMKT_CLAYTON   # Zestimate table not retrievable (valuation_methods KQ1 gap) -> Redfin Clayton on-market band used as proxy for all
    avm_out[k] = {**v, "vs_list_pct": val/LIST_PRICE - 1, "median_error_band": [round(val*(1-band_med)), round(val*(1+band_med))],
                  "band_within_5pct_77pct_coverage": [round(val*0.95), round(val*1.05)], "band_within_10pct_90pct_coverage": [round(val*0.90), round(val*1.10)],
                  "band_source": "valuation_methods.md KQ1: Redfin on-market Clayton County median error 1.94% (76.7% within 5%, 89.5% within 10%); Zestimate accuracy table could not be retrieved, so the Redfin band is applied to all AVMs as a proxy"}
avm_vals = np.array([v["value"] for v in AVM.values()])
avm_core = np.array([AVM["Zestimate"]["value"], AVM["Redfin Estimate"]["value"]])   # the two with published accuracy
A["avms"] = {"estimates": avm_out, "mean_all_four": float(avm_vals.mean()), "mean_zillow_redfin": float(avm_core.mean()),
             "range_low_mid_high": [float(avm_core.min()*(1-0.05)), float(avm_core.mean()), float(avm_vals.max()*(1+0.0194))],
             "off_market_caution": "for a resale years out the relevant band is the off-market 7.57% median error (38% within 5%)"}

# A4. Reconciliation
W_SC, W_AVM, W_INC = 0.50, 0.30, 0.20
sc_lmh  = A["sales_comparison"]["range_low_mid_high"]
avm_lmh = A["avms"]["range_low_mid_high"]
inc_lmh = A["income_approach"]["range_low_mid_high"]
rec = [W_SC*sc_lmh[i] + W_AVM*avm_lmh[i] + W_INC*inc_lmh[i] for i in range(3)]
rec = [round(x, -3) for x in rec]
A["reconciled"] = {"weights": {"sales_comparison": W_SC, "avm": W_AVM, "income": W_INC}, "low_mid_high": rec,
    "inputs": {"sales_comparison": [round(x) for x in sc_lmh], "avm": [round(x) for x in avm_lmh], "income": [round(x) for x in inc_lmh]},
    "vs_list_pct": [x/LIST_PRICE - 1 for x in rec], "county_notice_2026": NOTICE_2026,
    "investor_value_range": INVESTOR_ASIS, "investor_value_model": [round(float(inv_ind.min())), round(float(np.median(inv_ind)))],
    "arv_low_mid_high": [ARV_LOW, ARV_MID, ARV_HIGH], "arv_model_mean": round(float(arv_ind.mean()))}
V0 = rec[1]                          # reconciled mid market value, as-is, Oct 2026

# ----------------------------------------------------------------------------------------------
# B. APPRECIATION
# ----------------------------------------------------------------------------------------------
B = {}
# B1. FHFA repeat-sales statistics (computed from the index values in market_history KQ1)
yrs = sorted(FHFA_CLAYTON); idx = np.array([FHFA_CLAYTON[y] for y in yrs])
rets = idx[1:]/idx[:-1] - 1
peak_i = int(np.argmax(idx[:13])); trough_i = int(np.argmin(idx))
fh = {"cagr_2000_2025": cagr(FHFA_CLAYTON[2000], FHFA_CLAYTON[2025], 25), "cagr_2000_2024": cagr(100, FHFA_CLAYTON[2024], 24),
      "mean_annual_return_2001_2025": float(rets.mean()), "sd_annual_return_2001_2025": float(rets.std(ddof=1)),
      "drawdown_2005_2012": FHFA_CLAYTON[2012]/FHFA_CLAYTON[2005] - 1, "peak_year": yrs[peak_i], "trough_year": yrs[trough_i],
      "recovery_year": next(y for y in yrs if y > 2012 and FHFA_CLAYTON[y] >= FHFA_CLAYTON[2005]),
      "all_time_high": (2024, FHFA_CLAYTON[2024]), "2025_vs_2024": FHFA_CLAYTON[2025]/FHFA_CLAYTON[2024]-1,
      "worst_3yr": float(min(idx[i+3]/idx[i]-1 for i in range(len(idx)-3))), "worst_5yr": float(min(idx[i+5]/idx[i]-1 for i in range(len(idx)-5))),
      "share_negative_5yr_windows": float(np.mean([idx[i+5]/idx[i] < 1 for i in range(len(idx)-5)])),
      "annual_changes": {yrs[i+1]: float(rets[i]) for i in range(len(rets))},
      "real_cagr_2000_2025_at_cpi": (1+cagr(100, FHFA_CLAYTON[2025], 25))/(1+CPI) - 1}
zy = sorted(FHFA_ZIP); zi = np.array([FHFA_ZIP[y] for y in zy])
fz = {"cagr_2000_2025": cagr(100, FHFA_ZIP[2025], 25), "drawdown_2006_2012": FHFA_ZIP[2012]/FHFA_ZIP[2006]-1,
      "2025_change": FHFA_ZIP[2025]/FHFA_ZIP[2024]-1, "sd_annual_2006_2025": float(np.std(zi[1:][1:]/zi[1:][:-1]-1, ddof=1))}
msa = {"cagr_2000_2026_q2": cagr(FHFA_MSA_Q2[2000], FHFA_MSA_Q2[2026], 26), "drawdown_2007_2012": FHFA_MSA_Q2[2012]/FHFA_MSA_Q2[2007]-1}
zh = {"cagr_dec2000_dec2025": cagr(ZHVI_ZIP_DEC[2000], ZHVI_ZIP_DEC[2025], 25), "drawdown_from_peak_sep2026": ZHVI_ZIP_NOW/ZHVI_ZIP_PEAK-1,
      "cagr_dec2000_sep2026": (ZHVI_ZIP_NOW/ZHVI_ZIP_DEC[2000])**(1/25.75)-1}
B["index_stats"] = {"fhfa_clayton": fh, "fhfa_zip30238": fz, "fhfa_atlanta_msa": msa, "zillow_zip30238": zh,
                    "beta_zip_to_metro": {"fhfa_2001_2025_county": 1.33, "fhfa_2001_2025_zip": 1.48, "zillow_2001_2026_zip": 1.82, "zillow_2013_2026_zip": 1.55, "src": "verification.md 5b"}}

# B1b. Repeat-sales trend projection: V_T = V_0 x (1+g)^T, g = FHFA county CAGR 2000-2025; band = +/-1 sd x sqrt(T) (lognormal)
g_rs = fh["cagr_2000_2025"]; sd_rs = fh["sd_annual_return_2001_2025"]
trend = {}
for T in HORIZONS:
    mu_T = T*math.log(1+g_rs); s_T = sd_rs*math.sqrt(T)
    trend[T] = {"central": V0*math.exp(mu_T), "p16": V0*math.exp(mu_T - s_T), "p84": V0*math.exp(mu_T + s_T),
                "real_central": V0*math.exp(mu_T)/(1+CPI)**T,
                "alt_zip_fhfa_3.25": V0*(1.0325)**T, "alt_zillow_zip_2.86": V0*(1.0286)**T, "alt_1975_2025_3.42": V0*(1.0342)**T}
B["repeat_sales_trend"] = {"drift_used": g_rs, "sd_used": sd_rs, "V0": V0, "by_horizon": trend,
                           "formula": "V_T = V_0 x (1+g)^T with g = FHFA Clayton County 2000-2025 CAGR; +/-1 sd band uses sd of annual returns x sqrt(T) in logs (no autocorrelation)"}

# B2. Momentum + mean reversion. Fundamentals anchored to rent and income.
rent_gap = math.log(GROSS_YIELD_NOW/GROSS_YIELD_MEAN)     # +: price below rent-based fundamental
pi_years = [y for y in INCOME_SAIPE if y >= 2019 and y in ZHVI_ZIP_DEC]
pti_hist = {y: ZHVI_ZIP_DEC[y]/INCOME_SAIPE[y] for y in pi_years}
income_2026 = INCOME_SAIPE[2024]*(1+INCOME_GROWTH)**2
pti_now = ZHVI_ZIP_NOW/income_2026
pti_mean_1924 = float(np.mean(list(pti_hist.values())))
income_gap_a = math.log(pti_mean_1924/pti_now)          # vs 2019-2024 mean (includes pandemic boom)
income_gap_b = math.log(pti_hist[2019]/pti_now)         # vs 2019 pre-pandemic anchor
income_gap = 0.5*(income_gap_a + income_gap_b)
fund_gap = 0.5*rent_gap + 0.5*income_gap
FUND_GROWTH = RENT_GROWTH   # fundamental grows with rents (Gordon); 2.5%/yr nominal

def mm_path(alpha, beta, gamma, T=10, dp0=ZIP_12MO_LOG, gap0=fund_gap, g_star=FUND_GROWTH):
    """Capozza et al: dp_t = alpha*dp_{t-1} + beta*(p*_{t-1} - p_{t-1}) + gamma*dp*_t. Returns list of annual log changes."""
    out, dp, gap = [], dp0, gap0
    for t in range(T):
        dpt = alpha*dp + beta*gap + gamma*g_star
        gap = gap + g_star - dpt
        out.append(dpt); dp = dpt
    return out
paths_mm = {
    "capozza_panel_a0.33_b0.25_g0.52": mm_path(*CAPOZZA_PANEL),
    "capozza_repeat_sales_a0.55_b0.15_g0.52": mm_path(*CAPOZZA_RS),
    "local_ar1_0.644_gallin_0.169": mm_path(LOCAL_AR1, GALLIN_BETA, 1-LOCAL_AR1),
}
mm_mean = np.mean(np.array(list(paths_mm.values())), axis=0)
def cum_values(logchanges, v0=V0):
    c = np.cumsum(logchanges); return {T: float(v0*math.exp(c[T-1])) for T in HORIZONS}
B["momentum_mean_reversion"] = {
    "inputs": {"last_12mo_zip_log_change": ZIP_12MO_LOG, "rent_gap_log": rent_gap, "price_to_income_now": pti_now, "price_to_income_hist": pti_hist,
               "pti_mean_2019_2024": pti_mean_1924, "income_gap_vs_2019_2024_mean": income_gap_a, "income_gap_vs_2019_anchor": income_gap_b,
               "income_gap_blended": income_gap, "fundamental_gap_blended": fund_gap, "fundamental_growth": FUND_GROWTH,
               "rent_based_fundamental_value_zip": ZHVI_ZIP_NOW*math.exp(rent_gap), "income_2026_est": income_2026},
    "annual_log_changes": {k: [float(x) for x in v] for k, v in paths_mm.items()}, "mean_path_log_changes": [float(x) for x in mm_mean],
    "values_by_horizon": {k: cum_values(v) for k, v in paths_mm.items()}, "mean_values_by_horizon": cum_values(mm_mean),
    "year1_vs_zillow_zhvf": {"model_mean_year1": float(mm_mean[0]), "zillow_zip_12mo": -0.005},
    "steady_state_note": "Capozza form converges to price growth = fundamental growth (2.5%) with a steady gap of g*(1-alpha-gamma)/beta",
}

# B3. Monte Carlo (metro AR(1) -> ZIP via beta -> property noise; crash regime replays FHFA Clayton 2006-2015)
CRASH_PATH = np.log(np.array([FHFA_CLAYTON[y]/FHFA_CLAYTON[y-1] for y in range(2006, 2016)]))   # 10 annual log changes, 2006..2015
def monte_carlo(n=N_PATHS, T=10, beta=BETA_ZIP_BASE, hazard=CRASH_HAZARD, sd_prop=SD_PROPERTY, seed=20261019, v0=V0, drift=None):
    """ZIP log return = base drift path (momentum + mean reversion, section B2) + beta x metro AR(1) shock + ZIP idiosyncratic shock;
    property log return = ZIP return + property idiosyncratic shock; with probability `hazard` per year a crash regime starts that
    replaces the next 10 ZIP returns with the FHFA Clayton 2006-2015 replay. Metro shocks are zero-mean AR(1) with unconditional sd SD_METRO."""
    rng = np.random.default_rng(seed)
    drift = mm_mean if drift is None else drift
    sig_eps = SD_METRO*math.sqrt(1-PHI_METRO**2)
    u_m_prev = np.zeros(n)
    logv = np.zeros((n, T+1)); crash_start = np.full(n, -1)
    for t in range(1, T+1):
        u_m = PHI_METRO*u_m_prev + rng.normal(0, sig_eps, n)            # metro shock (deviation from its expected path)
        r_z = drift[t-1] + beta*u_m + rng.normal(0, SD_ZIP_IDIO, n)
        new = (crash_start < 0) & (rng.random(n) < hazard)
        crash_start = np.where(new, t, crash_start)
        in_crash = (crash_start > 0) & (t - crash_start < len(CRASH_PATH))
        k = np.clip(t - crash_start, 0, len(CRASH_PATH)-1)
        r_z = np.where(in_crash, CRASH_PATH[k] + rng.normal(0, 0.02, n), r_z)
        r_p = r_z + rng.normal(0, sd_prop, n)
        logv[:, t] = logv[:, t-1] + r_p
        u_m_prev = np.where(in_crash, np.minimum(u_m, 0.0), u_m)
    vals = v0*np.exp(logv)
    pct = {T_: {f"p{p}": float(np.percentile(vals[:, T_], p)) for p in [5,25,50,75,95]} for T_ in HORIZONS}
    pct_real = {T_: {f"p{p}": float(np.percentile(vals[:, T_], p)/(1+CPI)**T_) for p in [5,25,50,75,95]} for T_ in HORIZONS}
    running_max = np.maximum.accumulate(vals, axis=1); mdd = (vals/running_max - 1).min(axis=1)
    stats = {"share_negative_5yr": float(np.mean(vals[:,5] < v0)), "share_negative_10yr": float(np.mean(vals[:,10] < v0)),
             "share_max_drawdown_ge_40pct": float(np.mean(mdd <= -0.40)), "share_max_drawdown_ge_25pct": float(np.mean(mdd <= -0.25)),
             "share_paths_with_crash_regime": float(np.mean(crash_start > 0)), "mean_annual_log_return_10yr": float(np.mean(logv[:,10])/10),
             "p5_1yr_change": float(np.percentile(vals[:,1]/v0-1, 5)), "p95_1yr_change": float(np.percentile(vals[:,1]/v0-1, 95))}
    return vals, pct, pct_real, stats
mc_vals, mc_pct, mc_pct_real, mc_stats = monte_carlo()
_, mc_pct_nocrash, _, mc_stats_nocrash = monte_carlo(hazard=0.0, seed=7)
_, mc_pct_stress, _, mc_stats_stress = monte_carlo(beta=BETA_ZIP_STRESS, seed=11)
B["monte_carlo"] = {"n_paths": N_PATHS, "params": {"drift": "momentum + mean-reversion mean path (B2)", "sd_metro": SD_METRO, "phi_metro": PHI_METRO, "beta": BETA_ZIP_BASE,
                    "sd_zip_idio": SD_ZIP_IDIO, "sd_property": SD_PROPERTY, "crash_hazard": CRASH_HAZARD, "crash_path_cum_7yr": float(math.exp(CRASH_PATH[:7].sum())-1), "crash_path_cum_10yr": float(math.exp(CRASH_PATH.sum())-1), "V0": V0,
                    "implied_annual_sd_zip": math.sqrt((BETA_ZIP_BASE*SD_METRO)**2 + SD_ZIP_IDIO**2), "implied_annual_sd_property": math.sqrt((BETA_ZIP_BASE*SD_METRO)**2 + SD_ZIP_IDIO**2 + SD_PROPERTY**2)},
                    "percentiles_nominal": mc_pct, "percentiles_real": mc_pct_real, "stats": mc_stats,
                    "no_crash_regime": {"percentiles": mc_pct_nocrash, "stats": mc_stats_nocrash},
                    "stress_beta_1.8": {"percentiles": mc_pct_stress, "stats": mc_stats_stress},
                    "historical_check": {"zip_share_negative_5yr_windows_zillow": 0.27, "fhfa_zip_share_negative_5yr": 0.20, "zillow_1yr_p5": -0.234, "zillow_1yr_p95": 0.263, "src": "valuation_methods.md KQ3"}}

# B4. Named scenarios (annual index multipliers, 10 years)
bear_log = CRASH_PATH.copy()                                   # 2008 replay: FHFA Clayton 2006-2015
base_log = mm_mean.copy()                                      # momentum + mean reversion mean path
bull_log = np.log(1+np.array([0.02,0.08,0.08,0.06,0.05,0.04,0.04,0.035,0.035,0.035]))   # rate relief (Zillow 6.5% end-2027) + 2013-15-type rebound scaled to the current 13% drawdown
mod_bear_log = np.diff(np.log(np.array([V0] + [np.percentile(mc_vals[:, t], 10) for t in range(1, 11)])))
SCEN = {"bear_2008_replay": bear_log, "bear_moderate_mc_p10": mod_bear_log, "base": base_log, "bull": bull_log}
def scen_table(logs, v0=V0):
    c = np.cumsum(logs); out = {}
    for T in HORIZONS:
        v = v0*math.exp(c[T-1]); out[T] = {"value": v, "real_value": v/(1+CPI)**T, "cum_change": v/v0-1}
    return out
B["scenarios"] = {k: {"annual_log_changes": [float(x) for x in v], "table": scen_table(v)} for k, v in SCEN.items()}
B["scenario_definitions"] = {
    "bear_2008_replay": "FHFA Clayton County actual annual changes 2006-2015 applied from year 1 (-48.5% trough at year 7, -33% at year 10) - market_history KQ1",
    "bear_moderate_mc_p10": "10th percentile of the Monte Carlo value distribution at each horizon (with crash regime)",
    "base": "mean of three momentum + mean-reversion parameterisations (Capozza panel, Capozza repeat-sales, local AR(1)+Gallin) - valuation_methods KQ2",
    "bull": "year 1 +2%, years 2-3 +8%, year 4 +6%, year 5 +5%, years 6-7 +4%, years 8-10 +3.5%: rates easing to Zillow's 6.5% end-2027 path and a 2013-2015-type rebound (ZIP +14-28%/yr then) scaled to today's 13% drawdown - valuation_methods KQ3/KQ6",
}
B["published_forecasts"] = FORECASTS

# ----------------------------------------------------------------------------------------------
# C. CASH FLOW
# ----------------------------------------------------------------------------------------------
def proforma(price, rent=RENT_BASE, ltv=LTV_BASE, rate=RATE_PMMS, points=LLPA_PTS, vacancy=VACANCY, rent_growth=RENT_GROWTH,
             make_ready=MAKE_READY, contingency=SYS_CONTING, years=10, value_logs=None, exit_value_basis=None, exit_cap=None,
             evictions=None, extra_opex_pa=0.0, concession_pct=0.0, section8=False):
    """Annual pro forma for `years`; returns dict with year-1 metrics, annual CF list, IRR for 5 and 10 yr holds."""
    loan = ltv*price; p_m = pmt(loan, rate); ds = 12*p_m
    cash_in = (1-ltv)*price + CLOSING_PCT*price + points*loan + make_ready + contingency - concession_pct*price
    rows, cfs = [], []
    for t in range(1, years+1):
        r = rent*(1+rent_growth)**(t-1); gpr = 12*r; vac = vacancy*gpr; egi = gpr - vac
        mgmt = MGMT_PCT*egi + LEASING_FEE*(1+OPEX_GROWTH)**(t-1)
        maint = MAINT_PCT*gpr; capex = CAPEX_PCT*gpr
        tax = tax_nonhomestead(min(price, NOTICE_2026) if t == 1 else price)*(1+TAX_GROWTH)**(t-1)
        ins = INSURANCE*(1+INS_GROWTH)**(t-1); util = UTIL_OWNER*(1+OPEX_GROWTH)**(t-1)
        s8 = 300 if section8 else 0
        ev = EVICTION_COST if (evictions and t in evictions) else 0
        opex = mgmt+maint+capex+tax+ins+util+s8+extra_opex_pa*(1+OPEX_GROWTH)**(t-1)
        noi = egi - opex; cf = noi - ds - ev
        rows.append({"year": t, "rent_mo": r, "gpr": gpr, "vacancy": vac, "egi": egi, "mgmt": mgmt, "maint": maint, "capex": capex, "tax": tax, "insurance": ins, "utilities": util, "eviction": ev, "opex": opex, "noi": noi, "debt_service": ds, "cash_flow": cf})
        cfs.append(cf)
    v_basis = exit_value_basis if exit_value_basis is not None else V0 + 0.75*make_ready
    def exit_value(N):
        if exit_cap is not None:
            noi_next = rows[N-1]["noi"]*(1+rent_growth) if N == years else rows[N]["noi"]
            return noi_next/exit_cap
        c = np.cumsum(value_logs)[N-1]; return v_basis*math.exp(c)
    def hold(N):
        v = exit_value(N); bal = loan_balance(loan, rate, 12*N); net = v*(1-SELL_COST) - bal
        flows = [-cash_in] + cfs[:N-1] + [cfs[N-1] + net]
        return {"exit_value": v, "loan_balance": bal, "net_sale_proceeds": net, "irr": irr(flows), "equity_multiple": (sum(cfs[:N]) + net)/cash_in, "total_profit": sum(cfs[:N]) + net - cash_in}
    y1 = rows[0]
    out = {"price": price, "loan": loan, "rate": rate, "ltv": ltv, "pi_monthly": p_m, "cash_invested": cash_in,
           "year1": {k: (v/12 if k in ("gpr","vacancy","egi","mgmt","maint","capex","tax","insurance","utilities","opex","noi","debt_service","cash_flow") else v) for k, v in y1.items()},
           "year1_annual": y1, "cap_rate": y1["noi"]/price, "cash_on_cash": y1["cash_flow"]/cash_in,
           "dscr_lender_gross_rent_over_pitia": 12*rent/(ds + y1["tax"] + y1["insurance"]), "dscr_noi_over_debt_service": y1["noi"]/ds,
           "grm": price/(12*rent), "opex_ratio": y1["opex"]/y1["gpr"], "rows": rows}
    if value_logs is not None or exit_cap is not None:
        out["hold5"] = hold(5); out["hold10"] = hold(10)
    return out

SCEN_OPS = {  # operating assumptions by scenario (rent growth, vacancy, evictions, contingency)
    "bear_2008_replay": {"rent_growth": 0.0, "vacancy": 0.10, "evictions": [2,7], "contingency": SYS_CONTING_BAD},
    "bear_moderate_mc_p10": {"rent_growth": 0.01, "vacancy": 0.10, "evictions": [3], "contingency": SYS_CONTING_BAD},
    "base": {"rent_growth": RENT_GROWTH, "vacancy": VACANCY, "evictions": None, "contingency": SYS_CONTING},
    "bull": {"rent_growth": 0.035, "vacancy": 0.06, "evictions": None, "contingency": SYS_CONTING},
}
def scenario_set(price, **kw):
    return {s: proforma(price, value_logs=SCEN[s], rent_growth=o["rent_growth"], vacancy=o["vacancy"], evictions=o["evictions"], contingency=o["contingency"], **kw) for s, o in SCEN_OPS.items()}

C = {}
pf_list = proforma(LIST_PRICE, value_logs=SCEN["base"])
C["proforma_at_list_base"] = {k: v for k, v in pf_list.items() if k != "rows"}
C["proforma_at_list_base"]["rows_annual"] = [{k: round(v) if isinstance(v, float) else v for k, v in r.items()} for r in pf_list["rows"]]
C["proforma_at_list_dscr_loan_6.75"] = {k: v for k, v in proforma(LIST_PRICE, rate=RATE_DSCR, points=0.0, value_logs=SCEN["base"]).items() if k != "rows"}
C["proforma_at_list_80ltv_dscr_7.00"] = {k: v for k, v in proforma(LIST_PRICE, ltv=LTV_ALT, rate=0.07, points=0.0, value_logs=SCEN["base"]).items() if k != "rows"}
C["scenarios_at_list"] = {s: {"cash_invested": r["cash_invested"], "cap_rate": r["cap_rate"], "cash_on_cash": r["cash_on_cash"], "hold5": r["hold5"], "hold10": r["hold10"], "cum_cf_10": sum(x["cash_flow"] for x in r["rows"])} for s, r in scenario_set(LIST_PRICE).items()}
# Section 8 variant at list
s8 = proforma(LIST_PRICE, rent=S8_CONTRACT, vacancy=0.04, value_logs=SCEN["base"], section8=True)
C["section8_at_list"] = {k: v for k, v in s8.items() if k != "rows"}
C["section8_notes"] = "contract rent $2,100 (rent reasonableness, gapfill_4 KQ2); vacancy 4% (HAP share paid reliably; 2-4 week lease-up); +$300/yr inspection/admin; payment standard range $2,088-$2,552 (JHA schedule unpublished); SAFMR fell 4.1% FY2027 so no voucher-side rent growth"
# Flip variant
def flip(price, arv=ARV_MID, reno=RENO_FLIP, contingency=SYS_CONTING, months=6, hard_money=False):
    buy_close = 0.02*price
    holding = months*(tax_nonhomestead(price)/12 + INSURANCE/12 + 150)
    fin = (0.11*months/12*0.9*(price+reno)) if hard_money else (RATE_PMMS*months/12*(price+reno))   # hard money 11% not sourced; opportunity cost at PMMS otherwise
    sell = 0.10*arv   # 7% commission+closing + 3% concessions (gapfill_5: $6.5K-$10K concessions on 4 of 5 sales)
    cost = price + buy_close + reno + contingency + holding + fin
    profit = arv - sell - cost
    return {"price": price, "arv": arv, "renovation": reno, "contingency": contingency, "buy_closing": buy_close, "holding_6mo": holding, "financing_or_opportunity_cost": fin, "selling_costs_10pct": sell, "all_in_cost": cost, "profit": profit, "roi_on_cost": profit/cost, "mao_70_rule": 0.70*arv - reno, "mao_75_rule": 0.75*arv - reno}
C["flip"] = {"at_list_arv_mid": flip(LIST_PRICE), "at_list_arv_low": flip(LIST_PRICE, arv=ARV_LOW), "at_172500": flip(172500), "at_158000": flip(158000), "at_158000_arv_low": flip(158000, arv=ARV_LOW),
             "benchmarks": {"attom_q2_2026_us_gross_roi": 0.215, "attom_q2_2026_georgia_gross_roi": 0.253, "src": "value_add KQ5 / comparable_sales KQ4"}}
# levered IRR distribution across Monte Carlo paths (10-yr hold, base operations)
def mc_irr_dist(price, make_ready=MAKE_READY, contingency=SYS_CONTING):
    pf = proforma(price, make_ready=make_ready, contingency=contingency)
    loan = pf["loan"]; cfs = [r["cash_flow"] for r in pf["rows"]]
    v10 = mc_vals[:, 10]/V0*(V0 + 0.75*make_ready)
    net = v10*(1-SELL_COST) - loan_balance(loan, RATE_PMMS, 120)
    cfm = np.tile(np.array([-pf["cash_invested"]] + cfs), (len(v10), 1)); cfm[:, -1] += net
    r = irr_vec(cfm)
    return {"p5": float(np.percentile(r,5)), "p25": float(np.percentile(r,25)), "p50": float(np.percentile(r,50)), "p75": float(np.percentile(r,75)), "p95": float(np.percentile(r,95)),
            "share_irr_below_0": float(np.mean(r < 0)), "share_irr_above_12": float(np.mean(r >= 0.12)), "share_equity_wiped_out": float(np.mean((np.sum(cfs) + net) <= 0))}
C["mc_levered_irr_10yr_at_list"] = mc_irr_dist(LIST_PRICE)

# ----------------------------------------------------------------------------------------------
# D. PRICE TO BUY
# ----------------------------------------------------------------------------------------------
def solve_max_price(fn, target, lo=40000, hi=320000):
    """largest price P with fn(P) >= target (fn decreasing in P)."""
    if fn(hi) >= target: return hi
    if fn(lo) < target: return float('nan')
    for _ in range(60):
        mid = (lo+hi)/2
        if fn(mid) >= target: lo = mid
        else: hi = mid
    return (lo+hi)/2

def hurdles(rent=RENT_BASE, rate=RATE_PMMS, points=LLPA_PTS, ltv=LTV_BASE, exit_cap=None, contingency=SYS_CONTING, make_ready=MAKE_READY):
    kw = dict(rent=rent, rate=rate, points=points, ltv=ltv, make_ready=make_ready)
    cap_fn = lambda P: proforma(P, contingency=contingency, **kw)["cap_rate"]
    coc_fn = lambda P: proforma(P, contingency=contingency, **kw)["cash_on_cash"]
    irr_fn = lambda P: proforma(P, value_logs=SCEN["base"], exit_cap=exit_cap, contingency=contingency, **kw)["hold10"]["irr"]
    def bear_fn_for(key):
        o = SCEN_OPS[key]
        return lambda P: proforma(P, value_logs=SCEN[key], rent_growth=o["rent_growth"], vacancy=o["vacancy"], evictions=o["evictions"],
                                  contingency=(o["contingency"] if contingency > 0 else 0), exit_cap=exit_cap, **kw)["hold10"]["equity_multiple"]
    noi_cov_fn = lambda P: proforma(P, contingency=contingency, **kw)["dscr_noi_over_debt_service"]
    res = {"cap_ge_7.4_arbor": solve_max_price(cap_fn, 0.074), "cap_ge_6.5_mid": solve_max_price(cap_fn, 0.065),
           "coc_ge_6pct": solve_max_price(coc_fn, 0.06), "coc_ge_8pct": solve_max_price(coc_fn, 0.08),
           "irr10_base_ge_12pct": solve_max_price(irr_fn, 0.12), "irr10_base_ge_10pct": solve_max_price(irr_fn, 0.10),
           "bear_2008_replay_equity_multiple_ge_1": solve_max_price(bear_fn_for("bear_2008_replay"), 1.0),
           "bear_mc_p10_equity_multiple_ge_1": solve_max_price(bear_fn_for("bear_moderate_mc_p10"), 1.0),
           "noi_coverage_ge_1.0": solve_max_price(noi_cov_fn, 1.0), "noi_coverage_ge_1.2": solve_max_price(noi_cov_fn, 1.2),
           "cash_flow_breakeven": solve_max_price(lambda P: proforma(P, contingency=contingency, **kw)["year1_annual"]["cash_flow"], 0.0)}
    cluster = ["cap_ge_7.4_arbor", "irr10_base_ge_12pct", "noi_coverage_ge_1.2"]          # the three return hurdles that converge
    res["binding_return_hurdles"] = min(res[k] for k in cluster); res["binding_return_hurdle"] = min(cluster, key=lambda k: res[k])
    allh = cluster + ["coc_ge_6pct", "bear_2008_replay_equity_multiple_ge_1"]
    res["binding_all_hurdles"] = min(res[k] for k in allh); res["binding_all_hurdle"] = min(allh, key=lambda k: res[k])
    return res
D = {}
D["hurdles_base"] = hurdles()
D["hurdles_clean_inspection_no_contingency"] = hurdles(contingency=0)
D["hurdles_dscr_loan_6.75"] = hurdles(rate=RATE_DSCR, points=0.0)
D["hurdles_80ltv_dscr_7.00"] = hurdles(rate=0.07, points=0.0, ltv=LTV_ALT)
D["sensitivity"] = {
    "rent_minus_10": hurdles(rent=RENT_BASE*0.9), "rent_plus_10": hurdles(rent=RENT_BASE*1.1),
    "rate_minus_1pt": hurdles(rate=RATE_PMMS-0.01), "rate_plus_1pt": hurdles(rate=RATE_PMMS+0.01),
    "exit_cap": {str(c): hurdles(exit_cap=c) for c in [0.06, 0.065, 0.07, 0.075, 0.08]},
}
# recommended prices
MAX_PRICE = round(D["hurdles_base"]["binding_return_hurdles"], -3)            # walk-away with $10K systems contingency carried
MAX_PRICE_CLEAN = round(D["hurdles_clean_inspection_no_contingency"]["binding_return_hurdles"], -3)
ALL_HURDLE_PRICE = round(D["hurdles_base"]["binding_all_hurdles"], -3)
OPEN_OFFER = inp("opening_offer", 145000, "model: ~3% below the walk-away price to leave room for the 3% concession ask; sits inside the investor-tier comp indications ($143K-$182K, gapfill_5 county deeds) and below the 70%-rule MAO", "2026-10-19")
D["recommendation"] = {"walk_away_max_price": MAX_PRICE, "binding_hurdle": D["hurdles_base"]["binding_return_hurdle"],
    "walk_away_if_clean_inspection": MAX_PRICE_CLEAN, "all_hurdles_price_incl_coc6_and_2008_survival": ALL_HURDLE_PRICE, "all_hurdles_binding": D["hurdles_base"]["binding_all_hurdle"],
    "opening_offer": OPEN_OFFER, "opening_offer_vs_list": OPEN_OFFER/LIST_PRICE-1, "walk_away_vs_list": MAX_PRICE/LIST_PRICE-1, "concessions_ask_pct": 0.03,
    "formula_band": {"70_rule_arv290": 0.70*ARV_MID-45000, "75_rule_arv290": 0.75*ARV_MID-45000, "70_rule_arv280": 0.70*ARV_LOW-45000}, "day_one_realistic_band_notes": [185000, 190000],
    "context": {"dom_as_of_2026_10_18": 5, "price_drops": 0, "zip_price_drop_share": 0.358, "zip_sale_to_list": 0.985, "zip_median_dom": 61, "pending_ratio": 0.346, "deep_discount_dom_months": "5-7 (gapfill_5)", "estate_sale": True, "listed_2026_10_13": True}}
def ladder_row(P):
    pf = proforma(P, value_logs=SCEN["base"]); sc = scenario_set(P)
    return {"price": P, "vs_list": P/LIST_PRICE-1, "cash_invested": pf["cash_invested"], "cf_month": pf["year1_annual"]["cash_flow"]/12, "cap_rate": pf["cap_rate"], "cash_on_cash": pf["cash_on_cash"],
            "dscr_lender": pf["dscr_lender_gross_rent_over_pitia"], "noi_coverage": pf["dscr_noi_over_debt_service"], "irr5_base": pf["hold5"]["irr"], "irr10_base": pf["hold10"]["irr"], "em10_base": pf["hold10"]["equity_multiple"],
            "irr10_bull": sc["bull"]["hold10"]["irr"], "em10_bear_2008": sc["bear_2008_replay"]["hold10"]["equity_multiple"], "em10_bear_p10": sc["bear_moderate_mc_p10"]["hold10"]["equity_multiple"],
            "flip_profit_arv290": flip(P)["profit"], "flip_profit_arv280": flip(P, arv=ARV_LOW)["profit"]}
D["price_ladder"] = [ladder_row(P) for P in [LIST_PRICE, 190000, 185000, 172500, 158000, MAX_PRICE_CLEAN, MAX_PRICE, OPEN_OFFER, ALL_HURDLE_PRICE]]
C["scenarios_at_max_price"] = {s: {"cash_invested": r["cash_invested"], "cap_rate": r["cap_rate"], "cash_on_cash": r["cash_on_cash"], "dscr_lender": r["dscr_lender_gross_rent_over_pitia"], "noi_coverage": r["dscr_noi_over_debt_service"], "hold5": r["hold5"], "hold10": r["hold10"], "cum_cf_10": sum(x["cash_flow"] for x in r["rows"])} for s, r in scenario_set(MAX_PRICE).items()}
C["scenarios_at_open_offer"] = {s: {"cash_invested": r["cash_invested"], "cap_rate": r["cap_rate"], "cash_on_cash": r["cash_on_cash"], "hold5": r["hold5"], "hold10": r["hold10"]} for s, r in scenario_set(OPEN_OFFER).items()}
C["proforma_at_max_price_base"] = {k: v for k, v in proforma(MAX_PRICE, value_logs=SCEN["base"]).items() if k != "rows"}
C["mc_levered_irr_10yr_at_max_price"] = mc_irr_dist(MAX_PRICE)
C["section8_at_max_price"] = {k: v for k, v in proforma(MAX_PRICE, rent=S8_CONTRACT, vacancy=0.04, value_logs=SCEN["base"], section8=True).items() if k != "rows"}
C["flip"]["at_max_price"] = flip(MAX_PRICE)
# dollar gain/loss tables from purchase at list and at recommended prices (gross value minus price; and net of 8% sale costs)
def gain_table(price):
    out = {}
    for s in ["bear_2008_replay", "bear_moderate_mc_p10", "base", "bull"]:
        tb = B["scenarios"][s]["table"]
        out[s] = {T: {"value": tb[T]["value"], "gain_gross": tb[T]["value"]-price, "gain_net_of_8pct_sale_costs": tb[T]["value"]*(1-SELL_COST)-price,
                      "real_value": tb[T]["real_value"], "real_gain_gross": tb[T]["real_value"]-price} for T in HORIZONS}
    return out
B["gain_tables"] = {"purchase_at_list": gain_table(LIST_PRICE), "purchase_at_max_price": gain_table(MAX_PRICE), "purchase_at_opening_offer": gain_table(OPEN_OFFER)}

# ----------------------------------------------------------------------------------------------
# E. VALUE-ADD RANKING
# ----------------------------------------------------------------------------------------------
# tier $/sf from value_add KQ2: as-is $96-99, refreshed $112-127, full reno $133-148 (Pheasant $133 anchors ARV). Lift ranges = (tier spread) x share of package.
TIER = {"asis_psf": [96, 99], "refreshed_psf": [112, 127], "renovated_psf": [133, 148], "src": "value_add_and_strategy.md KQ2 / gapfill_5 KQ1"}
asis_val = V0; refreshed_val = [SF*TIER["refreshed_psf"][0], SF*TIER["refreshed_psf"][1]]; reno_val = [ARV_LOW, ARV_HIGH]
refresh_lift = [max(0, refreshed_val[0]-asis_val), refreshed_val[1]-asis_val]; full_lift = [reno_val[0]-asis_val, reno_val[1]-asis_val]
ITEMS = [
 # name, cost_low, cost_high, value_lift_low, value_lift_high, rent_lift_mo_low, rent_lift_mo_high, flag, src
 ("Interior paint (~2,100 sf, incl. wallpaper removal)", 4500, 7500, 0.35*refresh_lift[0], 0.35*refresh_lift[1], 25, 50, "core refresh", "gapfill_3 KQ4 Tier A; value_add KQ2 tiers"),
 ("LVP in ~1,170 sf of carpeted rooms", 3500, 7000, 0.30*refresh_lift[0], 0.30*refresh_lift[1], 25, 50, "core refresh", "gapfill_3 KQ4 Tier A; value_add KQ2 tiers"),
 ("Curb appeal (pressure wash, front/garage doors, landscaping)", 2000, 6000, 0.10*refresh_lift[0], 0.10*refresh_lift[1], 0, 25, "core refresh", "value_add KQ3; NAR 2025 steel door 100% recovery"),
 ("Bath touch-ups x3 (regrout, vanity, lights, GFCI)", 1200, 2500, 0.10*refresh_lift[0], 0.10*refresh_lift[1], 0, 25, "core refresh", "gapfill_3 KQ4 Tier A"),
 ("Haul-out, deep clean, hardware, smoke/CO, blinds", 2000, 4000, 0.15*refresh_lift[0], 0.15*refresh_lift[1], 25, 50, "core refresh", "gapfill_3 KQ4 Tier A"),
 ("Kitchen refresh (reface/paint cabinets, counters, sink, appliances)", 10000, 20000, 0.45*(full_lift[0]-refresh_lift[0]), 0.45*(full_lift[1]-refresh_lift[1]), 50, 100, "retail flip tier", "gapfill_3 KQ4 Tier B; HomeAdvisor Southeast $12,000-$32,200"),
 ("Two original baths: new tile surrounds, floors, vanities", 7000, 16000, 0.35*(full_lift[0]-refresh_lift[0]), 0.35*(full_lift[1]-refresh_lift[1]), 25, 75, "retail flip tier", "gapfill_3 KQ4 Tier B"),
 ("Primary bath full refresh (7'10\" x 5'1\")", 3500, 6000, 0.10*(full_lift[0]-refresh_lift[0]), 0.10*(full_lift[1]-refresh_lift[1]), 0, 25, "retail flip tier", "gapfill_3 KQ4 Tier B"),
 ("Lighting package, interior doors/trim paint, mid-grade LVP upgrade", 3000, 6000, 0.10*(full_lift[0]-refresh_lift[0]), 0.10*(full_lift[1]-refresh_lift[1]), 0, 25, "retail flip tier", "gapfill_3 KQ4 Tier B"),
 ("Sewer camera scope + lateral repair if needed", 100, 5300, 0, 0, 0, 0, "risk mitigation (expected loss avoided ~$1,000-$2,000)", "value_add KQ3; gapfill_3 contingency"),
 ("HVAC replacement as heat pump (if end of life), net of $1,500 Georgia Power rebate", 3500, 11000, 2000, 6000, 0, 25, "defensive: value lift limited, lowers turnover/insurance risk", "value_add KQ3; Georgia Power HEIP"),
 ("Electric water heater (if >10 yrs)", 900, 1800, 500, 1500, 0, 0, "defensive", "gapfill_3 KQ4"),
 ("Attic insulation top-up + air/duct sealing (net of rebates)", 1200, 2500, 500, 2000, 0, 15, "defensive / utility allowance help for voucher tenant", "gapfill_3 KQ4; Georgia Power rebates"),
 ("After-the-fact permits / electrician letter for panel + addition", 500, 3000, 5000, 20000, 0, 0, "financeability: removes lender-overlay risk on 544 sf addition", "gapfill_2 KQ3 (lender overlays may assign unpermitted space zero value)"),
 ("Wood privacy fence replacing chain-link", 2100, 9400, 0, 2000, 0, 25, "amenity; low ROI", "value_add KQ3"),
 ("Paint the brick exterior", 3000, 9000, -5000, 2000, 0, 0, "NOT recommended (permanent, high-maintenance; comps' premiums came from interiors)", "value_add KQ3"),
 ("Detached garage -> rental apartment/ADU", 20000, 50000, 0, 0, 0, 0, "NOT PERMITTED: ADU conditional use only in AG/ER/RS-180 (subject RS-110); whole-house STR also barred", "gapfill_8 KQ4; value_add KQ3"),
 ("Primary suite / bath addition", 35000, 80000, 8000, 24000, 25, 50, "OVER-IMPROVEMENT: 22-30% cost recovery; all-in above ~$150/sf not recovered", "value_add KQ1 (HomeAdvisor), KQ2"),
 ("High-end kitchen (stone, custom cabinets)", 30000, 65000, 0.5*(full_lift[0]-refresh_lift[0]), 0.6*(full_lift[1]-refresh_lift[1]), 50, 100, "OVER-IMPROVEMENT vs the $10-20K refresh: same tier ceiling", "value_add KQ2 (ZIP p90 $200/sf; 1955-79 cohort p75 $148/sf)"),
]
E = {"tiers": TIER, "asis_value_used": asis_val, "refreshed_value_range": refreshed_val, "renovated_value_range": reno_val, "refresh_lift_range": refresh_lift, "full_reno_lift_range": full_lift, "items": []}
for (n, cl, ch, vl, vh, rl, rh, flag, src) in ITEMS:
    cm = (cl+ch)/2; vm = (vl+vh)/2; rm = (rl+rh)/2
    roi_v = (vm - cm)/cm; roi_rent = 12*rm/cm
    E["items"].append({"item": n, "cost_2026": [cl, ch], "cost_mid": cm, "value_lift": [round(vl), round(vh)], "value_lift_mid": round(vm), "rent_lift_mo": [rl, rh],
                       "roi_value_net_of_cost": roi_v, "annual_rent_yield_on_cost": roi_rent, "combined_score": roi_v + 5*roi_rent, "flag": flag, "src": src})
E["items"].sort(key=lambda x: x["combined_score"], reverse=True)
for i, it in enumerate(E["items"]): it["rank"] = i+1
E["packages"] = {"tier_a_rent_ready": {"cost": [12000, 24500], "central": [15000, 18000], "value_lift": refresh_lift, "rent": [RENT_LIGHT, RENT_BASE]},
                 "tier_ab_retail_flip": {"cost": [37500, 77500], "central": [45000, 55000], "value_lift": full_lift, "rent": [RENT_BASE, RENT_HIGH]}}

# ----------------------------------------------------------------------------------------------
# F. RISK REGISTER (probability x impact; sources in each row)
# ----------------------------------------------------------------------------------------------
equity_at_max = (1-LTV_BASE)*MAX_PRICE
F = [
 {"risk": "2008-style drawdown (>=40% peak-to-trough) within 10 years", "probability": f"{mc_stats['share_max_drawdown_ge_40pct']:.0%} of Monte Carlo paths (crash hazard 2%/yr; FHFA county -48.5% 2005-12; ZIP share of negative 5-yr windows 20-27%)",
  "impact": f"at 75% LTV, equity (${equity_at_max:,.0f} at the max price) is wiped out and the loan goes under water; 2008-replay 10-yr equity multiple {C['scenarios_at_max_price']['bear_2008_replay']['hold10']['equity_multiple']:.2f}x", "mitigation": "buy below market, 25%+ down, hold >10 yrs, no forced sale", "src": "valuation_methods KQ3/KQ5; market_history KQ1; model section B3"},
 {"risk": "Eviction / non-payment / vacancy", "probability": "Clayton 38.9 filings per 100 renter households (2023; serial filings inflate); ~10-15%/yr chance of an eviction event for a screened SFR tenant (model: 1-2 events per 10 yrs in bear cases)",
  "impact": "$2,500-$7,000 per event + 1-3 months rent; expected ~$500-$1,000/yr; 8% vacancy allowance already in base", "mitigation": "3x income screening (thin pool: $73,800 needed vs $42,403 renter median); voucher tenant; 2-month deposit cap", "src": "rental_and_operating_costs KQ2"},
 {"risk": "Insurance and property-tax escalation", "probability": "high (80%+): GA premiums +7-10%/yr; county millage above rollback three years running; investor gets no HOME Act cap",
  "impact": f"insurance $1,500 -> ${INSURANCE*(1+INS_GROWTH)**9:,.0f} by yr 10; tax ${tax_nonhomestead(MAX_PRICE):,.0f} -> ${tax_nonhomestead(MAX_PRICE)*(1+TAX_GROWTH)**9:,.0f}; NOI growth lags rent growth", "mitigation": "appeal 2027 FMV to purchase price within 45 days; shop DP-3 with 1-2% wind/hail deductible", "src": "gapfill_6 KQ1-KQ3; rental KQ4"},
 {"risk": "1968 systems failure (HVAC, water heater, aluminum wiring, galvanized supply, sewer lateral, crawl moisture)", "probability": "HVAC/WH age unknown (50% replace within 5 yrs); aluminum branch wiring possible (1965-73 window, ~25%); galvanized supply likely (~50%); lateral ~20%; crawl moisture ~30%",
  "impact": "expected ~$9,000-$12,000 over 5 yrs; bad case $25,000 (contingency); insurer surcharge/decline on aluminum wiring or FPE panel", "mitigation": "inspection with panel-cover removal, receptacle sampling, sewer scope, data-plate reads; price the findings into the offer", "src": "gapfill_3 KQ4; builder_and_construction KQ2/KQ4"},
 {"risk": "Airport noise / 65 DNL contour", "probability": "<5%: 7.1 mi from runway complex, no airport overlay on parcel; moderate ambient noise scores (SoundScore 73; Local Logic 2.3/10)", "impact": "none expected on value; no NIP eligibility; ambient Tara Blvd noise may lengthen owner-occupant DOM slightly", "mitigation": "confirm with ATL Dept of Aviation noise office before resale", "src": "gapfill_8 KQ1; property_record KQ5"},
 {"risk": "Flood", "probability": "FEMA Zone X, Flood Factor 1/10, county floodplain NO (~1% over 30 yrs)", "impact": "negligible; no flood insurance required", "mitigation": "none needed; verify crawl/addition drainage", "src": "property_record KQ5"},
 {"risk": "Corporate-landlord supply and rent competition", "probability": "high (70%): 15-16 of 61 subdivision parcels entity-owned; institutional operators asking $1,781-$1,985 for 4BR in 30238; INVH net seller (657 sold vs 196 bought Q2 2026)", "impact": "achieved rent $115-$140/mo below private asks; resale competes with institutional dispositions of renovated 3-4BR ranches", "mitigation": "underwrite $2,000-$2,050; compete on condition/responsiveness; voucher tenancy", "src": "gapfill_4 KQ1; valuation_methods KQ4; builder KQ3"},
 {"risk": "School and crime perception capping owner-occupant exit demand", "probability": "persistent (90%): Swint ES 4/10, Jonesboro HS 3-4/10, district #199/222; tract 73% renter, $27,500 median income; county Part One crime down 22% (2024) and 17% (2025) but burglary +19% in 2026", "impact": "thin FHA/first-time pool; exit liquidity depends on rate-sensitive buyers; DOM 61 median; price cuts on 35.8% of listings", "mitigation": "plan a 10-yr hold; exit as a tenanted asset to an investor if owner-occupant demand is weak", "src": "property_record KQ6; city_and_county_outlook 4-6; gapfill_8 KQ3"},
 {"risk": "Property-specific: unpermitted 544 sf addition (4th bed/bath), unpermitted panel/roof/windows, garage not on county record, county 3BR vs MLS 4BR, slab vs crawl conflict", "probability": "near-certain that no permits exist (none in 2016-2025 exports; assessor permit tab empty); 20-30% chance an exit lender's appraiser assigns the addition reduced value",
  "impact": "resale value on 1,575 sf main block only would be ~$30,000-$50,000 lower; after-the-fact permits $500-$3,000; insurer may require electrical inspection letter", "mitigation": "pull EnerGov history, obtain contractor invoices, after-the-fact permits, licensed-electrician letter; underwrite conservative case on 1,575 sf + discounted addition", "src": "gapfill_2 KQ1-KQ3; gapfill_7 KQ3; verification claims 3-4"},
 {"risk": "Estate-sale execution: two out-of-state executors, no seller disclosure, unknown mortgage payoff, 2.2-year contested probate", "probability": "medium (30-40%) of delay or title friction; low (10%) that payoff exceeds net proceeds at a discounted price", "impact": "closing delay; as-is terms; need both executors' signatures and certified Letters Testamentary", "mitigation": "due-diligence period, owner's title policy, ask for lender name/payoff before offering", "src": "gapfill_1 KQ1-KQ2"},
 {"risk": "Radon (EPA Zone 1 county; 15-21% of Clayton tests >= 4 pCi/L) and lead paint (pre-1978)", "probability": "radon ~15-21%; lead paint present with high probability on original trim", "impact": "radon mitigation ~$1,000-$2,500 (not sourced locally); lead-safe work practices on renovation; disclosure", "mitigation": "radon test during inspection ($150-$300)", "src": "builder_and_construction KQ2"},
 {"risk": "Rate / exit-financing risk", "probability": "30-yr rate 7.40% (3-yr high); Zillow expects 7.1% end-2026, 6.5% end-2027; FOMC median funds 4.1% through 2027", "impact": "+1 pt on the rate lowers the max price by ~$" + f"{(D['hurdles_base']['binding_return_hurdles']-D['sensitivity']['rate_plus_1pt']['binding_return_hurdles']):,.0f}" + "; buyer pool shrinks above 7%", "mitigation": "DSCR loan at 6.75% par with 3-2-1 prepay; refinance option if rates fall", "src": "valuation_methods KQ6; gapfill_6 KQ4; model section D"},
 {"risk": "Voucher payment standard / rent-reasonableness uncertainty", "probability": "JHA schedule unpublished; DCA proposed cutting its own standards to 90% of FMR (June 2026); FY2027 SAFMR fell 4.1%", "impact": "voucher contract rent capped near $2,050-$2,150 regardless of a $2,552 ceiling; standard could be $2,088", "mitigation": "call JHA (770-478-7282) for the standard, utility allowance and RFTA timing before relying on Section 8", "src": "gapfill_4 KQ2"},
]

# ----------------------------------------------------------------------------------------------
# OUTPUT
# ----------------------------------------------------------------------------------------------
def clean(o):
    if isinstance(o, dict): return {str(k): clean(v) for k, v in o.items()}
    if isinstance(o, (list, tuple)): return [clean(x) for x in o]
    if isinstance(o, (np.floating, float)): return None if (isinstance(o, float) and math.isnan(o)) else float(o)
    if isinstance(o, (np.integer,)): return int(o)
    if isinstance(o, np.ndarray): return clean(o.tolist())
    return o
OUT = {"meta": {"subject": "8055 Crown Way, Jonesboro, GA 30238 (parcel 13211D B011)", "model_date": "2026-10-19", "script": os.path.abspath(__file__), "notes_dir": "/home/user/GameSim/research_notes/8055 Crown Way investment analysis/"},
       "inputs": I, "A_current_value": A, "B_appreciation": B, "C_cash_flow": C, "D_price_to_buy": D, "E_value_add": E, "F_risk_register": F}
with open(os.path.join(OUT_DIR, "valuation_outputs.json"), "w") as f:
    json.dump(clean(OUT), f, indent=1)

# ---- printed summary ----
def money(x): return f"${x:,.0f}"
print("=== A. CURRENT VALUE ===")
print("Sales comparison grid (as-is):")
for g in grid: print(f"  {g['comp']:<26} {g['tier']:<8} net {money(g['net_price'])} adj {g['net_adjustment']:+,.0f} ({g['gross_adj_pct']:.0%} gross) -> {money(g['indicated_value'])}")
print("  owner tier:", {k: round(v) for k, v in A['sales_comparison']['owner_tier'].items()}, "| investor tier:", {k: round(v) for k, v in A['sales_comparison']['investor_tier'].items()})
print("  ARV grid:", [(g['comp'], g['indicated_value']) for g in arv_grid], "mean", round(arv_ind.mean()))
print("Income approach values:", inc)
print(f"  NOI yr1 at list {money(noi_list)} -> cap {noi_list/LIST_PRICE:.2%}; opex ratio {det_list['opex_total']/det_list['gpr']:.1%}")
print("AVMs:", {k: (v['value'], [round(x) for x in v['median_error_band']]) for k, v in avm_out.items()})
print("Reconciled low/mid/high:", rec, "vs list", [f"{x:+.1%}" for x in A['reconciled']['vs_list_pct']])
print("\n=== B. APPRECIATION ===")
print(f"FHFA Clayton: CAGR 2000-25 {fh['cagr_2000_2025']:.2%}; drawdown 2005-12 {fh['drawdown_2005_2012']:.1%}; sd {fh['sd_annual_return_2001_2025']:.2%}; worst 5yr {fh['worst_5yr']:.1%}; neg 5yr windows {fh['share_negative_5yr_windows']:.0%}")
print("Momentum/MR: rent gap", round(rent_gap,3), "income gap", round(income_gap,3), "blended", round(fund_gap,3))
for k, v in paths_mm.items(): print(f"  {k}: yr1 {v[0]:+.2%}, yr2 {v[1]:+.2%}, yr5 {v[4]:+.2%}, yr10 {v[9]:+.2%} -> ", {T: round(x) for T, x in cum_values(v).items()})
print("  mean path values:", {T: round(x) for T, x in cum_values(mm_mean).items()})
print("Monte Carlo (crash regime on):"); [print(f"  yr {T}:", {k: round(v) for k, v in mc_pct[T].items()}) for T in HORIZONS]
print("  stats:", {k: round(v,3) for k, v in mc_stats.items()})
print("  no-crash stats:", {k: round(v,3) for k, v in mc_stats_nocrash.items()}, "| stress beta 1.8 yr5:", {k: round(v) for k, v in mc_pct_stress[5].items()})
for s in SCEN: print(f"  scenario {s}:", {T: round(B['scenarios'][s]['table'][T]['value']) for T in HORIZONS})
print("\n=== C. CASH FLOW at list ===")
y = pf_list
print(f"  P&I {money(y['pi_monthly'])}/mo; cash in {money(y['cash_invested'])}; NOI {money(y['year1_annual']['noi'])}; CF {money(y['year1_annual']['cash_flow'])}/yr ({y['year1_annual']['cash_flow']/12:,.0f}/mo); cap {y['cap_rate']:.2%}; CoC {y['cash_on_cash']:.2%}; lender DSCR {y['dscr_lender_gross_rent_over_pitia']:.2f}; NOI cov {y['dscr_noi_over_debt_service']:.2f}")
for s, r in C['scenarios_at_list'].items(): print(f"  {s}: IRR5 {r['hold5']['irr']:.2%} IRR10 {r['hold10']['irr']:.2%} EM10 {r['hold10']['equity_multiple']:.2f}")
print("  S8 at list: CF", round(s8['year1_annual']['cash_flow']), "IRR10", f"{s8['hold10']['irr']:.2%}")
print("  flip at list:", {k: round(v) if isinstance(v,float) else v for k, v in C['flip']['at_list_arv_mid'].items()})
print("  MC IRR at list:", {k: round(v,3) for k, v in C['mc_levered_irr_10yr_at_list'].items()})
print("\n=== D. PRICE TO BUY ===")
for k, v in D['hurdles_base'].items(): print(f"  {k}: {v if isinstance(v,str) else round(v)}")
print("  clean inspection:", {k: round(v) for k, v in D['hurdles_clean_inspection_no_contingency'].items() if not isinstance(v, str)})
print("  DSCR 6.75:", {k: round(v) for k, v in D['hurdles_dscr_loan_6.75'].items() if not isinstance(v, str)})
print("  80% LTV 7.00:", {k: round(v) for k, v in D['hurdles_80ltv_dscr_7.00'].items() if not isinstance(v, str)})
for k, v in D['sensitivity'].items():
    if k == 'exit_cap': print("  exit cap -> ", {c: (round(x['irr10_base_ge_12pct']), round(x['binding_return_hurdles'])) for c, x in v.items()})
    else: print(f"  {k}: return-hurdles {round(v['binding_return_hurdles'])} ({v['binding_return_hurdle']}); cap7.4 {round(v['cap_ge_7.4_arbor'])}; cap6.5 {round(v['cap_ge_6.5_mid'])}; coc6 {round(v['coc_ge_6pct'])}; irr12 {round(v['irr10_base_ge_12pct'])}; noicov1.2 {round(v['noi_coverage_ge_1.2'])}; bear2008 {round(v['bear_2008_replay_equity_multiple_ge_1'])}; bearp10 {round(v['bear_mc_p10_equity_multiple_ge_1'])}")
print("  MAX PRICE", MAX_PRICE, "| clean", MAX_PRICE_CLEAN, "| all-hurdles", ALL_HURDLE_PRICE, "| opening offer", OPEN_OFFER)
for s, r in C['scenarios_at_max_price'].items(): print(f"  at max: {s}: CoC {r['cash_on_cash']:.2%} IRR5 {r['hold5']['irr']:.2%} IRR10 {r['hold10']['irr']:.2%} EM10 {r['hold10']['equity_multiple']:.2f}")
print("  MC IRR at max:", {k: round(v,3) for k, v in C['mc_levered_irr_10yr_at_max_price'].items()})
print("  price ladder:")
for r in D["price_ladder"]:
    print(f"   {money(r['price'])} ({r['vs_list']:+.1%}): cash {money(r['cash_invested'])} CF {r['cf_month']:+,.0f}/mo cap {r['cap_rate']:.2%} CoC {r['cash_on_cash']:+.1%} DSCR {r['dscr_lender']:.2f} NOIcov {r['noi_coverage']:.2f} IRR5 {r['irr5_base']:.1%} IRR10 {r['irr10_base']:.1%} EM10 {r['em10_base']:.2f} bull10 {r['irr10_bull']:.1%} bear08 EM {r['em10_bear_2008']:.2f} bearP10 EM {r['em10_bear_p10']:.2f} flip290 {r['flip_profit_arv290']:+,.0f} flip280 {r['flip_profit_arv280']:+,.0f}")
print("  gain tables (purchase at list / max / open):")
for key in ["purchase_at_list", "purchase_at_max_price", "purchase_at_opening_offer"]:
    for s in ["bear_2008_replay", "bear_moderate_mc_p10", "base", "bull"]:
        g = B["gain_tables"][key][s]
        print(f"   {key:<26} {s:<22}", {T: (round(g[T]['value']), round(g[T]['gain_gross']), round(g[T]['gain_net_of_8pct_sale_costs']), round(g[T]['real_value'])) for T in HORIZONS})
print("  MC real percentiles:", {T: {k: round(v) for k, v in mc_pct_real[T].items()} for T in HORIZONS})
print("  repeat-sales trend:", {T: (round(v['central']), round(v['p16']), round(v['p84']), round(v['real_central'])) for T, v in trend.items()})
print("\n=== E. VALUE-ADD ===")
for it in E['items']: print(f"  {it['rank']:>2}. {it['item'][:60]:<60} cost {money(it['cost_mid'])} lift {money(it['value_lift_mid'])} ROI {it['roi_value_net_of_cost']:+.0%} rentyld {it['annual_rent_yield_on_cost']:.0%} [{it['flag'][:40]}]")
print("\nJSON written:", os.path.join(OUT_DIR, "valuation_outputs.json"))
