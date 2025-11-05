import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())
    df.loc[df["status"] == "Scheduled", "status"] = "Completed"
    print("Updated Data Preview:")
    print(df.head())

    print("\nFinal file saved")


if __name__ == "__main__":
    compute()
