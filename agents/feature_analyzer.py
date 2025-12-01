from typing import Dict, Any, List

import pandas as pd


def analyze_features(csv_path: str) -> Dict[str, Any]:
    """
    Identify numeric/categorical columns, high-missing columns, and low-variance columns.
    """
    df = pd.read_csv(csv_path)

    numeric_cols: List[str] = df.select_dtypes(include=["number"]).columns.tolist()
    categorical_cols: List[str] = df.select_dtypes(exclude=["number"]).columns.tolist()

    missing_ratio = df.isna().mean()
    high_missing_cols = missing_ratio[missing_ratio > 0.5].index.tolist()

    low_variance_cols = []
    for col in numeric_cols:
        if df[col].nunique() <= 1:
            low_variance_cols.append(col)

    return {
        "numeric_columns": numeric_cols,
        "categorical_columns": categorical_cols,
        "high_missing_columns": high_missing_cols,
        "low_variance_columns": low_variance_cols,
    }
