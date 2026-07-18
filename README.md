# Telco Customer Churn Analysis (BDA601)

Torrens University — **BDA601 Big Data and Analytics**, Assessment 2: Visualisation and Model Development.

## Original dataset

Full IBM Telco Customer Churn sample on Kaggle (**7,043 rows × 21 columns**):

https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data

## What’s in this repository

| File | Description |
|------|-------------|
| `telco_churn_modified.csv` | **Modified dataset** used for modelling (7,043 × 16). Removed per brief: `MonthlyCharges`, `OnlineSecurity`, `StreamingTV`, `InternetService`, `Partner`. |
| `BDA601_Assessment2_Churn_Prediction.ipynb` | Jupyter notebook: data prep, EDA, cleaning, feature selection, decision-tree churn model. |
| `BDA601_Assessment2_Report.pdf` | Assessment report (~1,000 words): missing-value strategy and churn interpretation. |
| `requirements.txt` | Python packages needed to run the notebook. |

## How to run

```bash
pip install -r requirements.txt
jupyter notebook BDA601_Assessment2_Churn_Prediction.ipynb
```

The notebook can also re-download the original Kaggle data and rebuild the modified CSV.

## Power BI manager dashboard

See the powerbi/ folder for the manager reporting pack:

- powerbi/Manager_Churn_Dashboard.html — open in browser
- powerbi/Telco_Churn_PowerBI_Model.xlsx — import into Power BI Desktop to create .pbix
- Includes Accuracy, Precision, Recall, F1, and Confusion Matrix for leadership review

