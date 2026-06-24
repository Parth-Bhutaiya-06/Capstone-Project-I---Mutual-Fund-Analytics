# Data Dictionary
## Dataset 1: Fund Master

**Source File:** 01_fund_master.csv
This dataset contains the basic details of all mutual fund schemes.

**amfi_code (Integer):** Unique identification number assigned to each mutual fund scheme.
**fund_house (Text):** Name of the Asset Management Company (AMC).
**scheme_name (Text):** Name of the mutual fund scheme.
**category (Text):** Main category of the fund such as Equity, Debt, or Hybrid.
**sub_category (Text):** More specific classification within a category.
**plan (Text):** Indicates whether the scheme is Direct or Regular.
**launch_date (Date):** Date on which the scheme was launched.
**benchmark (Text):** Market index used to compare the scheme's performance.
**expense_ratio_pct (Real):** Percentage charged annually for managing the fund.
**exit_load_pct (Real):** Fee charged if investors withdraw before a specified period.
**min_sip_amount (Real):** Minimum amount required for SIP investment.
**min_lumpsum_amount (Real):** Minimum amount required for one-time investment.
**fund_manager (Text):** Name of the person managing the fund.
**risk_category (Text):** Risk level associated with the scheme.
**sebi_category_code (Text):** Regulatory classification assigned by SEBI.

## Dataset 2: NAV History

**Source File:** 02_nav_history.csv

This dataset stores historical Net Asset Value (NAV) information for mutual funds.

**amfi_code (Integer):** Unique scheme identifier.
**date (Date):** Date on which NAV was recorded.
**nav (Real):** Net Asset Value of the scheme on that date.

## Dataset 3: AUM by Fund House

**Source File:** 03_aum_by_fund_house.csv

This dataset provides information about assets managed by fund houses.

**date (Date):** Reporting date.
**fund_house (Text):** Name of the AMC.
**aum_lakh_crore (Real):** Assets under management in lakh crore rupees.
**aum_crore (Real):** Assets under management in crore rupees.
**num_schemes (Integer):** Total number of schemes managed by the AMC.
# Dataset 4: Monthly SIP Inflows

**Source File:** 04_monthly_sip_inflows.csv

This dataset tracks monthly SIP investment trends.

**month (Text):** Reporting month.
**sip_inflow_crore (Real):** Total SIP inflow amount in crore rupees.
**active_sip_accounts_crore (Real):** Number of active SIP accounts.
**new_sip_accounts_lakh (Real):** Number of newly registered SIP accounts.
**sip_aum_lakh_crore (Real):** SIP ssets under management.
**yoy_growth_pct (Real):** Year-over-year growth percentage.

## Dataset 5: Category Inflows

**Source File:** 05_category_inflows.csv

This dataset records money flowing into different fund categories.

**month (Text):** Reporting month.
**category (Text):** Mutual fund category.
**net_inflow_crore (Real):** Net amount invested in the category.

## Dataset 6: Industry Folio Count

**Source File:** 06_industry_folio_count.csv

This dataset shows the number of investor folios in the mutual fund industry.

**month (Text):** Reporting month.
**total_folios_crore (Real):** Total folio count.
**equity_folios_crore (Real):** Equity fund folios.
**debt_folios_crore (Real):** Debt fund folios.
**hybrid_folios_crore (Real):** Hybrid fund folios.
**others_folios_crore (Real):** Folios from other categories.

## Dataset 7: Scheme Performance

**Source File:** 07_scheme_performance.csv

This dataset contains performance and risk-related information for mutual fund schemes.

**amfi_code (Integer):** Unique scheme identifier.
**scheme_name (Text):** Name of the scheme.
**fund_house (Text):** AMC managing the scheme.
**category (Text):** Fund category.
**plan (Text):** Direct or Regular plan.
**return_1yr_pct (Real):** One-year return percentage.
**return_3yr_pct (Real):** Three-year return percentage.
**return_5yr_pct (Real):** Five-year return percentage.
**benchmark_3yr_pct (Real):** Three-year benchmark return.
**alpha (Real):** Excess return over benchmark.
**beta (Real):** Measure of market-related risk.
**sharpe_ratio (Real):** Risk-adjusted return metric.
**sortino_ratio (Real):** Downside risk-adjusted return metric.
**std_dev_ann_pct (Real):** Annualized volatility.
**max_drawdown_pct (Real):** Maximum observed loss.
**aum_crore (Real):** Assets under management.
**expense_ratio_pct (Real):** Annual expense ratio.
**morningstar_rating (Integer):** und rating score.
**risk_grade (Text):** Overall risk grade.

## Dataset 8: Investor Transactions

**Source File:** 08_investor_transactions.csv

This dataset records investment transactions performed by investors.

**investor_id (Text):** Unique investor identifier.
**transaction_date (Date):** Date of transaction.
**amfi_code (Integer):** Scheme identifier.
**transaction_type (Text):** SIP, Lumpsum, or Redemption.
**amount_inr (Real):** Transaction amount in Indian Rupees.
**state (Text):** Investor's state.
**city (Text):** Investor's city.
**city_tier (Text):** Classification of city.
**age_group (Text):** Investor age category.
**gender (Text):** Investor gender.
**annual_income_lakh (Real):** Annual income in lakhs.
**payment_mode (Text):** Mode used for payment.
**kyc_status (Text):** KYC verification status.

## Dataset 9: Portfolio Holdings

**Source File:** 09_portfolio_holdings.csv

This dataset contains stock holdings of mutual fund schemes.

**amfi_code (Integer):** Scheme identifier.
**stock_symbol (Text):** Stock trading symbol.
**stock_name (Text):** Name of the stock.
**sector (Text):** Industry sector of the stock.
**weight_pct (Real):** Percentage weight in portfolio.
**market_value_cr (Real):** Market value in crore rupees.
**current_price_inr (Real):** Current stock price.
**portfolio_date (Date):** Portfolio reporting date.

## Dataset 10: Benchmark Indices

**Source File:** 10_benchmark_indices.csv

This dataset stores benchmark index values used for performance comparison.

**date (Date):** Trading date.
**index_name (Text):** Name of the benchmark index.
**close_value (Real):** Closing value of the index.
