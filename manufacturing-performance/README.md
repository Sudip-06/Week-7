# Manufacturing Performance Analysis — 2024

**Author (verification): 23f3004246@ds.study.iitm.ac.in**

This PR provides a data-driven story about equipment efficiency for 2024 and concrete actions to close the gap to the industry target.

## Executive Summary

- **Average 2024 efficiency:** **73.16** (required value)  
- **Industry target:** **90**
- **Gap to target (avg):** **16.84** points
- **Trend:** Improving quarter-over-quarter (71.5 → 75.52) but still below target.

> **Recommendation:** Implement a **predictive maintenance program** to reduce unplanned downtime, stabilize quality, and raise OEE toward the target of 90.

## Data

| Quarter | Efficiency |
|--------:|-----------:|
| Q1-2024 | 71.50 |
| Q2-2024 | 71.53 |
| Q3-2024 | 74.10 |
| Q4-2024 | 75.52 |
| **Average** | **73.16** |

## Visualizations

- `figures/trend_vs_target.png` — Trend vs target line (90)
- `figures/shortfall_by_quarter.png` — Shortfall to target by quarter

## Key Findings

1. **Consistent shortfall:** Average efficiency **73.16** vs target **90**.  
2. **Positive trajectory:** +4.02 points from Q1 (71.50) to Q4 (75.52).  
3. **Shortfall still material:** Ending the year **14.48** points below target.

## Business Implications

- The current shortfall implies **excess downtime**, **higher scrap/rework**, and **missed throughput**.  
- Without intervention, the organization risks **higher cost per unit** and **late orders**.

## Recommendations (Roadmap to 90)

**Primary solution: _Implement a Predictive Maintenance Program_.**

1. **Data & Sensors**
   - Instrument critical assets with vibration, temperature, and current sensors.
   - Centralize telemetry in a historian/warehouse for model training.

2. **Modeling**
   - Build failure-prediction models (survival analysis + anomaly detection).
   - Prioritize assets by **risk × impact**; deploy alerts with lead time ≥ 1 week.

3. **Workflows**
   - Auto-create planned work orders in CMMS upon high-risk alerts.
   - Standardize root-cause tagging to improve continuous learning.

4. **KPIs & Targets**
   - Reduce unplanned downtime by **30–40%** in 2–3 quarters.
   - Lift efficiency by **~12–15 points** to close the gap to **90**.

## Reproducibility

- Code: `analysis.py` (Python 3, `pandas`, `matplotlib`)
- Figures: in `figures/`
- To run locally:
  ```bash
  python analysis.py
  ```

## LLM Assistance

Portions of this analysis (code scaffolding, narrative structuring) were created with an LLM.  
Include this note in the PR description to show LLM assistance (e.g., **Jules / ChatGPT Codex**).

