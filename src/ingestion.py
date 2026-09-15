import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent

DATA_DIR = BASE_DIR / "data" / "raw"

SALES_PATH = DATA_DIR / "sales_train_evaluation.csv"
CALENDAR_PATH = DATA_DIR / "calendar.csv"
PRICES_PATH = DATA_DIR / "sell_prices.csv"

def load_sales_data():
    """Load historical sales data."""

    print("Loading sales data...")

    sales = pd.read_csv(SALES_PATH)

    print("Sales data loaded successfully.")
    print("Shape:", sales.shape)

    return sales


def load_calendar_data():
    """Load calendar data."""

    print("\nLoading calendar data...")

    calendar = pd.read_csv(CALENDAR_PATH)

    print("Calendar data loaded successfully.")
    print("Shape:", calendar.shape)

    return calendar


def load_price_data():
    """Load product price data."""

    print("\nLoading price data...")

    prices = pd.read_csv(PRICES_PATH)

    print("Price data loaded successfully.")
    print("Shape:", prices.shape)

    return prices


def load_all_data():
    """Load all project datasets."""

    sales = load_sales_data()
    calendar = load_calendar_data()
    prices = load_price_data()

    return sales, calendar, prices


if __name__ == "__main__":

    sales, calendar, prices = load_all_data()

    print("\n" + "=" * 50)
    print("DATASET VERIFICATION")
    print("=" * 50)

    print("\nSales columns:")
    print(sales.columns.tolist())

    print("\nCalendar columns:")
    print(calendar.columns.tolist())

    print("\nPrice columns:")
    print(prices.columns.tolist())