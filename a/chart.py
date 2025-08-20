import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Synthetic customer satisfaction data
data = {
    "Category": [
        "Electronics", "Clothing", "Home & Kitchen",
        "Sports", "Toys", "Beauty", "Grocery"
    ],
    "Satisfaction": [8.2, 7.5, 8.7, 7.9, 7.3, 8.0, 8.4]
}
df = pd.DataFrame(data)

# Professional styling
sns.set_style("whitegrid")
sns.set_context("talk")
palette = sns.color_palette("Set2")

# Create barplot
plt.figure(figsize=(8, 8))
ax = sns.barplot(
    x="Category",
    y="Satisfaction",
    data=df,
    palette=palette
)
ax.set_title("Average Customer Satisfaction by Product Category", fontsize=16, weight="bold")
ax.set_xlabel("Product Category", fontsize=12)
ax.set_ylabel("Satisfaction Score (1–10)", fontsize=12)
plt.xticks(rotation=30, ha="right")

# Save chart as 512x512 px
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
