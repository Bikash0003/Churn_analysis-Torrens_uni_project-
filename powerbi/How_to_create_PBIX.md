# How to create the best `.pbix` report (Power BI Desktop)

A binary `.pbix` file can only be saved from **Power BI Desktop**. This folder gives you the complete data model, DAX, and layout so you can produce a high-quality manager report in minutes.

## Steps

1. Install / open **Power BI Desktop**.
2. **Home → Get data → Excel workbook**.
3. Select `Telco_Churn_PowerBI_Model.xlsx`.
4. Select sheets: `Customers`, `KPI_Summary`, `Manager_Actions`, `By_Contract`, `By_PaymentMethod`, `By_TechSupport`, `By_TenureBand`, `By_RiskSegment`.
5. **Load**.
6. Open **Model view** and hide helper columns if needed (`ChurnFlag` can stay for measures).
7. Create measures from `DAX_Measures.txt` on the `Customers` table.
8. Build **4 pages** exactly as in `PowerBI_Dashboard_Guide.md`:
   - Page 1 Executive Summary
   - Page 2 Who Is Churning
   - Page 3 Drivers & Model Trust (include Accuracy / Precision / Recall / F1 / Confusion Matrix KPIs)
   - Page 4 Retention Action Plan
9. Add slicers: `Contract`, `TenureBand`, `RiskSegment`, `PaymentMethod`.
10. **File → Save as** → `Telco_Churn_Manager_Dashboard.pbix`.
11. Optional: **Publish** to Power BI Service for sharing with managers.

## Theme tips

- Title every page with an action insight (e.g. “Month-to-month + new customers drive most churn”).
- Put KPI cards on a single top row.
- Use red for churn / high risk; green for retained / low risk.
- Keep Page 1 under 6 visuals.

## Already available without Power BI Desktop

Open `Manager_Churn_Dashboard.html` — same executive story, charts, metrics, and action plan.
