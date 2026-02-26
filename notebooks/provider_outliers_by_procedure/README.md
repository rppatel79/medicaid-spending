## Observations: Provider Outliers Within Each Procedure (Paid per Claim)

To evaluate whether individual providers are reimbursed at unusually high levels for the *same* service, we calculated **paid per claim** for each:

- **HCPCS code**
- **Billing provider (NPI)**

Because the source data is aggregated at the **Provider × HCPCS × Month** level (2018–2024), we first summed payments and claims across all months for each provider–procedure pair and then computed:

> **paid_per_claim = total_paid / total_claims**

To ensure stable estimates and avoid distortion from low-volume providers, the analysis includes only provider–HCPCS combinations with:

> **more than 100 total claims**

This produces a volume-weighted average reimbursement per claim and allows meaningful comparisons **across providers performing the same procedure**.

---

### Key Observation: Most Providers Cluster Tightly, With a Small Number of High-Cost Outliers

Across many HCPCS codes, the distribution of paid per claim shows:

- A tight cluster of providers with similar reimbursement levels  
- A right-skewed distribution (long upper tail)  
- A small number of providers with substantially higher paid per claim than their peers  

This indicates that for many procedures:

> Reimbursement per claim is generally consistent across providers, but a small number of providers receive materially higher payments for the same service.

---

### Outlier Detection Method

We identified high-cost outliers separately within each HCPCS code using the **Interquartile Range (IQR)** rule:

- **Q1** = 25th percentile of paid per claim across providers  
- **Q3** = 75th percentile  
- **IQR = Q3 − Q1**  

A provider is flagged as a high outlier if:

> **paid_per_claim > Q3 + 1.5 × IQR**

These outliers appear as points beyond the whiskers in the box plots.

---

### Example: Provider Paid per Claim for a Single HCPCS

![Box Plot of Provider Paid per Claim](images/paid_per_claim_outliers_T2016.png)

---

### How to Interpret the Box Plot

- The **box** represents the middle 50% of providers (Q1–Q3)  
- The **median line** represents the typical paid per claim for the procedure  
- The **whiskers** represent the expected range for non-outlier providers  
- The **points beyond the whiskers** are providers with unusually high reimbursement per claim relative to peers  

---

### Important Interpretation Notes

These outliers are:

- **Procedure-specific** — comparisons are only made within the same HCPCS code  
- **Volume-stabilized** — each provider has at least 100 claims for that procedure  
- **Statistical signals** — not automatic indicators of inappropriate billing  

Higher paid per claim may reflect legitimate factors such as:

- Case-mix or patient severity  
- Place of service differences  
- Modifier usage  
- Geographic pricing adjustments  

However, they identify:

> Providers whose reimbursement patterns differ substantially from the norm and may warrant further review.

---

### Analytical Value

This approach enables:

- Procedure-level benchmarking of providers  
- Identification of reimbursement variation within the same service  
- Targeted, data-driven investigation rather than broad audits  

It highlights procedures where:

- Pricing is tightly standardized  
- A small number of providers account for disproportionately high paid per claim  

---

### Next Step: Financial Impact (Optional Extension)

While the IQR method identifies statistical outliers, the next analytical step is to measure:

> **Excess dollars = (provider paid per claim − median paid per claim) × total claims**

This allows prioritization of providers based not only on extremeness but also on **potential financial impact**.