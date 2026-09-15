import os
from pathlib import Path
from urllib.parse import quote_plus

from sqlalchemy import create_engine, text
from dotenv import load_dotenv


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


# Encode password so special characters like @ work correctly
encoded_password = quote_plus(DB_PASSWORD)


DATABASE_URL = (
    f"postgresql+psycopg2://"
    f"{DB_USER}:{encoded_password}@"
    f"{DB_HOST}:{DB_PORT}/{DB_NAME}"
)


# Create database engine
engine = create_engine(DATABASE_URL)


# ============================================
# Test Database Connection
# ============================================

def test_connection():

    try:

        with engine.connect() as connection:

            result = connection.execute(
                text("SELECT 1")
            )

            print("Database Connected Successfully!")
            print("Test result:", result.scalar())

    except Exception as e:

        print("Database connection failed!")
        print("Error:", e)


# ============================================
# Main
# ============================================

if __name__ == "__main__":
    test_connection()