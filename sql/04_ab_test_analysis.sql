-- A/B Test Summary

SELECT
    test_group,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct
FROM ab_test
GROUP BY test_group;
