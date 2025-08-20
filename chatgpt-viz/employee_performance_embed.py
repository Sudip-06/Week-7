# Author: 23f3004246@ds.study.iitm.ac.in
# Task: Employee Performance Analysis Visualization (HTML with embedded code)

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter
from pathlib import Path
import base64, io, html

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

# --- Histogram (categorical -> bar chart of counts) ---
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

# Save plot to PNG (in-memory) for embedding
buf = io.BytesIO()
fig.savefig(buf, format="png", dpi=100, bbox_inches="tight")
plt.close(fig)
png_b64 = base64.b64encode(buf.getvalue()).decode("ascii")

# --- Build HTML with chart + Python code ---
html_doc = f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Employee Performance — Department Distribution</title>
  <style>
    body {{ font-family: system-ui, -apple-system, Segoe UI, Roboto, Arial, sans-serif; margin: 24px; }}
    .meta {{ color: #555; margin-bottom: 16px; }}
    .card {{ border: 1px solid #ddd; border-radius: 8px; padding: 16px; max-width: 900px; }}
    img {{ max-width: 100%; height: auto; display: block; }}
    pre {{ background: #f6f8fa; padding: 12px; border-radius: 6px; overflow-x: auto; }}
  </style>
</head>
<body>
  <h1>Employee Distribution by Department</h1>
  <div class="meta">Author: 23f3004246@ds.study.iitm.ac.in</div>
  <div class="card">
    <p><strong>Number of employees in Operations:</strong> {ops_count}</p>
    <img alt="Histogram of departments" src="data:image/png;base64,{png_b64}" />
  </div>

  <h2>Python Code</h2>
  <pre><code>{{code}}</code></pre>
</body>
</html>
"""

# Escape the code for safe HTML embedding
escaped_code = html.escape(open(__file__, "r", encoding="utf-8").read()) if "__file__" in globals() else html.escape(code_str)

# Write final HTML
Path("employee_performance.html").write_text(html_doc.replace("{code}", escaped_code), encoding="utf-8")
print("employee_performance.html created with embedded code and chart.")
