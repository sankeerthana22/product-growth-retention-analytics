-- Revenue by Country
SELECT
  Country,
  COUNT(DISTINCT CustomerID) AS customers,
  ROUND(SUM(TotalPrice),2) AS revenue
FROM online_retail
GROUP BY Country
ORDER BY revenue DESC;
