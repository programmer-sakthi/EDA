import pymysql


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
            # Query to show all tables in the current database
            user_id = input()
            print("Order Details:")
            cursor.execute("SELECT * FROM Orders WHERE order_id= %s", (user_id,))
            result = cursor.fetchall()
            print(result[0])

        except pymysql.MySQLError as e:
            print("❌ Error fetching tables:", e)

        finally:
            conn.close()
