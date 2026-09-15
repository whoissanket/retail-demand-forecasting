import os
from pathlib import Path
from urllib.parse import quote_plus

import pandas as pd
import streamlit as st
import plotly.express as px

from sqlalchemy import create_engine
from dotenv import load_dotenv


# ============================================================
# PROJECT CONFIGURATION
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent

load_dotenv(BASE_DIR / ".env")


DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")
DB_NAME = os.getenv("DB_NAME", "retail_demand_db")


# Encode password so special characters such as @ work correctly
encoded_password = quote_plus(DB_PASSWORD)


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


engine = create_engine(DATABASE_URL)


# ============================================================
# STREAMLIT PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📊",
    layout="wide"
)


# ============================================================
# TITLE
# ============================================================

st.title(
    "📊 Retail Demand Forecasting & Inventory Optimization"
)

st.markdown(
    """
    **Production Analytics Dashboard**

    This dashboard combines demand forecasting, inventory
    optimization and PostgreSQL analytics for retail planning.
    """
)


# ============================================================
# DATABASE LOADING FUNCTIONS
# ============================================================

@st.cache_data
def load_inventory_data():

    query = """
        SELECT *
        FROM inventory_optimization
    """

    return pd.read_sql(query, engine)


@st.cache_data
def load_forecast_data():

    query = """
        SELECT *
        FROM demand_forecasts
    """

    return pd.read_sql(query, engine)


@st.cache_data
def load_daily_demand():

    query = """
        SELECT *
        FROM daily_demand
        ORDER BY date
    """

    return pd.read_sql(query, engine)


# ============================================================
# LOAD DATABASE DATA
# ============================================================

try:

    inventory = load_inventory_data()
    forecasts = load_forecast_data()
    daily_demand = load_daily_demand()

except Exception as e:

    st.error(
        "Unable to connect to PostgreSQL database."
    )

    st.error(str(e))

    st.stop()


# ============================================================
# DATA VALIDATION
# ============================================================

if inventory.empty:

    st.error(
        "Inventory data is empty."
    )

    st.stop()


if forecasts.empty:

    st.error(
        "Forecast data is empty."
    )

    st.stop()


if daily_demand.empty:

    st.error(
        "Daily demand data is empty."
    )

    st.stop()


# ============================================================
# PREPARE DATE COLUMNS
# ============================================================

if "date" in daily_demand.columns:

    daily_demand["date"] = pd.to_datetime(
        daily_demand["date"]
    )


if "date" in forecasts.columns:

    forecasts["date"] = pd.to_datetime(
        forecasts["date"]
    )


# ============================================================
# SIDEBAR FILTERS
# ============================================================

st.sidebar.header("🔎 Dashboard Filters")


stores = sorted(
    inventory["store_id"]
    .dropna()
    .unique()
)


selected_store = st.sidebar.selectbox(
    "Select Store",
    ["All Stores"] + list(stores)
)


priorities = sorted(
    inventory["inventory_priority"]
    .dropna()
    .unique()
)


selected_priority = st.sidebar.selectbox(
    "Inventory Priority",
    ["All Priorities"] + list(priorities)
)


# ============================================================
# APPLY FILTERS
# ============================================================

filtered_inventory = inventory.copy()


if selected_store != "All Stores":

    filtered_inventory = filtered_inventory[
        filtered_inventory["store_id"] == selected_store
    ]


if selected_priority != "All Priorities":

    filtered_inventory = filtered_inventory[
        filtered_inventory["inventory_priority"]
        == selected_priority
    ]


# ============================================================
# KPI CALCULATIONS
# ============================================================

total_forecast = (
    filtered_inventory["forecast_28_day"]
    .sum()
)


average_daily_demand = (
    filtered_inventory["average_daily_forecast"]
    .sum()
)


total_safety_stock = (
    filtered_inventory["safety_stock"]
    .sum()
)


total_recommended_order = (
    filtered_inventory["recommended_order_quantity"]
    .sum()
)


high_demand_items = (
    filtered_inventory["inventory_priority"]
    .eq("High Demand")
    .sum()
)


# ============================================================
# KPI CARDS
# ============================================================

st.subheader("📌 Key Performance Indicators")


col1, col2, col3, col4, col5 = st.columns(5)


with col1:

    st.metric(
        "28-Day Forecast",
        f"{total_forecast:,.0f}"
    )


with col2:

    st.metric(
        "Avg Daily Demand",
        f"{average_daily_demand:,.0f}"
    )


with col3:

    st.metric(
        "Safety Stock",
        f"{total_safety_stock:,.0f}"
    )


with col4:

    st.metric(
        "Recommended Order",
        f"{total_recommended_order:,.0f}"
    )


with col5:

    st.metric(
        "High Demand Items",
        int(high_demand_items)
    )


# ============================================================
# HISTORICAL DEMAND TREND
# ============================================================

st.subheader("📈 Historical Daily Demand")


fig_demand = px.line(
    daily_demand,
    x="date",
    y="units_sold",
    title="Historical Daily Retail Demand"
)


fig_demand.update_layout(
    xaxis_title="Date",
    yaxis_title="Units Sold",
    hovermode="x unified"
)


st.plotly_chart(
    fig_demand,
    use_container_width=True
)


# ============================================================
# STORE FORECAST + INVENTORY PRIORITY
# ============================================================

col_left, col_right = st.columns(2)


# ------------------------------------------------------------
# STORE FORECAST
# ------------------------------------------------------------

with col_left:

    st.subheader("🏪 Forecast Demand by Store")


    store_forecast = (
        filtered_inventory
        .groupby(
            "store_id",
            as_index=False
        )["forecast_28_day"]
        .sum()
        .sort_values(
            "forecast_28_day",
            ascending=False
        )
    )


    fig_store = px.bar(
        store_forecast,
        x="store_id",
        y="forecast_28_day",
        title="28-Day Forecast by Store"
    )


    fig_store.update_layout(
        xaxis_title="Store",
        yaxis_title="Forecast Units"
    )


    st.plotly_chart(
        fig_store,
        use_container_width=True
    )


# ------------------------------------------------------------
# INVENTORY PRIORITY
# ------------------------------------------------------------

with col_right:

    st.subheader("📦 Inventory Priority")


    priority_counts = (
        filtered_inventory[
            "inventory_priority"
        ]
        .value_counts()
        .reset_index()
    )


    priority_counts.columns = [
        "inventory_priority",
        "item_count"
    ]


    fig_priority = px.pie(
        priority_counts,
        names="inventory_priority",
        values="item_count",
        title="Inventory Priority Distribution"
    )


    st.plotly_chart(
        fig_priority,
        use_container_width=True
    )


# ============================================================
# PLANNING ACTION DISTRIBUTION
# ============================================================

st.subheader("🚚 Planning Actions")


planning_counts = (
    filtered_inventory[
        "planning_action"
    ]
    .value_counts()
    .reset_index()
)


planning_counts.columns = [
    "planning_action",
    "item_count"
]


fig_planning = px.bar(
    planning_counts,
    x="planning_action",
    y="item_count",
    title="Inventory Planning Actions"
)


fig_planning.update_layout(
    xaxis_title="Planning Action",
    yaxis_title="Number of Items"
)


st.plotly_chart(
    fig_planning,
    use_container_width=True
)


# ============================================================
# TOP ITEM-STORE COMBINATIONS
# ============================================================

st.subheader(
    "🔥 Top Item-Store Combinations by Forecast Demand"
)


top_items = (
    filtered_inventory
    .sort_values(
        "forecast_28_day",
        ascending=False
    )
    .head(10)
)


st.dataframe(
    top_items[
        [
            "item_id",
            "store_id",
            "forecast_28_day",
            "average_daily_forecast",
            "peak_daily_forecast",
            "safety_stock",
            "reorder_point",
            "eoq",
            "recommended_order_quantity",
            "inventory_priority",
            "planning_action"
        ]
    ],
    use_container_width=True
)


# ============================================================
# INVENTORY OPTIMIZATION DETAILS
# ============================================================

st.subheader(
    "📋 Inventory Optimization Details"
)


st.dataframe(
    filtered_inventory[
        [
            "item_id",
            "store_id",
            "forecast_28_day",
            "average_daily_forecast",
            "peak_daily_forecast",
            "historical_mean_demand",
            "historical_std_demand",
            "lead_time_demand",
            "safety_stock",
            "reorder_point",
            "eoq",
            "recommended_order_quantity",
            "inventory_priority",
            "planning_action"
        ]
    ],
    use_container_width=True
)


# ============================================================
# FOOTER
# ============================================================

st.divider()


st.caption(
    "Retail Demand Forecasting & Inventory Optimization | "
    "Python • LightGBM • PostgreSQL • Streamlit"
)