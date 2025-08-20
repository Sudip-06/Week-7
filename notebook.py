
# Author: 23f3004246@ds.study.iitm.ac.in
# Marimo reactive notebook: Interactive correlation demo
# How data flows:
#   slider -> noise_level -> synthetic dataset (X, Y) -> correlation r -> markdown + plot
# Moving the slider recomputes all downstream cells automatically.

import marimo as mo

# === Cell 1: UI ===
# Interactive slider controls noise level in the synthetic data generator (0.00–2.00)
noise_slider = mo.ui.slider(start=0.0, stop=2.0, step=0.05, value=0.50, label="Noise level (σ)")
noise_slider

# === Cell 2: Data ===
# Depends on: noise_slider.value
# Produces: df (DataFrame with columns ['X','Y'])
import numpy as np
import pandas as pd

rng = np.random.default_rng(42)
n = 300
X = rng.normal(0, 1, size=n)
epsilon = rng.normal(0, noise_slider.value, size=n)  # <- dependency
Y = 2.5 * X + epsilon
df = pd.DataFrame({"X": X, "Y": Y})
df.head()

# === Cell 3: Analysis ===
# Depends on: df
# Produces: r (Pearson correlation between X and Y)
r = df["X"].corr(df["Y"])
r

# === Cell 4: Dynamic Markdown ===
# Depends on: noise_slider.value, r
strength = (
    "very strong" if abs(r) >= 0.8 else
    "strong" if abs(r) >= 0.6 else
    "moderate" if abs(r) >= 0.4 else
    "weak" if abs(r) >= 0.2 else
    "very weak"
)
mo.md(f"""
### 📊 Interactive Correlation Demo
- **Noise σ:** `{noise_slider.value:.2f}`  
- **Pearson r(X, Y):** `{r:.2f}` → **{strength}** linear relationship  
- Moving the slider **increases noise**, which **reduces correlation**.

> Data flow: `slider → noise → data → correlation → markdown/plot`.
""")

# === Cell 5: Visualization ===
# Depends on: df
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(5, 4))
ax.scatter(df["X"], df["Y"], alpha=0.6, edgecolor="none")
ax.set_title(f"Scatter of Y vs X  |  r = {r:.2f}")
ax.set_xlabel("X")
ax.set_ylabel("Y")
fig
