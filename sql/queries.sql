-- 1. Top 5 funds by AUM
SELECT * FROM fact_aum
ORDER BY aum DESC
LIMIT 5;

-- 2. Average NAV
SELECT AVG(nav) AS avg_nav
FROM fact_nav;

-- 3. Average NAV by month
SELECT strftime('%Y-%m', date) AS month,
AVG(nav) AS avg_nav
FROM fact_nav
GROUP BY month;

-- 4. Transactions by state
SELECT state,
COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- 5. SIP transactions
SELECT COUNT(*) AS sip_count
FROM fact_transactions
WHERE transaction_type='SIP';

-- 6. Total investment amount
SELECT SUM(amount_inr)
FROM fact_transactions;

-- 7. Average 1-year return
SELECT AVG(return_1yr_pct)
FROM fact_performance;

-- 8. Top performing funds
SELECT amfi_code,
return_1yr_pct
FROM fact_performance
ORDER BY return_1yr_pct DESC
LIMIT 5;

-- 9. Average alpha
SELECT AVG(alpha)
FROM fact_performance;

-- 10. Number of funds
SELECT COUNT(DISTINCT amfi_code)
FROM fact_performance;