from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]

PROCESSED_DATA_DIR = BASE_DIR / "data" / "processed"

PARQUET_PATH = PROCESSED_DATA_DIR / "medicaid-provider-spending.parquet"

