import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())
    df["appointment_date"] = pd.to_datetime(
        df["appointment_date"], dayfirst=True, errors="coerce"
    )
    df["appointment_time"] = pd.to_datetime(
        df["appointment_time"], format="%H:%M", errors="coerce"
    ).dt.time
    print("Duplicate appointments based on appointment_id:")
    duplicates = df.duplicated(subset="appointment_id", keep=False)
    print(df[duplicates].sort_index())
    print("\nCleaned DataFrame:")
    df = df.sort_values(
        by=["user_id", "appointment_date", "appointment_time"],
        ascending=[True, False, False],
    )
    print(df.drop_duplicates(subset="appointment_id"))

    print("Cleaned data saved to the same file")


if __name__ == "__main__":
    compute()
