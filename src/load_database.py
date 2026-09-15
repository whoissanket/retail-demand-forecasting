import os
from pathlib import Path

import pandas as pd
from dotenv import load_dotenv
from sqlalchemy import create_engine
from urllib.parse import quote_plus


# ============================================
# Project Configuration
# ============================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "retail_demand_db")

encoded_password = quote_plus(DB_PASSWORD)

DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)

engine = create_engine(DATABASE_URL)


# ============================================
# Project Paths
# ============================================

RESULTS_DIR = BASE_DIR / "reports" / "model_results"
PROCESSED_DIR = BASE_DIR / "data" / "processed"


# ============================================
# Load Inventory Optimization
# ============================================

inventory_path = (
    RESULTS_DIR / "inventory_optimization_results.csv"
)

inventory = pd.read_csv(inventory_path)

print("Inventory results loaded:")
print(inventory.shape)


# ============================================
# Load Recursive Forecasts
# ============================================

forecast_path = (
    RESULTS_DIR / "recursive_lightgbm_forecast.csv"
)

forecasts = pd.read_csv(forecast_path)

print("\nForecast results loaded:")
print(forecasts.shape)


# ============================================
# Load Daily Demand
# ============================================

daily_demand_path = (
    PROCESSED_DIR / "daily_demand.csv"
)

daily_demand = pd.read_csv(daily_demand_path)

daily_demand["date"] = pd.to_datetime(
    daily_demand["date"]
)

print("\nDaily demand loaded:")
print(daily_demand.shape)


# ============================================
# Load Inventory Table
# ============================================

inventory.to_sql(
    "inventory_optimization",
    engine,
    if_exists="replace",
    index=False
)

print("\nInventory table loaded successfully.")


# ============================================
# Load Forecast Table
# ============================================

forecasts["date"] = pd.to_datetime(
    forecasts["date"]
)

forecasts.to_sql(
    "demand_forecasts",
    engine,
    if_exists="replace",
    index=False
)

print("Forecast table loaded successfully.")


# ============================================
# Load Daily Demand Table
# ============================================

daily_demand.to_sql(
    "daily_demand",
    engine,
    if_exists="replace",
    index=False
)

print("Daily demand table loaded successfully.")


print("\n========================================")
print("DATABASE LOADING COMPLETE")
print("========================================")