# AutoDataConcierge — Multi-Agent Data Science Pipeline

AutoDataConcierge is a multi-agent pipeline that automates:

- Dataset ingestion
- Exploratory Data Analysis (EDA)
- Feature analysis
- Baseline model training
- Best model selection
- Markdown report generation

It was originally built as a Kaggle × Google AI Agents Capstone project.

## Usage

```python
from agents.planner_agent import run_pipeline
result = run_pipeline("path/to/your.csv")
print(result["report_path"])
```

Outputs are saved under the `output/` directory.
