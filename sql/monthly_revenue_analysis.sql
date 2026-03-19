-- Monthly Revenue Trend
SELECT
  strftime('%Y-%m', InvoiceDate) AS order_month,
  ROUND(SUM(TotalPrice),2) AS monthly_revenue,
  COUNT(DISTINCT CustomerID) AS customers
FROM online_retail
GROUP BY order_month
ORDER BY order_month;
