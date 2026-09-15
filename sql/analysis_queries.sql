-- ============================================
-- Retail Demand Forecasting
-- Business Analysis Queries
-- ============================================


-- 1. Top item-store combinations by forecast demand

SELECT
    item_id,
    store_id,
    forecast_28_day,
    average_daily_forecast
FROM inventory_optimization
ORDER BY forecast_28_day DESC
LIMIT 10;


-- 2. Highest safety stock requirements

SELECT
    item_id,
    store_id,
    safety_stock,
    reorder_point
FROM inventory_optimization
ORDER BY safety_stock DESC
LIMIT 10;


-- 3. Highest recommended order quantities

SELECT
    item_id,
    store_id,
    recommended_order_quantity,
    eoq
FROM inventory_optimization
ORDER BY recommended_order_quantity DESC
LIMIT 10;


-- 4. Inventory priority distribution

SELECT
    inventory_priority,
    COUNT(*) AS item_count
FROM inventory_optimization
GROUP BY inventory_priority
ORDER BY item_count DESC;


-- 5. Planning action distribution

SELECT
    planning_action,
    COUNT(*) AS item_count
FROM inventory_optimization
GROUP BY planning_action
ORDER BY item_count DESC;


-- 6. Average inventory metrics

SELECT
    AVG(forecast_28_day) AS avg_28_day_forecast,
    AVG(safety_stock) AS avg_safety_stock,
    AVG(reorder_point) AS avg_reorder_point,
    AVG(eoq) AS avg_eoq
FROM inventory_optimization;


-- 7. Store-level forecast demand

SELECT
    store_id,
    SUM(forecast_28_day) AS total_forecast_demand,
    AVG(average_daily_forecast) AS avg_daily_forecast
FROM inventory_optimization
GROUP BY store_id
ORDER BY total_forecast_demand DESC;


-- 8. Products requiring high replenishment attention

SELECT
    item_id,
    store_id,
    forecast_28_day,
    reorder_point,
    recommended_order_quantity,
    planning_action
FROM inventory_optimization
WHERE planning_action = 'High Replenishment Need'
ORDER BY forecast_28_day DESC;


-- 9. Highest historical demand products

SELECT
    item_id,
    store_id,
    historical_mean_demand,
    historical_max_demand
FROM inventory_optimization
ORDER BY historical_mean_demand DESC
LIMIT 10;


-- 10. Forecast versus historical demand

SELECT
    item_id,
    store_id,
    historical_mean_demand,
    average_daily_forecast,
    forecast_28_day
FROM inventory_optimization
ORDER BY forecast_28_day DESC
LIMIT 20;