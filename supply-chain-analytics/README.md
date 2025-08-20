# Supply Chain Analytics — Correlation Heatmap

Contact: **23f3004246@ds.study.iitm.ac.in**

This folder contains:
- `correlation.csv` — 5×5 correlation matrix (Supplier_Lead_Time, Inventory_Levels, Order_Frequency, Delivery_Performance, Cost_Per_Unit)
- `heatmap.png` — Excel-style correlation heatmap using Red–White–Green color scale (size 500×500 px)

## How this was created
1. **Enable ToolPak:** File → Options → Add-ins → *Analysis ToolPak* ✔
2. **Correlation:** Data → Data Analysis → *Correlation*  
   - Input range: the 5 numeric columns (labels in first row ✔)  
   - Grouped by **Columns**, Output to new worksheet
3. **Heatmap:** Select correlation cells → Home → Conditional Formatting → Color Scales → **Red–White–Green**  
   - Take a **400–512 px** screenshot → save as `heatmap.png`
4. **CSV:** Copy correlation values (with labels in the first row/column) → save as `correlation.csv`

## Validation checklist
- [x] `README.md` includes email
- [x] `correlation.csv` present and numeric
- [x] `heatmap.png` Red–White–Green, 400–512 px
