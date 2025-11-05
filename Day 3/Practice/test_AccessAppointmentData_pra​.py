import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())

    print("Service ratings for appointments in Mumbai:")

    mumbai_appointments = df.loc[df["city"] == "Mumbai"]
    print(mumbai_appointments[["appointment_id", "service_rating"]])

    print("\nProvider ID and Final Amount of the 10th appointment:")
    provider_id = df.loc[9, "provider_id"]
    final_amount = df.loc[9, "final_amount"]
    print(f"Provider ID: {provider_id}, Final Amount: {final_amount}")

    # Convert 'appointment_date' to datetime
    df["appointment_date"] = pd.to_datetime(
        df["appointment_date"], dayfirst=True, errors="coerce"
    )

    # Filter completed appointments
    completed = df[df["status"].str.lower() == "completed"]

    # Sort by most recent date
    completed = completed.sort_values("appointment_date", ascending=False)

    # Select the last 5 completed appointments (date & service)
    last5 = completed[["appointment_date", "service_name"]].head(5)

    # Format date as YYYY-MM-DD
    last5["appointment_date"] = last5["appointment_date"].dt.strftime("%Y-%m-%d")

    print("\nLast 5 completed appointments (date & service):")
    print(last5.to_string(index=True))


if __name__ == "__main__":
    compute()
