-- Segmentation Analysis
-- Example: conversion by device or traffic source

SELECT
    device_type,
    COUNT(*) AS users,
    SUM(converted) AS conversions,
    ROUND(100.0 * SUM(converted) / COUNT(*), 2) AS conversion_rate_pct
FROM user_sessions
GROUP BY device_type
ORDER BY conversion_rate_pct DESC;
