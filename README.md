# Retail Demand Forecasting & Inventory Optimization

A production-oriented data analytics project that uses historical retail sales data to forecast future demand and generate inventory planning recommendations.

The project combines time-series forecasting, machine learning, inventory optimization, PostgreSQL analytics and an interactive Streamlit dashboard.

---

## 1. Project Overview

Retail businesses need accurate demand forecasts to maintain appropriate inventory levels and reduce stock-related risks.

This project develops an end-to-end analytics pipeline that transforms historical retail sales data into:

- Historical demand analysis
- Future demand forecasts
- Item-store level predictions
- Safety stock estimates
- Reorder points
- Economic Order Quantity (EOQ)
- Inventory priority classifications
- Replenishment planning signals
- Interactive business dashboards

The project is based on the M5 retail forecasting dataset.

---

## 2. Project Objectives

The main objectives are:

1. Analyze historical retail demand.
2. Identify demand patterns across products and stores.
3. Prepare chronological time-series data.
4. Establish baseline forecasting models.
5. Develop advanced forecasting models.
6. Generate 28-day demand forecasts.
7. Optimize inventory planning using forecast demand.
8. Store analytical results in PostgreSQL.
9. Provide SQL-based business analytics.
10. Build an interactive Streamlit dashboard.
11. Validate the pipeline using automated tests.

---

## 3. Technology Stack

| Category | Technology |
|---|---|
| Programming | Python |
| Data Processing | Pandas, NumPy |
| Visualization | Matplotlib, Plotly |
| Forecasting | Prophet |
| Machine Learning | LightGBM, Scikit-learn |
| Model Persistence | Joblib |
| Database | PostgreSQL |
| Database Connectivity | SQLAlchemy, Psycopg2 |
| Dashboard | Streamlit |
| Configuration | python-dotenv |
| Testing | Pytest |
| Development | Jupyter Notebook, VS Code |
| Version Control | Git, GitHub |

---
## Dataset Setup

The raw M5 dataset is not included in this repository because of its large file size.

Download the M5 Forecasting dataset from Kaggle and place the following files inside:

data/raw/

├── calendar.csv
├── sales_train_evaluation.csv
└── sell_prices.csv

After placing the dataset files in the correct directory, the notebooks and pipeline can be executed.


## 4. Dataset

The project uses the M5 retail forecasting dataset.

The raw dataset contains:

```text
calendar.csv
sales_train_evaluation.csv
sell_prices.csv
