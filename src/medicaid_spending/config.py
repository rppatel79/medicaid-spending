from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

RAW_DATA_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

RAW_CSV_PATH = RAW_DATA_DIR / "medicaid-provider-spending.csv"
PARQUET_PATH = PROCESSED_DATA_DIR / "medicaid_provider_spending.parquet"

