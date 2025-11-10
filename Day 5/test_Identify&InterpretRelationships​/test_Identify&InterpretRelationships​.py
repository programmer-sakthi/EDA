import os
import sys
import pandas as pd

def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)

def compute():
    file = input().strip()
    if not os.path.exists(file):
        print("File not found:", file)
        sys.exit(1)

    df = get_csv(file)

    # Ensure numeric columns for correlation
    df['total_amount'] = pd.to_numeric(df['total_amount'], errors='coerce')
    df['rating'] = pd.to_numeric(df['rating'], errors='coerce')

    # Drop rows with missing values in these columns
    df = df.dropna(subset=['total_amount', 'rating'])

    # --- Pearson Correlation (linear relationship) ---
    pearson_corr = df[['total_amount', 'rating']].corr(method='pearson')
    print("Pearson Correlation:")
    print(pearson_corr)
    print()

    # --- Spearman Correlation (rank-based / monotonic) ---
    spearman_corr = df[['total_amount', 'rating']].corr(method='spearman')
    print("Spearman Correlation:")
    print(spearman_corr)

if __name__ == '__main__':
    compute()
