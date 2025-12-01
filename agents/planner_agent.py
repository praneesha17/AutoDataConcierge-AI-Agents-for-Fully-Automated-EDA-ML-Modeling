import uuid
from typing import Dict, Any

from agents.dataset_ingestor import ingest_dataset
from agents.eda_analyzer import analyze_eda
from agents.feature_analyzer import analyze_features
from agents.model_builder import run_models
from agents.report_generator import generate_report


def run_pipeline(dataset_ref: str, output_dir: str = "output") -> Dict[str, Any]:
    """
    Full pipeline orchestration:
    1) Ingest dataset
    2) Run EDA
    3) Analyze features
    4) Train models
    5) Generate report
    """
    run_id = str(uuid.uuid4())

    dataset_info = ingest_dataset(dataset_ref, output_dir=output_dir)
    csv_path = dataset_info["csv_path"]

    eda_summary = analyze_eda(csv_path, run_id=run_id, output_dir=output_dir)
    feature_summary = analyze_features(csv_path)
    best_model = run_models(csv_path, run_id=run_id, output_dir=output_dir)
    report_path = generate_report(
        run_id,
        dataset_info,
        eda_summary,
        feature_summary,
        best_model,
        output_dir=output_dir,
    )

    return {
        "run_id": run_id,
        "dataset_info": dataset_info,
        "eda_summary": eda_summary,
        "feature_summary": feature_summary,
        "best_model": best_model,
        "report_path": report_path,
    }
