import duckdb
from medicaid_spending.config import PARQUET_PATH

def main():
    con = duckdb.connect()

    print("Row count:")
    row_count = con.execute(
        f"SELECT COUNT(*) FROM read_parquet('{PARQUET_PATH}')"
    ).fetchone()

    assert row_count is not None

    print(row_count[0])


    print("\nSchema:")
    print(con.execute(
        f"DESCRIBE SELECT * FROM read_parquet('{PARQUET_PATH}')"
    ).df())

if __name__ == "__main__":
    main()

