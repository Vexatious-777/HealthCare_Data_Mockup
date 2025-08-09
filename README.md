# Primary Care Performance Analysis

This is a compact, mock healthcare analytics project designed to demonstrate foundational data analysis skills relevant to an ACO or MSO setting.

**What you'll find**:
- `data.csv` — synthetic but realistic-looking healthcare visit records (de-identified)
- `analysis.ipynb` — Jupyter notebook that loads `data.csv`, computes provider KPIs, and generates `dashboard.png`
- `provider_summary.csv` — exported KPI summary for provider-level handoff
- `dashboard.png` — snapshot of the main visualizations

**Key analyses performed**:
- Provider attribution (unique patients per provider)
- Quality metric compliance rate (Met vs Not Met) by provider
- Visit type distribution (Annual/Follow-Up/ER/Telehealth)
- Top diagnoses frequency

**How to run**:
1. `pip install -r requirements.txt`
2. `jupyter notebook analysis.ipynb` (or open in VS Code / GitHub)
3. Re-run cells — the notebook will re-create `provider_summary.csv` and `dashboard.png`

**These Files can also be found on my GitHub**:
- `data.csv`
- `analysis.ipynb`
- `provider_summary.csv`
- `dashboard.png`
- `README.md`
- `requirements.txt`

**Skills demonstrated**: Python (Pandas), data aggregation, KPI calculation, matplotlib visualization, data export for business use.
