-- Top 5 Funds by AUM

SELECT fund_house,
SUM(aum_crore) total_aum
FROM fact_aum
GROUP BY fund_house
ORDER BY total_aum DESC
LIMIT 5;

-- Average NAV Per Month

SELECT
strftime('%Y-%m',date) month,
AVG(nav)
FROM fact_nav
GROUP BY month;

-- SIP YoY Growth

SELECT month,
AVG(yoy_growth_pct)
FROM fact_sip
GROUP BY month;

-- Transactions By State

SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state;

-- Expense Ratio < 1%

SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Top 10 Return Funds

SELECT scheme_name,
return_5yr_pct
FROM fact_performance
ORDER BY return_5yr_pct DESC
LIMIT 10;

-- Average AUM

SELECT AVG(aum_crore)
FROM fact_aum;

-- Redemption Trend

SELECT transaction_date,
SUM(amount_inr)
FROM fact_transactions
WHERE transaction_type='REDEMPTION'
GROUP BY transaction_date;

-- Highest NAV

SELECT amfi_code,
MAX(nav)
FROM fact_nav
GROUP BY amfi_code;

-- Risk Category Distribution

SELECT risk_category,
COUNT(*)
FROM dim_fund
GROUP BY risk_category;