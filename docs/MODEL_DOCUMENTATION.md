# Retail Demand Forecasting & Inventory Optimization
## Model Documentation

---

# 1. Introduction

This document describes the forecasting and inventory optimization models developed for the Retail Demand Forecasting & Inventory Optimization project.

The objective of the modeling pipeline is to use historical retail sales data to:

- Understand demand patterns
- Forecast future demand
- Compare different forecasting approaches
- Generate item-store level forecasts
- Calculate inventory planning metrics
- Support replenishment planning

The project uses both statistical/time-series forecasting and machine learning approaches.

The forecasting models implemented are:

1. Naive Forecast
2. 7-Day Moving Average
3. Prophet
4. LightGBM
5. Recursive LightGBM Forecasting

The forecast output is subsequently used by the inventory optimization module.

---

# 2. Dataset

The project uses the M5 Forecasting dataset.

The primary files are:

```text
calendar.csv
sales_train_evaluation.csv
sell_prices.csv