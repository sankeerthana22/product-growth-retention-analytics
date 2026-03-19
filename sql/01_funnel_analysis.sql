-- Funnel Analysis
-- Replace table and column names after dataset is loaded

SELECT
    event_type,
    COUNT(DISTINCT user_id) AS users
FROM events
GROUP BY event_type
ORDER BY users DESC;
