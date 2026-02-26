# Provider Outlier Detection by Procedure (HCPCS)

## Overview

This notebook identifies providers whose **paid per claim** for a given procedure (HCPCS code) is unusually high compared to other providers billing the **same** HCPCS. The approach is:

1. Aggregate claims and payments to **Provider × HCPCS** level  
2. Compute `paid_per_claim` per provider within each HCPCS  
3. Flag high outliers using an **IQR (Interquartile Range)** rule  
4. Rank flagged providers by **% above the HCPCS mean**

This produces a list of statistically high-cost providers for each procedure and highlights the most extreme cases across procedures.

---

## Data Extraction (DuckDB)

The source parquet is aggregated at **Provider × HCPCS × Month**. We sum across all months and compute:

```text
paid_per_claim = SUM(TOTAL_PAID) / SUM(TOTAL_CLAIMS)
```

We also compute each provider’s total claim volume for the HCPCS, and filter to stable estimates:

- Only include provider–HCPCS pairs with `SUM(TOTAL_CLAIMS) > 100`

---

## Outlier Detection Method (Within Each HCPCS)

For each HCPCS code, we compute:

- `Q1` = 25th percentile of provider `paid_per_claim`
- `Q3` = 75th percentile
- `IQR = Q3 − Q1`
- `UPPER_BOUND = Q3 + 1.5 × IQR`

A provider is flagged as a high outlier when:

```text
paid_per_claim > UPPER_BOUND
```

This is a standard box-plot rule for identifying high outliers and is performed **within each HCPCS** (no cross-procedure comparisons).

---

## Provider Ranking Metric: Percent Above HCPCS Mean

For interpretability, each flagged provider is also scored using the provider’s percent difference from the HCPCS mean:

```text
PERCENT_ABOVE_AVG =
((provider_paid_per_claim − mean_paid_per_claim_for_HCPCS) / mean_paid_per_claim_for_HCPCS) × 100
```

The notebook then ranks all flagged providers across HCPCS codes by `PERCENT_ABOVE_AVG` and selects the top N results for review.

---

## Provider Outliner

![Provider Outliner](/images/provider_outliers_detection.png)
