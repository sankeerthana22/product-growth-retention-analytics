-- Cohort Analysis
-- Example structure only; final version depends on dataset schema

WITH first_purchase AS (
    SELECT
        customer_id,
        MIN(DATE(order_date)) AS cohort_date
    FROM orders
    GROUP BY customer_id
),
activity AS (
    SELECT
        o.customer_id,
        DATE(o.order_date) AS activity_date,
        f.cohort_date
    FROM orders o
    JOIN first_purchase f
      ON o.customer_id = f.customer_id
)
SELECT *
FROM activity
LIMIT 20;
