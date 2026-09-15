-- ============================================
-- Retail Demand Forecasting Database Schema
-- ============================================

-- Daily aggregate demand
CREATE TABLE IF NOT EXISTS daily_demand (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    units_sold DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Item-store demand forecasts
CREATE TABLE IF NOT EXISTS demand_forecasts (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(50) NOT NULL,
    store_id VARCHAR(20) NOT NULL,
    forecast_date DATE NOT NULL,
    forecast_units DOUBLE PRECISION NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Inventory optimization results
CREATE TABLE IF NOT EXISTS inventory_optimization (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(50) NOT NULL,
    store_id VARCHAR(20) NOT NULL,

    forecast_28_day DOUBLE PRECISION,
    average_daily_forecast DOUBLE PRECISION,
    peak_daily_forecast DOUBLE PRECISION,

    historical_mean_demand DOUBLE PRECISION,
    historical_std_demand DOUBLE PRECISION,
    historical_max_demand DOUBLE PRECISION,

    lead_time_demand DOUBLE PRECISION,
    safety_stock DOUBLE PRECISION,
    reorder_point DOUBLE PRECISION,

    eoq INTEGER,
    recommended_order_quantity INTEGER,

    inventory_priority VARCHAR(30),
    planning_action VARCHAR(50),

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);


-- Product information
CREATE TABLE IF NOT EXISTS product_information (
    id SERIAL PRIMARY KEY,
    item_id VARCHAR(50) NOT NULL,
    dept_id VARCHAR(50),
    cat_id VARCHAR(50),
    store_id VARCHAR(20),
    state_id VARCHAR(20),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);