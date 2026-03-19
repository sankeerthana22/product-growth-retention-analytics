-- Top Customers by Revenue
SELECT
  CustomerID,
  Country,
  COUNT(DISTINCT InvoiceNo) AS orders,
  ROUND(SUM(TotalPrice),2) AS total_revenue
FROM online_retail
GROUP BY CustomerID, Country
ORDER BY total_revenue DESC
LIMIT 20;
