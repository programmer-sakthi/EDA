import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    appointments = get_csv(input())
    payments = get_csv(input())
    services = get_csv(input())

    merge1 = pd.merge(appointments, payments, on=["appointment_id"])
    merge2 = pd.merge(merge1, services, on="service_id")

    print("Average rating per service provider:")
    avg_rating = merge1.groupby("provider_id")["service_rating"].mean()
    print(avg_rating.reset_index())

    print("\nRevenue and service rating statistics by city:")
    revenue_by_city = (
        merge1.groupby("city")
        .agg(
            total_revenue=("final_amount", "sum"),
            avg_revenue=("final_amount", "mean"),
            avg_rating=("service_rating", "mean"),
        )
        .reset_index()
    )
    print(revenue_by_city)

    print("\nRevenue by provider and service category (pivot table):")
    pivot = merge2.pivot_table(
        index="provider_id",
        columns="category",
        values="final_amount",
        aggfunc="sum",
        fill_value=0,  # fill missing combinations with 0
    ).reset_index()

    # Optional: reorder columns if needed
    pivot = pivot[
        ["provider_id"] + [col for col in pivot.columns if col != "provider_id"]
    ]

    print(pivot)


if __name__ == "__main__":
    compute()
