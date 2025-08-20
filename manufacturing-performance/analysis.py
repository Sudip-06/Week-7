# Author: 23f3004246@ds.study.iitm.ac.in
# Manufacturing Performance Analysis — Data Story with Visualizations
# Requirements: pandas, matplotlib

import pandas as pd
import matplotlib.pyplot as plt

# Data
df = pd.DataFrame({"Quarter": ["Q1-2024", "Q2-2024", "Q3-2024", "Q4-2024"], "Efficiency": [71.5, 71.53, 74.1, 75.52]})
target = 90.0

# Compute average and print
avg = df["Efficiency"].mean()
print(f"Average efficiency in 2024: {avg:.2f}")

# Trend vs target
plt.figure(figsize=(8, 5))
plt.plot(df["Quarter"], df["Efficiency"], marker="o", linewidth=2)
plt.axhline(target, linestyle="--")
plt.title("Equipment Efficiency Rate — 2024 vs Industry Target")
plt.xlabel("Quarter")
plt.ylabel("Efficiency Rate")
for x, y in zip(df["Quarter"], df["Efficiency"]):
    plt.text(x, y + 0.4, f"{y:.2f}", ha="center", va="bottom")
plt.text(df["Quarter"].iloc[-1], target + 0.6, "Target 90", ha="left")
plt.tight_layout()
plt.savefig("figures/trend_vs_target.png", dpi=150)
plt.close()

# Shortfall bars
shortfall = [target - v for v in df["Efficiency"]]
plt.figure(figsize=(8, 5))
bars = plt.bar(df["Quarter"], shortfall)
plt.title("Shortfall from Target by Quarter (90 − Efficiency)")
plt.xlabel("Quarter")
plt.ylabel("Points Below Target")
for rect, s in zip(bars, shortfall):
    plt.text(rect.get_x() + rect.get_width()/2, rect.get_height() + 0.5, f"{s:.2f}", ha="center", va="bottom")
plt.tight_layout()
plt.savefig("figures/shortfall_by_quarter.png", dpi=150)
plt.close()
