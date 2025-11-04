import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    dp = get_csv(input())
    print("Null values in key columns:")
    key_cols = ["discount%", "tax", "tax_amount(INR)", "service_rating"]
    print(dp[key_cols].isnull().sum())

    print("\nCleaned DataFrame:")

    dp["tax"] = dp["tax"].fillna(0)
    dp["tax_amount(INR)"] = dp["tax_amount(INR)"].fillna(0)

    avg_rating = dp["service_rating"].mean()
    dp["service_rating"] = dp["service_rating"].fillna(avg_rating)

    print(dp)


if __name__ == "__main__":
    compute()
