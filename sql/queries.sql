-- Top 5 funds by AUM
SELECT scheme_name, aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Average NAV by month
SELECT strftime('%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- Transactions by state
SELECT state,
COUNT(*) AS transactions
FROM fact_transactions
GROUP BY state
ORDER BY transactions DESC;

-- Funds with expense ratio < 1%
SELECT scheme_name,
expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1;

-- Average 1-year return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- Highest Sharpe Ratio
SELECT scheme_name,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- Highest Alpha
SELECT scheme_name,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;

-- Transactions by type
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- Average investment amount
SELECT AVG(amount_inr)
FROM fact_transactions;


SELECT state,
SUM(amount_inr)
FROM fact_transactions
GROUP BY state
ORDER BY SUM(amount_inr) DESC
LIMIT 5;