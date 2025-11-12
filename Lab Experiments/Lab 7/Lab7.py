import pandas as pd
import matplotlib.pyplot as plt
import sys
import os


def main():
    df = pd.read_csv(r"C:\Users\HP\OneDrive\Desktop\Python-EDA\data\tips.csv")

    # Histogram - Total Bill
    plt.figure(figsize=(7, 4))
    plt.hist(df["total_bill"], bins=15, color="skyblue", edgecolor="black")
    plt.title("Distribution of Total Bill")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    # Histogram - Tip
    plt.figure(figsize=(7, 4))
    plt.hist(df["tip"], bins=15, color="lightgreen", edgecolor="black")
    plt.title("Distribution of Tip Amounts")
    plt.xlabel("Tip ($)")
    plt.ylabel("Frequency")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    # Bar chart - Average Tip per Day
    avg_tip_day = df.groupby("day")["tip"].mean()
    plt.figure(figsize=(6, 4))
    avg_tip_day.plot(kind="bar", color="coral", edgecolor="black")
    plt.title("Average Tip by Day")
    plt.xlabel("Day")
    plt.ylabel("Average Tip ($)")
    plt.xticks(rotation=0)
    plt.show()

    # Bar chart - Average Total Bill by Meal Time
    avg_bill_time = df.groupby("time")["total_bill"].mean()
    plt.figure(figsize=(5, 4))
    avg_bill_time.plot(kind="bar", color="orange", edgecolor="black")
    plt.title("Average Total Bill by Meal Time")
    plt.xlabel("Time of Day")
    plt.ylabel("Average Total Bill ($)")
    plt.xticks(rotation=0)
    plt.show()

    # Scatter Plot - Total Bill vs Tip with Smoker Color Coding
    plt.figure(figsize=(7, 5))
    colors = {"Yes": "red", "No": "blue"}
    for smoker_status, color in colors.items():
        subset = df[df["smoker"] == smoker_status]
        plt.scatter(
            subset["total_bill"],
            subset["tip"],
            color=color,
            label=smoker_status,
            alpha=0.7,
        )
    plt.title("Total Bill vs Tip (by Smoker Status)")
    plt.xlabel("Total Bill ($)")
    plt.ylabel("Tip ($)")
    plt.legend(title="Smoker")
    plt.grid(True, linestyle="--", alpha=0.5)
    plt.show()

    # Boxplot - Total Bill by Day
    plt.figure(figsize=(7, 5))
    df.boxplot(
        column="total_bill",
        by="day",
        grid=False,
        patch_artist=True,
        boxprops=dict(facecolor="lightblue"),
    )
    plt.title("Total Bill Distribution by Day")
    plt.suptitle("")
    plt.xlabel("Day")
    plt.ylabel("Total Bill ($)")
    plt.show()

    # Boxplot - Tip by Sex
    plt.figure(figsize=(6, 4))
    df.boxplot(
        column="tip",
        by="sex",
        grid=False,
        patch_artist=True,
        boxprops=dict(facecolor="lightgreen"),
    )
    plt.title("Tip Distribution by Gender")
    plt.suptitle("")
    plt.xlabel("Gender")
    plt.ylabel("Tip ($)")
    plt.show()


if _name_ == "_main_":
    main()
