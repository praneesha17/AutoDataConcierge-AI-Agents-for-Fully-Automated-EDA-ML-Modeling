AutoDataConcierge — Multi-Agent Data Science Pipeline

AutoDataConcierge is a modular multi-agent system that automates the early stages of data science for any CSV dataset.

The pipeline performs:

Dataset ingestion

Exploratory Data Analysis (EDA)

Feature analysis

Baseline model training

Best model selection

Markdown report generation

This project was developed as part of the Kaggle × Google AI Agents Intensive Capstone (Nov 2025).

Project Goals

Traditional data science workflows require repetitive tasks:

reading datasets

checking missing values

summarizing statistics

selecting features

training first models

writing reports

AutoDataConcierge automates these steps end-to-end.
Instead of manually executing cells, you call one function.

Why Multi-Agent Architecture?

Instead of a single monolithic script, each part of the workflow is handled by a specialized agent.

One agent = one responsibility.

Benefits:

Maintainable

Modular

Reusable

Easy extension (plug-and-play)

The orchestrator (planner_agent) controls the entire pipeline.

System Overview
Agent flow
dataset_ingestor
    ↓
eda_analyzer
    ↓
feature_analyzer
    ↓
model_builder
    ↓
report_generator


All components are coordinated by the planner_agent.

Agent Responsibilities
1. DatasetIngestor

Finds the dataset (local CSV or Kaggle input folder)

Reads sample of the data

Extracts metadata

Output example:

csv_path
sample_rows
sample_columns

2. EDAAnalyzer

Runs dataset-wide EDA

Computes:

shape

column dtypes

missing values

numeric statistics

Saved to:

output/eda/<run_id>_eda.json

3. FeatureAnalyzer

Detects numeric/categorical columns

Identifies:

high-missing columns (>50%)

low-variance features

4. ModelBuilder

Trains baseline models:

Linear Regression

RandomForest

Evaluates performance (RMSE)

Selects best model

Saves artifacts:

output/models/<run_id>_*.joblib
output/models/<run_id>_results.json

5. ReportGenerator

Generates Markdown summarizing:

dataset metadata

EDA insights

feature summary

model performance

Saved to:

output/report_<run_id>.md

6. PlannerAgent

Generates unique run ID

Executes agents in sequence

Returns unified results object

Installation

Clone the project:

git clone https://github.com/<username>/AutoDataConcierge.git
cd AutoDataConcierge


Install dependencies:

pip install -r requirements.txt


Create output directories:

mkdir -p output/eda output/models

Usage

Minimal example:

from agents.planner_agent import run_pipeline

result = run_pipeline("path/to/your.csv")
print(result["report_path"])


You can then open the generated Markdown report in output/.

Project Structure
AutoDataConcierge/
│
├── agents/
│   ├── dataset_ingestor.py
│   ├── eda_analyzer.py
│   ├── feature_analyzer.py
│   ├── model_builder.py
│   ├── report_generator.py
│   └── planner_agent.py
│
├── output/
│   ├── eda/                # Automated EDA JSONs
│   ├── models/             # Stored ML models
│   └── report_<run_id>.md
│
├── sample_run.ipynb
├── README.md
└── requirements.txt

Dataset Example

Wine Reviews Dataset
https://www.kaggle.com/datasets/zynicide/wine-reviews

Do not upload this dataset to GitHub.
Link to Kaggle instead.

Requirements
pandas
numpy
scikit-learn
joblib

Outputs

The system produces:

EDA Summary

output/eda/<run_id>_eda.json


Trained models

output/models/<run_id>_random_forest.joblib
output/models/<run_id>_linear_regression.joblib


Model performance

output/models/<run_id>_results.json


Final report

output/report_<run_id>.md

Principles

One agent → one task

No manual steps

All artifacts persisted

Reproducible pipeline
