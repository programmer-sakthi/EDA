# lazy to do the first questions
import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():

    df = get_csv(input())
    df = df[df["status"] != "Cancelled"]
    amount = df["final_amount"]
    rating = df["service_rating"]

    print("Central Tendency Measures of service amounts (₹):")
    mean = round(amount.mean(), 2)
    median = round(amount.median(), 2)
    mode = round(amount.mode()[0], 2)
    print(f"Mean: {mean}, Median: {median}, Mode: {mode}")

    print("\nCentral Tendency Measures of service ratings:")
    mean = round(rating.mean(), 2)
    median = round(rating.median(), 2)
    mode = round(rating.mode()[0], 2)
    print(f"Mean: {mean}, Median: {median}, Mode: {mode}")


if __name__ == "__main__":
    compute()
