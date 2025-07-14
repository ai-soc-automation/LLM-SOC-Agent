# ⚡ LLM‑SOC‑Agent

**AI‑Driven SOC Automation • MVP v0.0.1**

> "Classify each log, enrich it with threat‑intel context, and assign a triage priority — all in near‑real‑time."

## 📌 Project Goal
Build a lightweight, reproducible pipeline that proves LLMs can reduce SOC alert fatigue by automating log enrichment and priority scoring.

## 🛠 MVP Scope (Phase 1)
1. Ingest CIC‑IDS 2018 flows as CSV
2. Parse essentials (timestamp, src_ip, dst_port, label)
3. **LLM Prompt**: classify benign vs suspicious
4. Enrich suspicious logs with → IP reputation + ATT&CK technique
5. Output `triaged_logs.csv` with priority scores 1‑5

## 📚 Dataset
- **Source**: [CIC‑IDS 2018](https://www.unb.ca/cic/datasets/ids-2018.html)
- Download script: `scripts/download_cicids.py`
- Cleaned sample: `datasets/sample_logs.csv` (100 k rows)

## 🚀 Quick Start
```bash
pip install -r requirements.txt
python scripts/download_cicids.py --dest datasets/cicids2018
jupyter notebook notebooks/01_explore_cicids.ipynb