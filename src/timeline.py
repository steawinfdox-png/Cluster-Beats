import seaborn as sns
import pandas as pd
#plot chronological frequency of all clusters
df["Release Date"] = pd.to_datetime(df["Release Date"], errors="coerce")
df["Year"] = df["Release Date"].dt.year
timeline = df.groupby(["Year", "Cluster Names"]).size().reset_index(name = "Count")
plt.figure(figsize=(6,6))
sns.lineplot(data=timeline, x = "Year", y = "Count", hue = "Cluster Names", marker = "o")
plt.xlim(left=2018)
plt.xlim(right=2025)
plt.title("Stray Kids Song Topics over Time")
plt.legend(loc="upper right", bbox_to_anchor=(1.8, 1), ncol=1)
plt.show
