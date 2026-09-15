import pandas as pd
import numpy as np
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def test_processed_daily_demand_exists():
    path = BASE_DIR / "data" / "processed" / "daily_demand.csv"

    assert path.exists(), "daily_demand.csv not found"


def test_daily_demand_data():
    path = BASE_DIR / "data" / "processed" / "daily_demand.csv"

    df = pd.read_csv(path)

    assert not df.empty
    assert "date" in df.columns
    assert "units_sold" in df.columns
    assert df["units_sold"].notna().all()
    assert (df["units_sold"] >= 0).all()


def test_inventory_results():
    path = (
        BASE_DIR
        / "reports"
        / "model_results"
        / "inventory_optimization_results.csv"
    )

    assert path.exists(), "Inventory optimization results not found"

    df = pd.read_csv(path)

    assert not df.empty
    assert len(df) == 50

    required_columns = [
        "item_id",
        "store_id",
        "forecast_28_day",
        "safety_stock",
        "reorder_point",
        "eoq",
        "recommended_order_quantity",
        "inventory_priority",
        "planning_action"
    ]

    for column in required_columns:
        assert column in df.columns


def test_inventory_values_are_valid():
    path = (
        BASE_DIR
        / "reports"
        / "model_results"
        / "inventory_optimization_results.csv"
    )

    df = pd.read_csv(path)

    numeric_columns = [
        "forecast_28_day",
        "average_daily_forecast",
        "peak_daily_forecast",
        "safety_stock",
        "reorder_point",
        "eoq",
        "recommended_order_quantity"
    ]

    for column in numeric_columns:
        assert df[column].notna().all()
        assert (df[column] >= 0).all()


def test_no_duplicate_item_store_pairs():
    path = (
        BASE_DIR
        / "reports"
        / "model_results"
        / "inventory_optimization_results.csv"
    )

    df = pd.read_csv(path)

    duplicates = df.duplicated(
        subset=["item_id", "store_id"]
    )

    assert not duplicates.any()


def test_recursive_forecast_exists():
    path = (
        BASE_DIR
        / "reports"
        / "model_results"
        / "recursive_lightgbm_forecast.csv"
    )

    assert path.exists(), "Recursive forecast file not found"

    df = pd.read_csv(path)

    assert not df.empty
    assert len(df) == 1400

    assert "item_id" in df.columns
    assert "store_id" in df.columns
    assert "date" in df.columns
    assert "forecast_units" in df.columns

    assert df["forecast_units"].notna().all()
    assert (df["forecast_units"] >= 0).all()