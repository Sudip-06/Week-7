# Author: 23f3004246@ds.study.iitm.ac.in
# Task: Employee Performance Analysis Visualization

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# --- Step 1: Generate synthetic dataset ---
data = {
    "EmployeeID": range(1, 101),
    "Department": [
        "Operations", "HR", "Finance", "IT", "Sales", "Operations", "Operations",
        "Finance", "Sales", "HR"
    ] * 10,  # repeats to make 100 rows
    "Region": ["North", "South", "East", "West"] * 25,
    "PerformanceScore": [round(x, 1) for x in list(range(60, 160))]  # dummy scores
}

df = pd.DataFrame(data)

# --- Step 2: Frequency count for Operations ---
ops_count = (df["Department"] == "Operations").sum()
print(f"Number of employees in Operations: {ops_count}")

# --- Step 3: Visualization ---
plt.figure(figsize=(8, 6))
sns.set_style("whitegrid")
ax = sns.histplot(df["Department"], discrete=True, shrink=0.8, palette="Set2")

plt.title("Employee Distribution by Department", fontsize=16, weight="bold")
plt.xlabel("Department")
plt.ylabel("Count")

# Save as HTML using mpld3
import mpld3
html_path = "employee_performance.html"
mpld3.save_html(ax.figure, html_path)

print(f"Visualization saved to {html_path}")
