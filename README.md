# Medicaid Spending Analysis

## Overview

This project handles downloading, converting, and exploring Medicaid provider spending data. The workflow runs in three stages: downloading the dataset, converting it to Parquet, and exploring it interactively.

## Modules

1. `download.py`
   - Downloads the parquet dataset from the specified URL.
   - Run via:  
     ```bash
     python -m medicaid_spending.download
     ```

2. `explore.py`
   - Provides example queries for summarizing or profiling the Parquet data.
   - Run via:  
     ```bash
     python -m medicaid_spending.explore
     ```

## Using the Notebook

The Jupyter notebook (e.g., `analysis.ipynb`) allows interactive exploration:
- Open the notebook in VS Code.
- Select the virtual environment kernel when prompted.
- Run the cells to query the Parquet file, visualize results, and analyze the data interactively.
