# AutoDataConcierge-AI-Agents-for-Fully-Automated-EDA-ML-Modeling

**AutoDataConcierge** is a modular **multi-agent system** that automates
the early stages of data science for any CSV dataset.\
It was developed as part of the **Kaggle × Google AI Agents Intensive
Capstone (Nov 2025)**.

------------------------------------------------------------------------

## 🚀 Features

AutoDataConcierge automates the repetitive steps of a traditional data
science workflow:

-   Dataset ingestion
-   Exploratory Data Analysis (EDA)
-   Feature analysis
-   Baseline model training
-   Best model selection
-   Automated Markdown report generation

------------------------------------------------------------------------

## 🧠 Why Multi-Agent Architecture?

Each agent has a single responsibility, making the system modular and
extensible.

### Benefits

-   Modular & maintainable
-   Easy plug-and-play extensions
-   Debug-friendly
-   Fully automated pipeline

------------------------------------------------------------------------

## 🏗️ System Architecture

    dataset_ingestor
            ↓
         eda_analyzer
            ↓
      feature_analyzer
            ↓
        model_builder
            ↓
      report_generator

------------------------------------------------------------------------

## 🤖 Agent Responsibilities

### 1. DatasetIngestor

-   Loads CSV
-   Extracts metadata

### 2. EDAAnalyzer

-   Summaries
-   Missing values
-   Stats

### 3. FeatureAnalyzer

-   Column type detection
-   High-missing & low-variance flagging

### 4. ModelBuilder

-   Trains Linear Regression & Random Forest
-   Selects best RMSE model

### 5. ReportGenerator

-   Generates Markdown report

### 6. PlannerAgent

-   Coordinates workflow
-   Generates run ID

------------------------------------------------------------------------

## 📁 Project Structure

    AutoDataConcierge
    ├── agents
    ├── output
    ├── sample_run.ipynb
    ├── README.md
    └── requirements.txt

------------------------------------------------------------------------

## 📦 Installation

    pip install -r requirements.txt
    mkdir -p output/eda output/models

------------------------------------------------------------------------

## 🖥️ Usage

    from agents.planner_agent import run_pipeline
    result = run_pipeline("path/to/your.csv")
    print(result["report_path"])

------------------------------------------------------------------------

## 📜 Outputs

-   EDA JSON
-   Saved ML models
-   Model performance
-   Markdown report

