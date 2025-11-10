import pandas as pd
import pymysql


def get_connection():
    """Establish and return a pymysql connection to the database."""
    return pymysql.connect(
        host="localhost",
        user="rootuser",
        passwd="rootuser",  # pymysql uses 'passwd' instead of 'password'
        db="rootuser",
        autocommit=True,
        cursorclass=pymysql.cursors.DictCursor,
    )


def fetch_delivered_orders():
    """Fetch only completed orders from Orders table."""
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM Orders WHERE LOWER(order_status) = 'completed';"
        cursor.execute(query)
        rows = cursor.fetchall()
        df = pd.DataFrame(rows)
        return df
    except pymysql.MySQLError as e:
        print(f"Error fetching orders: {e}")
        return pd.DataFrame()
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def create_city_month_bill_pivot(df):
    """Pivot orders to show total billing per city per month."""
    if df.empty:
        return df

    # Ensure total_amount is float
    df["total_amount"] = df["total_amount"].astype(float)

    # Create yearmonth column if not present
    if "yearmonth" not in df.columns:
        df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
        df["yearmonth"] = df["order_date"].dt.strftime("%Y-%m")

    # Group by city_user and yearmonth, sum total_amount
    pivot_df = df.groupby(["city_user", "yearmonth"], as_index=False)[
        "total_amount"
    ].sum()
    pivot_df.rename(columns={"total_amount": "total_bill"}, inplace=True)
    return pivot_df


def save_to_city_month_bill(pivot_df):
    """Save pivoted data to city_month_bill table in MySQL."""
    if pivot_df.empty:
        print("No data to save to city_month_bill.")
        return

    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Drop table if exists
        cursor.execute("DROP TABLE IF EXISTS city_month_bill;")

        # Create table
        create_query = """
        CREATE TABLE city_month_bill (
            city_user VARCHAR(255),
            yearmonth VARCHAR(7),
            total_bill FLOAT
        );
        """
        cursor.execute(create_query)

        # Insert rows
        insert_query = "INSERT INTO city_month_bill (city_user, yearmonth, total_bill) VALUES (%s, %s, %s);"
        for _, row in pivot_df.iterrows():
            cursor.execute(
                insert_query, (row["city_user"], row["yearmonth"], row["total_bill"])
            )

        print("city_month_bill table updated.")
    except pymysql.MySQLError as e:
        print(f"Error saving pivot: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def replace_order_details_table(df):
    """Replace OrderDetails table with full transformed orders."""
    if df.empty:
        print("No data to replace OrderDetails table.")
        return

    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()

        # Drop table if exists
        cursor.execute("DROP TABLE IF EXISTS OrderDetails;")

        # Create table dynamically based on DataFrame columns
        columns = df.columns
        col_defs = []
        for col in columns:
            if df[col].dtype == "float64" or df[col].dtype == "int64":
                col_defs.append(f"{col} FLOAT")
            else:
                col_defs.append(f"{col} VARCHAR(255)")
        create_query = f"CREATE TABLE OrderDetails ({', '.join(col_defs)});"
        cursor.execute(create_query)

        # Insert rows
        placeholders = ", ".join(["%s"] * len(columns))
        insert_query = (
            f"INSERT INTO OrderDetails ({', '.join(columns)}) VALUES ({placeholders});"
        )
        for _, row in df.iterrows():
            cursor.execute(insert_query, tuple(row))

        print("OrderDetails table replaced.")
    except pymysql.MySQLError as e:
        print(f"Error replacing OrderDetails table: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def show_city_month_bill():
    """Retrieve and display contents of city_month_bill table."""
    conn = None
    cursor = None
    try:
        conn = get_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM city_month_bill ORDER BY city_user, yearmonth;")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows)
        print("city_month_bill table contents:")
        print(df)
    except pymysql.MySQLError as e:
        print(f"Error reading city_month_bill: {e}")
    finally:
        if cursor:
            cursor.close()
        if conn:
            conn.close()


def main():
    # Step 1: Fetch completed orders
    df_orders = fetch_delivered_orders()

    # Step 2: Pivot total billing per city per month
    pivot_df = create_city_month_bill_pivot(df_orders)

    # Step 3: Save pivoted data to city_month_bill table
    save_to_city_month_bill(pivot_df)

    # Step 4: Replace OrderDetails table with transformed orders
    replace_order_details_table(df_orders)

    # Step 5: Display city_month_bill table
    show_city_month_bill()


if __name__ == "__main__":
    main()
