import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px

# -----------------------------
# 1. Load dataset
# -----------------------------
df = pd.read_csv("master_dataset.csv")

# -----------------------------
# 2. Basic setup
# -----------------------------
sns.set(style="whitegrid")
plt.rcParams["figure.figsize"] = (10, 6)

# -----------------------------
# 3. Scatter Plot: Commute vs Unemployment
# -----------------------------
plt.figure()
sns.regplot(
    data=df,
    x="Commute_Time",
    y="Unemployment_Rate",
    scatter_kws={"alpha": 0.7},
    line_kws={"color": "red"}
)
plt.title("Commute Time vs Unemployment Rate")
plt.xlabel("Average Commute Time (Minutes)")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("commute_vs_unemployment.png")
plt.show()

# -----------------------------
# 4. Scatter Plot: Transit vs Unemployment
# -----------------------------
plt.figure()
sns.regplot(
    data=df,
    x="Percent_Public_Transit",
    y="Unemployment_Rate",
    scatter_kws={"alpha": 0.7},
    line_kws={"color": "red"}
)
plt.title("Public Transit Usage vs Unemployment Rate")
plt.xlabel("Public Transit Usage (%)")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("transit_vs_unemployment.png")
plt.show()

# -----------------------------
# 5. Scatter Plot: Transportation Score vs Unemployment
# -----------------------------
plt.figure()
sns.regplot(
    data=df,
    x="Transportation_Score",
    y="Unemployment_Rate",
    scatter_kws={"alpha": 0.7},
    line_kws={"color": "red"}
)
plt.title("Transportation Score vs Unemployment Rate")
plt.xlabel("Transportation Score")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("score_vs_unemployment.png")
plt.show()

# -----------------------------
# 6. Income vs Unemployment (Control Variable)
# -----------------------------
plt.figure()
sns.regplot(
    data=df,
    x="Median_Income",
    y="Unemployment_Rate",
    scatter_kws={"alpha": 0.7},
    line_kws={"color": "red"}
)
plt.title("Median Income vs Unemployment Rate")
plt.xlabel("Median Income ($)")
plt.ylabel("Unemployment Rate (%)")
plt.tight_layout()
plt.savefig("income_vs_unemployment.png")
plt.show()

# -----------------------------
# 7. Distribution of Unemployment
# -----------------------------
plt.figure()
sns.histplot(df["Unemployment_Rate"], bins=10, kde=True)
plt.title("Distribution of Unemployment Rates")
plt.xlabel("Unemployment Rate (%)")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("unemployment_distribution.png")
plt.show()

# -----------------------------
# 8. Interactive Plot (Plotly)
# -----------------------------
fig = px.scatter(
    df,
    x="Commute_Time",
    y="Unemployment_Rate",
    size="Median_Income",
    hover_name="ZIP",
    title="Interactive: Commute Time vs Unemployment"
)

fig.write_html("interactive_commute_plot.html")
fig.show()