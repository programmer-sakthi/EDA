import pymysql
import pandas as pd


# Step 1: Fetch appointments data from MySQL
def fetch_appointments():
    connection = pymysql.connect(
        host="localhost", user="rootuser", passwd="rootuser", db="rootuser"
    )
    query = "SELECT * FROM appointments"
    df = pd.read_sql(query, connection)
    connection.close()
    return df


# Step 2: Clean and preprocess the data
def preprocess_appointments(df):
    print("Preprocessing data...")

    # 2.1.1 Handle missing values (forward fill)
    if df.isnull().values.any():
        df.fillna(method="ffill", inplace=True)
        print("Missing values filled using forward fill.")

    # 2.1.2 Convert 'appointment_date' to datetime
    df["appointment_date"] = pd.to_datetime(df["appointment_date"], errors="coerce")

    # 2.1.3 Standardize payment methods
    df["payment_method"] = df["payment_method"].replace(
        {"PhonePe": "UPI", "gpay": "UPI", "Google Pay": "UPI", "Paytm": "UPI"}
    )

    # 2.1.4 Rename columns
    df.rename(columns={"appointment_date": "date"}, inplace=True)

    # 2.1.5 Filter only completed appointments
    df = df[df["status"].str.lower() == "completed"]

    # 2.1.6 Sort by final_amount descending
    df = df.sort_values(by="final_amount", ascending=False)

    print("Preprocessing complete.\n")
    return df


# Step 3: Create pivot tables for business questions
def create_pivot_tables(df):
    print("=== Pivot Tables and Business Insights ===")

    # 2.3.1: Total revenue by city and service category
    try:
        pivot1 = pd.pivot_table(
            df,
            values="final_amount",
            index="city",
            columns="category",
            aggfunc="sum",
            fill_value=0,
        )
        print("\n2.3.1: Total Revenue by City and Service Category")
        print(pivot1)
    except KeyError as e:
        print("Missing column for 2.3.1:", e)

    # 2.3.2: Average rating by provider_id and category
    try:
        pivot2 = pd.pivot_table(
            df,
            values="provider_rating",
            index="provider_id",
            columns="category",
            aggfunc="mean",
            fill_value=0,
        )
        print("\n2.3.2: Average Provider Rating by Provider ID and Category")
        print(pivot2)
    except KeyError as e:
        print("Missing column for 2.3.2:", e)

    # 2.3.3: Total revenue by service categories and providers
    try:
        pivot3 = pd.pivot_table(
            df,
            values="final_amount",
            index="category",
            columns="provider_name",
            aggfunc="sum",
            fill_value=0,
        )
        print("\n2.3.3: Total Revenue by Service Categories and Providers")
        print(pivot3)
    except KeyError as e:
        print("Missing column for 2.3.3:", e)

    # 2.3.4: Monthly revenue trending across cities
    try:
        df["year_month"] = df["date"].dt.to_period("M").astype(str)
        pivot4 = pd.pivot_table(
            df,
            values="final_amount",
            index="year_month",
            columns="city",
            aggfunc="sum",
            fill_value=0,
        )
        print("\n2.3.4: Monthly Revenue Trending Across Cities")
        print(pivot4)
    except KeyError as e:
        print("Missing column for 2.3.4:", e)


# Step 4: Main flow
def main():
    appointments_df = fetch_appointments()
    cleaned_df = preprocess_appointments(appointments_df)
    create_pivot_tables(cleaned_df)


if __name__ == "__main__":
    main()
