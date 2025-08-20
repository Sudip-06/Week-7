# Author: 23f3004246@ds.study.iitm.ac.in
# Task: Employee Performance Analysis Visualization (HTML export with embedded PNG)

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
import base64, io

# Synthetic dataset (100 rows)
data = {'EmployeeID': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100], 'Department': ['Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR', 'Operations', 'HR', 'Finance', 'IT', 'Sales', 'Operations', 'Operations', 'Finance', 'Sales', 'HR'], 'Region': ['North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West', 'North', 'South', 'East', 'West'], 'PerformanceScore': [60.0, 61.0, 62.0, 63.0, 64.0, 65.0, 66.0, 67.0, 68.0, 69.0, 70.0, 71.0, 72.0, 73.0, 74.0, 75.0, 76.0, 77.0, 78.0, 79.0, 80.0, 81.0, 82.0, 83.0, 84.0, 85.0, 86.0, 87.0, 88.0, 89.0, 90.0, 91.0, 92.0, 93.0, 94.0, 95.0, 96.0, 97.0, 98.0, 99.0, 100.0, 101.0, 102.0, 103.0, 104.0, 105.0, 106.0, 107.0, 108.0, 109.0, 110.0, 111.0, 112.0, 113.0, 114.0, 115.0, 116.0, 117.0, 118.0, 119.0, 120.0, 121.0, 122.0, 123.0, 124.0, 125.0, 126.0, 127.0, 128.0, 129.0, 130.0, 131.0, 132.0, 133.0, 134.0, 135.0, 136.0, 137.0, 138.0, 139.0, 140.0, 141.0, 142.0, 143.0, 144.0, 145.0, 146.0, 147.0, 148.0, 149.0, 150.0, 151.0, 152.0, 153.0, 154.0, 155.0, 156.0, 157.0, 158.0, 159.0]}
df = pd.DataFrame(data)

# Frequency count for Operations
ops_count = (df["Department"] == "Operations").sum()
print(f"Number of employees in Operations: {ops_count}")

# Histogram of departments (categorical -> bar chart)
counts = Counter(df["Department"])
labels = sorted(counts.keys())
values = [counts[k] for k in labels]

fig = plt.figure(figsize=(8, 6))
ax = fig.add_subplot(111)
ax.bar(labels, values)
ax.set_title("Employee Distribution by Department")
ax.set_xlabel("Department")
ax.set_ylabel("Count")
fig.tight_layout()

buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=100, bbox_inches="tight")
plt.close(fig)
png_b64 = base64.b64encode(buf.getvalue()).decode("ascii")

html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Employee Performance — Department Distribution</title>
  <style>
    body { font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }
    .meta { color: #555; margin-bottom: 16px; }
    .card { border: 1px solid #ddd; border-radius: 8px; padding: 16px; max-width: 900px; }
    img { max-width: 100%; height: auto; display: block; }
  </style>
</head>
<body>
  <h1>Employee Distribution by Department</h1>
  <div class="meta">Author: 23f3004246@ds.study.iitm.ac.in</div>
  <div class="card">
    <p><strong>Number of employees in Operations:</strong> {ops_count}</p>
    <img alt="Histogram of departments" src="data:image/png;base64,{png_b64}" />
    <p>This visualization shows the count of employees in each department.</p>
  </div>
</body>
</html>
"""

Path("employee_performance.html").write_text(html, encoding="utf-8")
print("Visualization saved to employee_performance.html")
