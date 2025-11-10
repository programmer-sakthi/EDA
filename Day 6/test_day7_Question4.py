import pandas as pd
import pymysql


def fetch_delivered_orders():
    """Connects to MySQL using pymysql and fetches completed (delivered) orders."""
    conn = None
    cursor = None
    try:
        # Connect to MySQL database
        conn = pymysql.connect(
            host="localhost",
            user="rootuser",
            passwd="rootuser",  # correct keyword
            db="rootuser",  # correct keyword
            cursorclass=pymysql.cursors.DictCursor,
        )
        cursor = conn.cursor()

        # Fetch orders where status is 'completed' (case-insensitive)
        query = """
        SELECT *
        FROM Orders
        WHERE LOWER(order_status) = 'completed';
        """
        cursor.execute(query)
        rows = cursor.fetchall()

        # Load into Pandas DataFrame
        df = pd.DataFrame(rows)
        return df

    except pymysql.MySQLError as err:
        print(f"Error: {err}")
        return pd.DataFrame()

    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def preprocess_orders(df):
    """Preprocess the orders DataFrame."""
    if df.empty:
        return df

    # Convert order_date to datetime
    df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

    # Convert total_amount to float and rename
    if "total_amount" in df.columns:
        df["total_bill"] = df["total_amount"].astype(float)
        df.drop(columns=["total_amount"], inplace=True)

    # Create yearmonth column if not present
    if "yearmonth" not in df.columns:
        df["yearmonth"] = df["order_date"].dt.strftime("%Y-%m")

    return df


def revenue_by_payment_method(df):
    """Generate pivot table: Total revenue by payment method across months."""
    if df.empty or "payment_method" not in df.columns or "total_bill" not in df.columns:
        print("Insufficient data to generate revenue pivot table.")
        return

    pivot = pd.pivot_table(
        df,
        values="total_bill",
        index="yearmonth",
        columns="payment_method",
        aggfunc="sum",
        fill_value=0,
    )
    print("Total Revenue by Payment Method Across Months:")
    print(pivot)
    print()


def orders_per_restaurant(df):
    """Generate pivot table: Number of orders at each restaurant per month."""
    if df.empty or "name_restaurant" not in df.columns or "order_id" not in df.columns:
        print("Insufficient data to generate restaurant orders pivot table.")
        return

    pivot = pd.pivot_table(
        df,
        values="order_id",
        index="yearmonth",
        columns="name_restaurant",
        aggfunc="count",
        fill_value=0,
    )
    print("Number of Orders at Each Restaurant Every Month:")
    print(pivot)
    print()


def most_frequent_cuisine(df):
    """Identify the most frequently ordered cuisine type in each city."""
    if df.empty or "cuisine_type" not in df.columns or "user_city" not in df.columns:
        print("'cuisine_type' column not found in the data.")
        return

    grouped = (
        df.groupby(["user_city", "cuisine_type"]).size().reset_index(name="order_count")
    )
    idx = grouped.groupby("user_city")["order_count"].idxmax()
    top_cuisines = grouped.loc[idx]

    print("Most Frequently Ordered Cuisine by City:")
    for _, row in top_cuisines.iterrows():
        print(f"{row['user_city']}: {row['cuisine_type']} ({row['order_count']})")
    print()


def main():
    # Fetch delivered orders
    df_orders = fetch_delivered_orders()

    # Preprocess the data
    df_orders = preprocess_orders(df_orders)

    # Business analysis
    revenue_by_payment_method(df_orders)
    orders_per_restaurant(df_orders)
    most_frequent_cuisine(df_orders)


if __name__ == "__main__":
    main()
