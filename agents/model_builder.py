import os
import json
from typing import Dict, Any

import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error


def _detect_target_column(df: pd.DataFrame) -> str:
    """
    Simple heuristic to pick a numeric target column.
    Prefer columns whose name includes 'point', 'score', or 'target'.
    Otherwise use the last numeric column.
    """
    numeric_cols = df.select_dtypes(include=["number"]).columns.tolist()
    if not numeric_cols:
        raise ValueError("No numeric columns available for target detection.")

    lowered = {c: c.lower() for c in numeric_cols}
    for col in numeric_cols:
        name = lowered[col]
        if "point" in name or "score" in name or "target" in name:
            return col

    return numeric_cols[-1]  # fallback


def run_models(csv_path: str, run_id: str, output_dir: str = "output") -> Dict[str, Any]:
    """
    Train simple regression models and return info about the best one.
    """
    df = pd.read_csv(csv_path).dropna()

    target_col = _detect_target_column(df)

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    models = {
        "linear_regression": LinearRegression(),
        "random_forest": RandomForestRegressor(n_estimators=100, random_state=42),
    }

    model_dir = os.path.join(output_dir, "models")
    os.makedirs(model_dir, exist_ok=True)

    results = []

    for name, model in models.items():
        model.fit(X_train, y_train)
        preds = model.predict(X_test)
        rmse = mean_squared_error(y_test, preds, squared=False)
        model_path = os.path.join(model_dir, f"{run_id}_{name}.joblib")
        joblib.dump(model, model_path)

        results.append({
            "model": name,
            "rmse": float(rmse),
            "model_path": model_path,
        })

    # Persist results
    results_path = os.path.join(model_dir, f"{run_id}_results.json")
    with open(results_path, "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2)

    # Pick best by RMSE
    best = min(results, key=lambda r: r["rmse"])
    return best
