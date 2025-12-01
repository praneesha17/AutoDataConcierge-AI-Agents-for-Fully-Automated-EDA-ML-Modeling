import os
from typing import Dict, Any


def generate_report(
    run_id: str,
    dataset_info: Dict[str, Any],
    eda_summary: Dict[str, Any],
    feature_summary: Dict[str, Any],
    best_model: Dict[str, Any],
    output_dir: str = "output",
) -> str:
    """
    Generate a simple Markdown report summarizing the run.
    """
    os.makedirs(output_dir, exist_ok=True)
    report_path = os.path.join(output_dir, f"report_{run_id}.md")

    lines = []
    lines.append(f"# AutoDataConcierge Report")
    lines.append("")
    lines.append(f"**Run ID:** `{run_id}`")
    lines.append("")
    lines.append("## Dataset")
    lines.append(f"- CSV Path: `{dataset_info['csv_path']}`")
    lines.append(f"- Sample Rows: {dataset_info['sample_rows']}")
    lines.append(f"- Sample Columns: {dataset_info['sample_cols']}")
    lines.append(f"- Sample Columns List: {', '.join(dataset_info['sample_columns'])}")
    lines.append("")
    lines.append("## EDA Summary")
    shape = eda_summary.get("shape", None)
    if shape:
        lines.append(f"- Shape: {shape[0]} rows × {shape[1]} columns")
    lines.append(f"- Missing Values (per column):")
    for col, mv in eda_summary.get("missing_values", {}).items():
        lines.append(f"  - {col}: {mv}")
    lines.append("")
    lines.append("## Feature Summary")
    lines.append(f"- Numeric Columns: {feature_summary.get('numeric_columns', [])}")
    lines.append(f"- Categorical Columns: {feature_summary.get('categorical_columns', [])}")
    lines.append(f"- High Missing Columns: {feature_summary.get('high_missing_columns', [])}")
    lines.append(f"- Low Variance Columns: {feature_summary.get('low_variance_columns', [])}")
    lines.append("")
    lines.append("## Best Model")
    lines.append(f"- Name: {best_model.get('model')}")
    lines.append(f"- RMSE: {best_model.get('rmse')}")
    lines.append(f"- Saved At: `{best_model.get('model_path')}`")
    lines.append("")
    lines.append("---")
    lines.append("Generated automatically by AutoDataConcierge.")

    with open(report_path, "w", encoding="utf-8") as f:
        f.write("\n".join(lines))

    return report_path
