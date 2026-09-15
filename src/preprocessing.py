import pandas as pd
from pathlib import Path


# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"


SALES_PATH = DATA_DIR / "sales_train_evaluation.csv"
CALENDAR_PATH = DATA_DIR / "calendar.csv"


def load_sales_data():
    """Load raw sales data."""

    print("Loading sales data...")

    sales = pd.read_csv(SALES_PATH)

    print("Sales data loaded.")
    print("Shape:", sales.shape)

    return sales


def load_calendar_data():
    """Load calendar data."""

    print("\nLoading calendar data...")

    calendar = pd.read_csv(CALENDAR_PATH)

    calendar["date"] = pd.to_datetime(calendar["date"])

    print("Calendar data loaded.")
    print("Shape:", calendar.shape)

    return calendar


def identify_day_columns(sales):
    """Identify daily sales columns."""

    day_columns = [
        column for column in sales.columns
        if column.startswith("d_")
    ]

    print("\nDaily sales columns:", len(day_columns))
    print("First:", day_columns[:5])
    print("Last:", day_columns[-5:])

    return day_columns


if __name__ == "__main__":

    sales = load_sales_data()
    calendar = load_calendar_data()

    day_columns = identify_day_columns(sales)

    print("\n" + "=" * 50)
    print("PREPROCESSING INITIALIZATION COMPLETE")
    print("=" * 50)