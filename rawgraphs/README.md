# RAWGraphs Treemap — Market Research Analytics

**Email:** 23f3004246@ds.study.iitm.ac.in

This folder contains the dataset for creating a **Treemap** in RAWGraphs to visualize market share distribution across product categories and subcategories.

## Files
- `market_treemap.csv` — 15–20 rows with `category`, `subcategory`, and `value` columns (hierarchical data).

## How to Build the Treemap (RAWGraphs)
1. Open **https://rawgraphs.io/**
2. Click **Use It Now → Start with a Blank Chart** (or open RAWGraphs 2 online).
3. **Copy** the contents of `market_treemap.csv` and **Paste** into RAWGraphs.
4. Select **Treemap**.
5. Map fields:
   - **Hierarchy**: `category` → then `subcategory`
   - **Size**: `value`
   - **Color**: `category` (or `subcategory` for finer palette)
   - **Labels**: `subcategory` (and/or `value` as secondary label)
6. Customize:
   - Choose a professional palette (e.g., Tableau/Category10)
   - Enable labels and adjust font size for readability
7. **Export** as **PNG**, dimensions **300–512 px** (e.g., 512×512). Name it `chart.png`.

## Repository Checklist
- `README.md` (this file) — must include your email.
- `chart.png` — RAWGraphs Treemap (300–512 px).
- (Optional) `market_treemap.csv` — include for transparency.

## Raw URL Example
After uploading to GitHub (e.g., `Sudip-06/Week-7` under a folder like `rawgraphs/`), your raw README URL will be:
```
https://raw.githubusercontent.com/Sudip-06/Week-7/main/rawgraphs/README.md
```
