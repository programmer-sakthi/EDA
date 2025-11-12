# Exp8
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------- PART 1: WINE DATASET --------------------
# Load Wine dataset directly from your system path
df_wine = pd.read_csv(
    r"C:\Users\HP\OneDrive\Desktop\Python-EDA\data\wine-quality-white-and-red.csv"
)

print("\n=== Part 1: Univariate Analysis (Wine Dataset) ===")

# Select only numeric columns
numeric_cols = df_wine.select_dtypes(include=["float64", "int64"]).columns

print("\nNumeric columns found in Wine dataset:")
print(list(numeric_cols))

# Histogram
df_wine[numeric_cols].hist(
    figsize=(12, 10), bins=15, color="skyblue", edgecolor="black"
)
plt.suptitle("Histogram - Distribution of Wine Features")
plt.tight_layout()
plt.show()

# Boxplot
plt.figure(figsize=(12, 6))
df_wine[numeric_cols].boxplot()
plt.title("Boxplot - Distribution and Outliers in Wine Features")
plt.xticks(rotation=45)
plt.ylabel("Value Range")
plt.show()

# Density Plots
df_wine[numeric_cols].plot(
    kind="density", subplots=True, layout=(4, 4), figsize=(12, 10), sharex=False
)
plt.suptitle("Density Plots - Wine Feature Distributions")
plt.tight_layout()
plt.show()

# Variability
variability = df_wine[numeric_cols].std().sort_values(ascending=False)
print("\nFeature Variability (Standard Deviation):")
print(variability)

high_var = variability.head(3)
print("\nFeatures with highest variability:")
for feature in high_var.index:
    print(f"- {feature}: Std = {high_var[feature]:.2f}")

# -------------------- PART 2: TIPS DATASET --------------------
# Load Tips dataset directly from your system path
df_tips = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Python-EDA\data\tips.csv")

print("\n=== Part 2: Bivariate Analysis (Tips Dataset) ===")

# Scatter Plot: total_bill vs tip (by smoker)
plt.figure(figsize=(7, 5))
sns.scatterplot(data=df_tips, x="total_bill", y="tip", hue="smoker", palette="cool")
plt.title("Scatterplot: Total Bill vs Tip (by Smoker Status)")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.legend(title="Smoker")
plt.show()

# Boxplot: Tip by Gender
plt.figure(figsize=(6, 5))
sns.boxplot(data=df_tips, x="sex", y="tip", palette="Set2")
plt.title("Boxplot: Tip Distribution by Gender")
plt.xlabel("Gender")
plt.ylabel("Tip ($)")
plt.show()

# Barplot: Average Total Bill by Day
plt.figure(figsize=(6, 5))
sns.barplot(data=df_tips, x="day", y="total_bill", ci=None, palette="viridis")
plt.title("Barplot: Average Total Bill by Day")
plt.xlabel("Day")
plt.ylabel("Average Total Bill ($)")
plt.show()

# Correlation
corr_val = df_tips["total_bill"].corr(df_tips["tip"]).round(2)
print(f"\nCorrelation between Total Bill and Tip: {corr_val}")

print("\nInsights:")
print("- Tips generally increase with higher total bills (positive correlation).")
print("- Female customers may tip differently compared to males (as seen in boxplot).")
print("- Higher bills often occur on weekends (as seen in barplot).")
