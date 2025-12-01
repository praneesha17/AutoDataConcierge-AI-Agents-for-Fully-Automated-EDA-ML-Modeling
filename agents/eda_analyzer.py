import os
import json
from typing import Dict, Any

import pandas as pd


def analyze_eda(csv_path: str, run_id: str, output_dir: str = "output") -> Dict[str, Any]:
    """
    Perform simple EDA on the dataset and save a JSON summary.
    """
    df = pd.read_csv(csv_path)

    summary: Dict[str, Any] = {}
    summary["shape"] = tuple(df.shape)
    summary["columns"] = df.columns.tolist()
    summary["dtypes"] = df.dtypes.astype(str).to_dict()
    summary["missing_values"] = df.isna().sum().to_dict()

    numeric_df = df.select_dtypes(include=["number"])
    if not numeric_df.empty:
        summary["numeric_summary"] = numeric_df.describe().to_dict()
    else:
        summary["numeric_summary"] = {}

    eda_dir = os.path.join(output_dir, "eda")
    os.makedirs(eda_dir, exist_ok=True)
    out_path = os.path.join(eda_dir, f"{run_id}_eda.json")
    with open(out_path, "w", encoding="utf-8") as f:
        json.dump(summary, f, indent=2)

    return summary
