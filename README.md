# Churn Analysis — Torrens University (BDA601 Assessment 2)

Telco customer churn prediction for **BDA601 Big Data and Analytics** (Torrens University).

## Dataset

- **Source:** [Kaggle — Telco Customer Churn (IBM sample)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn/data)
- **Full extract:** 7,043 rows × 21 columns
- **A2 modified file:** 7,043 rows × 16 columns  
  Removed: `MonthlyCharges`, `OnlineSecurity`, `StreamingTV`, `InternetService`, `Partner`

## Project structure

```
data/raw/Telco-Customer-Churn.csv          # full 21-column extract
data/processed/telco_churn_modified.csv    # A2 Task 1 modified data
telco_churn_modified.csv                   # submission copy
BDA601_Assessment2_Churn_Prediction.ipynb  # analysis notebook
BDA601_Assessment2_Report.pdf              # ~1000-word report
scripts/download_and_prepare_data.py       # download + modify helper
```

## Quick start

```bash
pip install -r requirements.txt
python scripts/download_and_prepare_data.py
jupyter notebook BDA601_Assessment2_Churn_Prediction.ipynb
```

Optional (direct Kaggle API download): place `kaggle.json` in `~/.kaggle/`.  
Without Kaggle credentials the script uses the public IBM mirror of the same sample.

## Model

Decision Tree Classifier (scikit-learn) with stratified train/validation/test split.  
Top driver in this run: **Contract** (followed by tenure / TechSupport).
