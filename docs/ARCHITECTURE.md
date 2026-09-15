# Retail Demand Forecasting & Inventory Optimization
## System Architecture

---

## 1. Overview

The Retail Demand Forecasting & Inventory Optimization project is a production-oriented analytics pipeline designed to transform historical retail sales data into demand forecasts and inventory planning recommendations.

The system follows a modular architecture:

```text
M5 Retail Dataset
        |
        v
Data Ingestion
        |
        v
Data Preprocessing
        |
        v
Exploratory Data Analysis
        |
        v
Time-Series Preparation
        |
        v
Demand Forecasting
   |              |
   |              |
Prophet        LightGBM
   |              |
   |              v
   |       Recursive Forecasting
   |              |
   +--------------+
          |
          v
Forecast Results
          |
          v
Inventory Optimization
          |
          v
PostgreSQL Database
          |
          v
SQL Analytics
          |
          v
Streamlit Dashboard