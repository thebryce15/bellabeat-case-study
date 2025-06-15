import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# === 1. Setup ===
# Ensure output directories exist
os.makedirs("outputs/plots", exist_ok=True)

# === 2. Load Cleaned Data ===
df = pd.read_csv("data/daily_activity_clean.csv")

# === 3. Data Cleaning ===
df['activity_date'] = pd.to_datetime(df['activity_date'], errors='coerce')
df['daily_steps'] = pd.to_numeric(df['daily_steps'], errors='coerce')
df['distance'] = pd.to_numeric(df['distance'], errors='coerce')
df['calories'] = pd.to_numeric(df['calories'], errors='coerce')

df_clean = df.dropna().copy()  #combine dropna and .copy()

# === 4. Summary Statistics ===
summary_stats = df_clean[['daily_steps', 'distance', 'calories']].agg(['mean', 'median', 'std']).T
summary_stats.to_csv("outputs/summary_stats.csv")

# === 5. Correlation Matrix ===
corr = df_clean[['daily_steps', 'distance', 'calories']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm')
plt.title("Correlation Matrix")
plt.savefig("outputs/plots/correlation_matrix.png")
plt.clf()

# === 6. Distribution of Daily Steps ===
sns.histplot(df_clean['daily_steps'], kde=True)
plt.title("Distribution of Daily Steps")
plt.xlabel("Steps")
plt.ylabel("Frequency")
plt.savefig("outputs/plots/steps_distribution.png")
plt.clf()

# === 7. Activity Over Time ===
df_by_date = df_clean.groupby('activity_date')[['daily_steps', 'calories']].mean().reset_index()

sns.lineplot(data=df_by_date, x='activity_date', y='daily_steps')
plt.title("Average Daily Steps Over Time")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("outputs/plots/steps_over_time.png")
plt.clf()

# === 8. Scatter Plot: Steps vs Calories ===
sns.scatterplot(data=df_clean, x='daily_steps', y='calories')
plt.title("Steps vs. Calories Burned")
plt.xlabel("Daily Steps")
plt.ylabel("Calories")
plt.savefig("outputs/plots/steps_vs_calories.png")
plt.clf()

# === 9. Weekday vs Weekend Analysis ===
df_clean['day_type'] = df_clean['activity_date'].dt.dayofweek.apply(
    lambda x: 'Weekend' if x >= 5 else 'Weekday'
)

sns.barplot(data=df_clean, x='day_type', y='daily_steps')
plt.title("Average Daily Steps: Weekday vs Weekend")
plt.xlabel("Day Type")
plt.ylabel("Steps")
plt.savefig("outputs/plots/weekday_vs_weekend.png")
plt.clf()

print("EDA complete! Summary stats and plots saved to /outputs/")
