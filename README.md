# Receipts
Receipts is an NLP-driven political intelligence platform that extracts, structures, and evaluates campaign promises from large-scale unstructured text. It combines supervised classification, entity extraction, and probabilistic modeling to track promise fulfillment and surface accountability signals.

Problem

Political promises are often unstructured, scattered across speeches and media, and difficult to track longitudinally.

Receipts addresses:
- Lack of systematic promise tracking
- No standardized delivery scoring
- Limited structured comparison between politicians
- Poor visibility into fulfillment status


## System Overview

Receipts consists of:

1. **Promise Ingestion Layer**
   - Structured CSV ingestion (prototype)
   - Future: automated scraping + NLP extraction

2. **Scoring Engine**
   - Maps fulfillment status → weighted scores
   - Computes normalized delivery score per politician
   - Designed for extensibility to confidence-weighted evidence

3. **Lightweight NLP Module**
   - Detects numeric specificity in promises
   - Extracts quantitative targets (e.g., "build 50 schools")
   - Future: promise classification + entity linking

4. **Interactive Dashboard**
   - Streamlit-based visualization
   - Displays politician-level delivery scores
   - Built for rapid iteration and transparency

## 📊 Current Features

- Structured promise dataset
- Delivery scoring logic (Kept = 1, In Progress = 0.5, Broken = 0)
- Politician-level aggregation
- Interactive dashboard prototype
- Modular architecture for future ML integration


## Roadmap

Planned extensions include:

- Automated news ingestion pipeline
- Fulfillment evidence matching via NLP
- Confidence-weighted scoring
- Promise specificity scoring
- Historical trend visualization
- Model-based fulfillment likelihood estimation


## 🛠 Tech Stack

- Python
- Pandas
- Streamlit
- Modular scoring pipeline
- Lightweight NLP (regex-based prototype)


## ▶️ Run Locally

```bash
pip install -r requirements.txt
streamlit run dashboard.py
