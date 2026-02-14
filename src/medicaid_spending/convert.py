import duckdb
from medicaid_spending.config import RAW_CSV_PATH, PARQUET_PATH

def convert_csv_to_parquet():
    con = duckdb.connect()

    print("Converting CSV to Parquet...")
    con.execute(f"""
        COPY (
            SELECT *
            FROM read_csv_auto('{RAW_CSV_PATH}')
        )
        TO '{PARQUET_PATH}'
        (FORMAT PARQUET);
    """)

    print("Conversion complete.")

if __name__ == "__main__":
    convert_csv_to_parquet()

