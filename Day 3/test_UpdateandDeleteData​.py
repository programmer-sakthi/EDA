import os
import sys

import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    orders = get_csv(input())
    reviews = get_csv(input())
    restaurants = get_csv(input())
    print("Updated Orders (First 5 Rows)")
    orders.loc[orders["order_id"] == "ORD1968", "delivery_time_min"] = 40
    cancelled = orders.loc[orders["order_status"] == "Cancelled"].copy()
    completed = orders.loc[orders["order_status"] == "Completed"].copy()

    cancelled.drop("order_status", axis=1, inplace=True)
    completed.drop("order_status", axis=1, inplace=True)

    print(orders.head())

    print("\nDelivered Orders (First 5 Rows)")
    print(completed.head())
    print("\nCancelled Orders (First 5 Rows)")
    print(cancelled.head())

    rating_map = {1: "Poor", 2: "Average", 3: "Good", 4: "Very Good", 5: "Excellent"}
    print("\nUsers Reviews with Rating Category & Flag (First 5 Rows)")
    reviews["rating_category"] = reviews["rating"].map(rating_map)
    reviews["review_flag"] = "Positive"
    reviews.loc[reviews["rating"] <= 3, "review_flag"] = "Negative"
    print(reviews.head())

    print("\nRestaurants Reviews (First 5 Rows)")
    print(restaurants.head())


if __name__ == "__main__":
    compute()
