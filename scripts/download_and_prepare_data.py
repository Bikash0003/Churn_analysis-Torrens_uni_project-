"""
Download the full IBM/Kaggle Telco Customer Churn dataset (7,043 x 21),
then produce the Assessment-2 modified dataset (7,043 x 16).

Primary source: Kaggle dataset blastchar/telco-customer-churn
Fallback: IBM public mirror of the same sample (identical schema/rows).
"""
from __future__ import annotations

import io
import zipfile
from pathlib import Path

import pandas as pd
import urllib.request

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROC_DIR = ROOT / "data" / "processed"
RAW_CSV = RAW_DIR / "Telco-Customer-Churn.csv"
MODIFIED_CSV = PROC_DIR / "telco_churn_modified.csv"
# Also keep a copy at project root for notebook convenience / submission
MODIFIED_ROOT = ROOT / "telco_churn_modified.csv"

KAGGLE_DATASET = "blastchar/telco-customer-churn"
IBM_MIRROR_URL = (
    "https://raw.githubusercontent.com/IBM/telco-customer-churn-on-icp4d/"
    "master/data/Telco-Customer-Churn.csv"
)

DROP_COLS = [
    "MonthlyCharges",
    "OnlineSecurity",
    "StreamingTV",
    "InternetService",
    "Partner",
]


def try_kaggle_download(dest: Path) -> bool:
    """Download from Kaggle via kagglehub (preferred) or classic Kaggle API."""
    RAW_DIR.mkdir(parents=True, exist_ok=True)

    # 1) kagglehub (works with browser/login cache on many machines)
    try:
        import kagglehub
        import shutil

        cache_path = Path(kagglehub.dataset_download(KAGGLE_DATASET))
        candidates = list(cache_path.rglob("*.csv"))
        if candidates:
            preferred = next(
                (
                    c
                    for c in candidates
                    if "Telco" in c.name or "WA_Fn" in c.name or "telco" in c.name.lower()
                ),
                candidates[0],
            )
            shutil.copy2(preferred, dest)
            print(f"Downloaded via kagglehub: {KAGGLE_DATASET} -> {dest}")
            return True
    except Exception as exc:
        print(f"kagglehub download failed ({exc}); trying classic Kaggle API...")

    # 2) classic Kaggle API (needs ~/.kaggle/kaggle.json)
    try:
        from kaggle.api.kaggle_api_extended import KaggleApi

        api = KaggleApi()
        api.authenticate()
        api.dataset_download_files(KAGGLE_DATASET, path=str(RAW_DIR), unzip=True)
        candidates = list(RAW_DIR.glob("*.csv"))
        if not candidates:
            return False
        preferred = next(
            (
                c
                for c in candidates
                if "Telco" in c.name or "telco" in c.name.lower() or "WA_Fn" in c.name
            ),
            candidates[0],
        )
        if preferred.resolve() != dest.resolve():
            dest.write_bytes(preferred.read_bytes())
        print(f"Downloaded from Kaggle API: {KAGGLE_DATASET} -> {dest}")
        return dest.exists()
    except Exception as exc:
        print(f"Kaggle API download failed ({exc}); will use IBM mirror fallback.")
        return False


def download_ibm_mirror(dest: Path) -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Downloading IBM mirror (same Kaggle/IBM sample):\n  {IBM_MIRROR_URL}")
    urllib.request.urlretrieve(IBM_MIRROR_URL, dest)
    print(f"Saved raw dataset -> {dest}")


def prepare_modified(raw_path: Path) -> pd.DataFrame:
    df = pd.read_csv(raw_path)
    if df.shape != (7043, 21):
        raise ValueError(f"Expected shape (7043, 21), got {df.shape}")
    missing = [c for c in DROP_COLS if c not in df.columns]
    if missing:
        raise ValueError(f"Missing columns to drop: {missing}")

    modified = df.drop(columns=DROP_COLS)
    if modified.shape != (7043, 16):
        raise ValueError(f"Expected modified shape (7043, 16), got {modified.shape}")

    PROC_DIR.mkdir(parents=True, exist_ok=True)
    modified.to_csv(MODIFIED_CSV, index=False)
    modified.to_csv(MODIFIED_ROOT, index=False)
    print(f"Modified dataset (A2 Task 1) saved -> {MODIFIED_CSV}")
    print(f"Also copied to -> {MODIFIED_ROOT}")
    print(f"Columns retained ({len(modified.columns)}): {list(modified.columns)}")
    return modified


def main() -> None:
    RAW_DIR.mkdir(parents=True, exist_ok=True)
    if not RAW_CSV.exists():
        ok = try_kaggle_download(RAW_CSV)
        if not ok:
            download_ibm_mirror(RAW_CSV)
    else:
        print(f"Raw file already present: {RAW_CSV}")

    df_raw = pd.read_csv(RAW_CSV)
    print(f"Raw shape: {df_raw.shape}")
    print(f"Raw columns: {list(df_raw.columns)}")
    prepare_modified(RAW_CSV)


if __name__ == "__main__":
    main()
