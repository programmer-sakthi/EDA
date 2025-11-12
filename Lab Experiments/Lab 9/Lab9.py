# Exp9
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# ---------------- Load Dataset ----------------
# Update this path if your iris dataset is stored elsewhere
df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Python-EDA\data\Iris.csv")

print("\n=== Multivariate Analysis: Iris Dataset ===")

# Display first few records
print("\nFirst 5 rows of the dataset:")
print(df.head())

# Display basic info
print("\nDataset Info:")
print(df.info())

# Display summary statistics
print("\nSummary Statistics:")
print(df.describe())

# ---------------- Pairplot ----------------
print("\nGenerating pairplot to visualize relationships between features...")
sns.pairplot(df, hue="Species", diag_kind="kde", palette="husl")
plt.suptitle("Pairplot of Iris Features by Species", y=1.02)
plt.show()

# ---------------- Correlation Heatmap ----------------
print("\nGenerating heatmap to visualize correlations between numeric features...")
plt.figure(figsize=(8, 6))
corr = df.select_dtypes(include=["float64", "int64"]).corr()
sns.heatmap(corr, annot=True, cmap="YlGnBu", linewidths=0.5)
plt.title("Correlation Heatmap of Iris Dataset Features")
plt.show()

# ---------------- Insights ----------------
print("\n=== Insights from Multivariate Analysis ===")
print(
    "- Petal length and petal width are highly correlated, indicating they vary together across species."
)
print(
    "- Sepal measurements show moderate correlation with each other but less with petal measurements."
)
print(
    "- Setosa species tend to have smaller petal measurements compared to Versicolor and Virginica."
)
print(
    "- Virginica generally has the largest petal and sepal dimensions among all species."
)
