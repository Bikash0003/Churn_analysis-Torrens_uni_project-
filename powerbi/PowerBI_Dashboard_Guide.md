# Power BI Manager Dashboard — Build Guide

Use this guide in **Power BI Desktop** to create a leadership-ready churn report from the files in this folder.

## Files to use

| File | Purpose |
|------|---------|
| `Telco_Churn_PowerBI_Model.xlsx` | Best import source (Customers + summary sheets + actions) |
| `Telco_Churn_PowerBI.csv` | Single flat table alternative |
| `Manager_Churn_Dashboard.html` | Instant browser preview of the same story |
| `DAX_Measures.txt` | Copy-paste measures |

## Recommended report pages

### Page 1 — Executive Summary
**Audience:** Manager / leadership (30-second story)

Visuals:
1. **KPI cards:** Total Customers, Churn Rate %, Churned Customers, Est. Monthly Revenue at Risk
2. **Donut:** CustomerStatus (Churned vs Retained)
3. **Bar:** Churn Rate by Contract
4. **Card / callout text:** “Contract is the #1 churn driver; focus saves on month-to-month + new customers.”

Filters (slicers): Contract, TenureBand, RiskSegment

### Page 2 — Who Is Churning
Visuals:
1. Clustered bar: Churn Rate by TenureBand
2. Clustered bar: Churn Rate by PaymentMethod
3. Clustered bar: Churn Rate by TechSupport
4. Matrix: Contract × TenureBand with Churn Rate %
5. Table: top risky segments (RiskSegment, Customers, ChurnRatePct, RevenueAtRisk)

### Page 3 — Drivers & Model Trust
Visuals:
1. KPI cards: Model Accuracy 73.2%, Churn Recall 76%, ROC-AUC 0.81
2. Bullet / text: Top driver = Contract
3. Bar: RiskSegment churn rates
4. Scatter (optional): tenure vs TotalCharges, legend = CustomerStatus

### Page 4 — Retention Action Plan
Visuals:
1. Table from sheet `Manager_Actions` (Priority, Segment, RecommendedAction, Owner)
2. Bar: Revenue at Risk by Contract
3. Card: High-Risk customer count + churn rate

## Import steps (Power BI Desktop)

1. Open Power BI Desktop → **Get data** → **Excel workbook**
2. Select `Telco_Churn_PowerBI_Model.xlsx`
3. Tick at least: `Customers`, `KPI_Summary`, `Manager_Actions` (optional: other By_* sheets)
4. **Load**
5. In **Report view**, build Page 1–4 using the visuals above
6. Create measures from `DAX_Measures.txt` on the `Customers` table
7. File → **Save as** → `Telco_Churn_Manager_Dashboard.pbix`

## Design tips for managers

- Keep Page 1 sparse: 4 KPIs + 2 charts + 1 insight sentence
- Use red/orange only for churn / high risk; green for retained / low risk
- Always show **% churn** and **customer count** together
- End with actions and owners (Page 4), not only charts
