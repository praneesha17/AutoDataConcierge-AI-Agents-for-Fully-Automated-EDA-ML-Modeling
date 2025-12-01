import os
from typing import Dict, Any

import pandas as pd


def ingest_dataset(dataset_ref: str, output_dir: str = "output") -> Dict[str, Any]:
    """
    Ingest a dataset given either:
    - a local CSV file path
    - a local folder containing a CSV
    - a Kaggle-style folder name (looked up under /kaggle/input/<name>)
    """
    os.makedirs(output_dir, exist_ok=True)

    csv_path = None

    # Kaggle-style folder
    kaggle_folder = os.path.join("/kaggle/input", dataset_ref)
    if os.path.isdir(kaggle_folder):
        for f in os.listdir(kaggle_folder):
            if f.lower().endswith(".csv"):
                csv_path = os.path.join(kaggle_folder, f)
                break

    # Local folder
    if csv_path is None and os.path.isdir(dataset_ref):
        for f in os.listdir(dataset_ref):
            if f.lower().endswith(".csv"):
                csv_path = os.path.join(dataset_ref, f)
                break

    # Direct CSV path
    if csv_path is None and os.path.isfile(dataset_ref) and dataset_ref.lower().endswith(".csv"):
        csv_path = dataset_ref

    if csv_path is None:
        raise FileNotFoundError(f"Could not locate a CSV for dataset_ref={dataset_ref!r}")

    df_sample = pd.read_csv(csv_path, nrows=500)

    return {
        "csv_path": csv_path,
        "sample_rows": int(df_sample.shape[0]),
        "sample_cols": int(df_sample.shape[1]),
        "sample_columns": df_sample.columns.tolist(),
    }
