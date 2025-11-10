import os
import sys
import pandas as pd
from scipy.stats import skew, kurtosis


def get_csv(file):
    path = os.path.join(sys.path[0], file)
    return pd.read_csv(path)


def compute():
    df = get_csv(input())
    df = df[df["order_status"] == "Completed"]
    x = df["total_amount"]
    print("--- Spread / Dispersion ---")
    _range = x.max() - x.min()
    variance = round(x.var(), 2)
    std_dev = round(x.std(), 2)
    print("Range: ", _range)
    print("Variance: ", variance)
    print("Standard Deviation: ", std_dev)

    print("\n--- Distribution Shape ---")
    skew_val = round(skew(x), 3)
    kurt_val = round(kurtosis(x), 3)
    print("Skewness: ", skew_val)
    print("Kurtosis: ", kurt_val)

    print("""\n--- Insights ---""")
    print("- Range shows the spread between the smallest and largest order amounts.")
    print(
        "- High variance or standard deviation indicates variability in order amounts."
    )

    # ✅ Dynamic interpretation based on skewness
    if skew_val > 0:
        print(
            "- Positive skewness: distribution has a long tail to the right (some very high orders)."
        )
    elif skew_val < 0:
        print(
            "- Negative skewness: distribution has a long tail to the left (some very low orders)."
        )
    else:
        print("- Skewness near 0: distribution is roughly symmetric.")

    # ✅ Dynamic interpretation based on kurtosis
    if kurt_val > 0:
        print(
            "- Positive kurtosis: sharper peak and fatter tails than normal distribution."
        )
    elif kurt_val < 0:
        print("- Negative kurtosis: flatter distribution than normal.")
    else:
        print("- Kurtosis near 0: normal-like distribution.")


if __name__ == "__main__":
    compute()
