import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())
    payment_methods = ["gpay", "Google Pay", "PhonePe", "Paytm"]
    print("Records with inconsistent payment methods:")
    inconsistent = df[df["payment_method"].isin(payment_methods)]
    print(inconsistent)
    df["payment_method"] = df["payment_method"].replace(payment_methods, "UPI")

    print("\nAfter replacement, inconsistent payment methods should be gone:")
    inconsistent = df[df["payment_method"].isin(payment_methods)]
    print(inconsistent)


if __name__ == "__main__":
    compute()
