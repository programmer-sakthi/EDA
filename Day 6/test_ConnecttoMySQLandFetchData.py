import pymysql
import pandas as pd


def create_connection():
    try:
        connection = pymysql.connect(
            host="localhost", user="rootuser", passwd="rootuser", database="rootuser"
        )
        cursor = connection.cursor()
        return connection, cursor
    except pymysql.MySQLError as e:
        print("❌ Error while connecting to MySQL:", e)
        return None, None


if __name__ == "__main__":
    conn, cursor = create_connection()

    if conn:
        try:
            query = "SELECT * FROM Orders"
            df = pd.read_sql(query, conn)
            # print(df)

            if df.isnull().values.any():
                df.fillna(method="ffill", inplace=True)
            else:
                print("No missing values found.")

            df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")
            print("Converted 'order_date' to datetime.")
            df["total_amount"] = pd.to_numeric(df["total_amount"], errors="coerce")
            print("Converted 'total_amount' to float.")
            df.rename(
                columns={"total_amount": "total_bill", "rating": "customer_rating"},
                inplace=True,
                errors="ignore",
            )
            if "customer_rating" in df.columns:
                df.sort_values(by="customer_rating", ascending=False, inplace=True)
            print(
                "Renamed columns: {'total_amount': 'total_bill' , 'rating': 'customer_rating'}"
            )
            print("Data sorted by 'customer_rating' descending.")
            df = df[df["order_status"] == "Completed"]
            print("Filtered delivered orders :", len(df), "records found.")
            print(df.head())

        except pymysql.MySQLError as e:
            print("❌ Error fetching tables:", e)

        finally:
            conn.close()
