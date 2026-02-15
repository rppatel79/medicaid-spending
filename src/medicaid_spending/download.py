import requests
from medicaid_spending.config import PARQUET_PATH

#https://opendata.hhs.gov/datasets/medicaid-provider-spending/
DATASET_URL = "https://stopendataprod.blob.core.windows.net/datasets/medicaid-provider-spending/2026-02-09/medicaid-provider-spending.parquet"

def download_dataset():
    response = requests.get(DATASET_URL, stream=True)
    response.raise_for_status()  # Ensure we notice bad responses
    with open(PARQUET_PATH, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    print(f"Dataset downloaded to {PARQUET_PATH}")

if __name__ == "__main__":
    download_dataset()
