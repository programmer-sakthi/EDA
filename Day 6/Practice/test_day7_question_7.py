import pymysql
import pandas as pd
from typing import Optional, Tuple

# Set display options for pandas to match output format
pd.set_option("display.float_format", lambda x: "%.2f" % x)


def create_connection() -> (
    Tuple[Optional[pymysql.connections.Connection], Optional[pymysql.cursors.Cursor]]
):
    """Establishes a connection to the MySQL database."""
    try:
        connection = pymysql.connect(
            host="localhost", user="rootuser", passwd="rootuser", database="rootuser"
        )
        cursor = connection.cursor()
        return connection, cursor
    except pymysql.MySQLError as e:
        print(f"❌ Error while connecting to MySQL: {e}")
        return None, None


def fetch_appointments_data(
    connection: pymysql.connections.Connection,
) -> Optional[pd.DataFrame]:
    """Fetches all data from the 'appointments' table into a Pandas DataFrame."""
    try:
        # Use pandas read_sql_query for direct DataFrame creation
        query = "SELECT * FROM appointments"
        df = pd.read_sql_query(query, connection)
        print(f"Fetched appointments data with columns: {list(df.columns)}")
        return df
    except (pymysql.MySQLError, ValueError) as e:
        print(f"❌ Error fetching appointments data: {e}")
        return None


def clean_and_preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """Performs data cleaning and preprocessing."""

    # 1. Fill missing values by forward filling
    if df.isnull().any().any():
        # Use .copy() to ensure we work on our own data structure
        df = df.ffill().copy()
        print("Missing values detected and filled using forward fill.")

    # 2. Convert 'appointment_date' to datetime format
    if "appointment_date" in df.columns:
        # Use .loc for explicit modification of the dataframe
        df.loc[:, "appointment_date"] = pd.to_datetime(df["appointment_date"])
        print("'appointment_date' converted to datetime format.")
    else:
        print("Warning: 'appointment_date' column not found for conversion.")

    # 3. Standardize payment methods
    if "payment_method" in df.columns:
        standardization_map = {
            "PhonePe": "UPI",
            "gpay": "UPI",
            "Google Pay": "UPI",
            "Paytm": "UPI",
        }
        changes_made = (
            df["payment_method"].replace(standardization_map).nunique()
            != df["payment_method"].nunique()
        )
        # Use .loc for explicit modification of the dataframe
        df.loc[:, "payment_method"] = df["payment_method"].replace(standardization_map)
        if changes_made:
            print("Standardized payment methods to UPI.")
        else:
            print("No payment methods needed standardization.")
    else:
        print("Warning: 'payment_method' column not found for standardization.")

    # 4. Rename columns
    rename_map = {"appointment_date": "date", "provider_rating": "provider_rating"}
    # Filter map to only include columns that exist in the DataFrame
    valid_rename_map = {k: v for k, v in rename_map.items() if k in df.columns}
    if valid_rename_map:
        # Assign result of rename to df, avoid inplace
        df = df.rename(columns=valid_rename_map)
        print(f"Renamed columns: {valid_rename_map}")
    else:
        print("No columns were renamed as required columns were missing.")

    if "status" in df.columns:
        initial_count = len(df)
        # Slicing creates a new filtered DataFrame
        df = df[df["status"].str.lower() == "completed"]
        final_count = len(df)
        print(
            f"Filtered appointments: kept {final_count} completed out of {initial_count} total."
        )
    else:
        print("Warning: 'status' column not found for filtering.")

    # 6. Sort by 'final_amount' in descending order
    if "final_amount" in df.columns:
        # Use sort_values and assign result to df, avoid inplace
        df = df.sort_values(by="final_amount", ascending=False)
        print("Sorted data by 'final_amount' in descending order.")
    else:
        print("Warning: 'final_amount' column not found for sorting.")

    return df


def analyze_data(df: pd.DataFrame):
    """Computes and prints basic statistics."""

    # 1. Average final_amount grouped by city
    if all(col in df.columns for col in ["final_amount", "city"]):
        avg_by_city = df.groupby("city")["final_amount"].mean()
        print("\nAverage final_amount by city:")
        print(avg_by_city)
    else:
        print(
            "Warning: 'final_amount' or 'city' column missing for average calculation."
        )

    if "payment_method" in df.columns:
        most_used_payment = df["payment_method"].mode()
        if not most_used_payment.empty:
            print(f"\nMost used payment method: {most_used_payment.iloc[0]}")
        else:
            print("\nMost used payment method: N/A")
    else:
        print("Warning: 'payment_method' column missing for most used calculation.")

    # 3. Descriptive statistics for provider ratings
    pd.set_option("display.precision", 6)
    if "provider_rating" in df.columns:
        print("\nDistribution of provider ratings:")
        describe_rating = df["provider_rating"].describe()
        pd.set_option("display.float_format", "{:.6f}".format)
        print(describe_rating)
        pd.reset_option("display.float_format")
        # print(describe_rating)

    else:
        print("Warning: 'provider_rating' column missing for descriptive statistics.")


if __name__ == "__main__":
    conn, cursor = create_connection()

    if conn:
        try:
            appointments_df = fetch_appointments_data(conn)

            if appointments_df is not None and not appointments_df.empty:
                # Use .copy(deep=True) for full isolation from original fetched data
                cleaned_df = clean_and_preprocess_data(appointments_df.copy(deep=True))
                if not cleaned_df.empty:
                    analyze_data(cleaned_df)
                else:
                    print("\nNo data to analyze after filtering.")
            elif appointments_df is not None and appointments_df.empty:
                print("\nAppointments table is empty.")

        finally:
            conn.close()
