# Author: 23f3004246@ds.study.iitm.ac.in
# Task: Employee Performance Analysis Visualization

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
import base64, io

# --- Synthetic dataset (100 rows) ---
data = {
    "EmployeeID": list(range(1, 101)),
    "Department": (
        ["Operations", "HR", "Finance", "IT", "Sales",
         "Operations", "Operations", "Finance", "Sales", "HR"] * 10
    ),
    "Region": (["North", "South", "East", "West"] * 25),
    "PerformanceScore": [float(60 + i) for i in range(100)]
}
df = pd.DataFrame(data)

# --- Frequency count for Operations ---
ops_count = (df["Department"] == "Operations").sum()
print(f"Number of employees in Operations: {ops_count}")

# --- Histogram ---
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

# Save to PNG (in-memory) for embedding
buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=100, bbox_inches="tight")
plt.close(fig)
png_b64 = base64.b64encode(buf.getvalue()).decode("ascii")

# --- Build HTML with chart + Python code ---
html = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <title>Employee Performance Analysis</title>
  <style>
    body {{ font-family: Arial, sans-serif; margin: 24px; }}
    pre {{ background: #f6f8fa; padding: 12px; border-radius: 6px; }}
    img {{ max-width: 100%; height: auto; }}
  </style>
</head>
<body>
  <h1>Employee Distribution by Department</h1>
  <p><strong>Number of employees in Operations:</strong> {ops_count}</p>
  <img alt="Histogram" src="data:image/png;base64,{png_b64}" />

  <h2>Python Code</h2>
  <pre><code>{Path(__file__).read_text()}</code></pre>
</body>
</html>
"""

Path("employee_performance.html").write_text(html, encoding="utf-8")
print("employee_performance.html created with embedded code and chart.")
