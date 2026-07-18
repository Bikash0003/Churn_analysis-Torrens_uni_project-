# Power BI — Telco Churn Manager Dashboard

Manager-facing churn reporting pack for BDA601 Assessment 2.

## What’s included

| File | Description |
|------|-------------|
| `Telco_Churn_PowerBI_Model.xlsx` | **Main Power BI import** — Customers, KPIs, segment tables, action plan |
| `Telco_Churn_PowerBI.csv` | Flat customer table (risk scores, tenure bands, revenue at risk) |
| `Manager_Churn_Dashboard.html` | Ready-to-open interactive manager dashboard (browser) |
| `DAX_Measures.txt` | Copy-paste DAX for Power BI Desktop |
| `PowerBI_Dashboard_Guide.md` | 4-page report layout (Executive → Who churns → Drivers → Actions) |
| `How_to_create_PBIX.md` | Steps to save a best-practice `.pbix` in Power BI Desktop |

## Model metrics included for managers

- Accuracy ≈ **73.2%**
- Precision (Churn) ≈ **50%**
- Recall (Churn) ≈ **76%**
- F1-score ≈ **0.60**
- Confusion matrix counts + ROC-AUC ≈ **0.81**

## Quick start

1. Open `Manager_Churn_Dashboard.html` in a browser for the instant report.
2. In Power BI Desktop: **Get data → Excel** → `Telco_Churn_PowerBI_Model.xlsx` → follow `How_to_create_PBIX.md`.
