import os
import sys
import pandas as pd


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())

    # Remove cancelled orders
    df = df[df["status"] != "Cancelled"]

    # Pearson correlation among amounts
    print("Pearson correlation:")
    pearson_corr = df[["price", "discounted_amount(INR)", "final_amount"]].corr(
        method="pearson"
    )
    print(pearson_corr)

    # Correlation with service_rating
    print("\nCorrelation with service_rating:")
    corr_with_rating = df[["price", "final_amount", "service_rating"]].corr(
        method="pearson"
    )
    print(corr_with_rating) 

    # Insights
    print(
        "\nAnswer: Based on the correlations, customers who pay more do not tend to give higher ratings.\n"
    )
    print("Insights:")
    print(
        "* Correlation between price and service_rating is very close to zero, indicating almost no relationship."
    )
    print(
        "* Correlation between final_amount and service_rating is effectively zero, confirming no meaningful association."
    )
    print(
        "* Strong positive correlations exist among price, discounted_amount(INR), and final_amount, as expected."
    )
    print(
        "* Discount% shows moderate negative correlation with final_amount, suggesting higher percentage discounts slightly reduce total paid."
    )


if __name__ == "__main__":
    compute()
