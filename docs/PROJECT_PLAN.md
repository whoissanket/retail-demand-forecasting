# Retail Demand Forecasting & Inventory Optimization
## Project Plan

---

## 1. Project Overview

The Retail Demand Forecasting & Inventory Optimization project is a production-oriented data analytics and machine learning system designed to analyze historical retail sales, forecast future product demand, and generate inventory planning recommendations.

The project uses the M5 Forecasting dataset, which contains historical Walmart retail unit sales across multiple products, stores, categories, departments, and geographical regions.

The system combines:

- Data ingestion
- Data preprocessing
- Exploratory Data Analysis
- Time-series analysis
- Baseline forecasting
- Prophet forecasting
- LightGBM forecasting
- Recursive multi-step forecasting
- Inventory optimization
- PostgreSQL analytics
- Streamlit dashboard visualization
- Automated testing

The overall objective is to transform historical retail sales data into actionable demand and inventory planning insights.

---

# 2. Problem Statement

Retail businesses need to maintain the right amount of inventory to satisfy customer demand.

If inventory is too high, the business may experience:

- Excess inventory
- Higher holding costs
- Increased storage requirements
- Product overstocking
- Capital being locked in unsold products

If inventory is too low, the business may experience:

- Stockout risk
- Lost sales
- Poor customer experience
- Emergency replenishment
- Reduced revenue opportunities

Therefore, a demand forecasting and inventory optimization system can help estimate future demand and support better replenishment planning.

This project focuses on developing such a system using historical retail sales data.

---

# 3. Project Objectives

The major objectives of the project are:

1. Load and understand the M5 retail sales dataset.

2. Clean and prepare the historical sales data.

3. Perform exploratory data analysis to identify demand patterns.

4. Analyze demand across:
   - Products
   - Stores
   - Categories
   - Departments
   - Time periods

5. Develop baseline forecasting models.

6. Develop an aggregate demand forecasting model using Prophet.

7. Develop an item-store level demand forecasting model using LightGBM.

8. Generate recursive multi-step forecasts for future demand.

9. Calculate inventory planning metrics.

10. Estimate:
    - Lead-time demand
    - Safety stock
    - Reorder point
    - Economic Order Quantity
    - Recommended order quantity

11. Store analytical results in PostgreSQL.

12. Build an interactive Streamlit dashboard.

13. Add automated project validation tests.

14. Provide complete project documentation.

---

# 4. Dataset

## 4.1 Dataset Used

The project uses the M5 Forecasting dataset.

The major input files are:

```text
calendar.csv
sales_train_evaluation.csv
sell_prices.csv