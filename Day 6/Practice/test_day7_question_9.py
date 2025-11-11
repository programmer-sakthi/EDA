import pymysql
import pandas as pd


# --------------------- 1. CONNECT TO DATABASE --------------------- #
def get_connection():
    return pymysql.connect(
        host="localhost",
        user="rootuser",
        passwd="rootuser",
        db="rootuser",
        autocommit=True,
    )


# --------------------- 2. FETCH COMPLETED APPOINTMENTS --------------------- #
def fetch_completed_appointments():
    conn = get_connection()
    query = "SELECT * FROM appointments WHERE LOWER(status) = 'completed'"
    df = pd.read_sql(query, conn)
    conn.close()
    return df


# --------------------- 3. CREATE PIVOT TABLE --------------------- #
def create_provider_category_rating_pivot(df):
    pivot_df = pd.pivot_table(
        df,
        index="provider_id",
        columns="category",
        values="provider_rating",
        aggfunc="mean",
        fill_value=0,
    ).reset_index()
    return pivot_df


# --------------------- 4. SAVE DATAFRAME TO MYSQL --------------------- #
def save_dataframe_to_mysql(df, table_name):
    conn = get_connection()
    cursor = conn.cursor()

    # Drop if table exists
    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")

    # Create table dynamically
    columns = []
    for col in df.columns:
        dtype = df[col].dtype
        if "float" in str(dtype):
            col_type = "FLOAT"
        elif "int" in str(dtype):
            col_type = "INT"
        else:
            col_type = "VARCHAR(100)"
        columns.append(f"`{col}` {col_type}")

    create_stmt = f"CREATE TABLE {table_name} ({', '.join(columns)})"
    cursor.execute(create_stmt)

    # Replace NaN with None for SQL compatibility
    df = df.where(pd.notnull(df), None)

    # Insert data
    for _, row in df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        insert_stmt = f"INSERT INTO {table_name} VALUES ({placeholders})"
        cursor.execute(insert_stmt, tuple(row))

    conn.close()
    print(f"Table `{table_name}` uploaded successfully.")


# --------------------- 5. SAVE TRANSFORMED APPOINTMENTS --------------------- #
def save_cleaned_appointments(df):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DROP TABLE IF EXISTS cleaned_appointments")

    create_stmt = """
        CREATE TABLE cleaned_appointments (
            appointment_id VARCHAR(20),
            user_id VARCHAR(20),
            user_name VARCHAR(100),
            gender VARCHAR(10),
            area VARCHAR(50),
            city VARCHAR(50),
            service_id VARCHAR(20),
            provider_id VARCHAR(20),
            appointment_date DATE,
            appointment_time TIME,
            status VARCHAR(20),
            payment_id VARCHAR(20),
            amount FLOAT,
            discount_percent FLOAT,
            tax FLOAT,
            discounted_amount FLOAT,
            tax_amount FLOAT,
            final_amount FLOAT,
            payment_method VARCHAR(50),
            service_rating FLOAT,
            service_name VARCHAR(100),
            category VARCHAR(50),
            price FLOAT,
            provider_name VARCHAR(100),
            specialization VARCHAR(50),
            provider_rating FLOAT
        )
    """
    cursor.execute(create_stmt)

    df = df.where(pd.notnull(df), None)

    for _, row in df.iterrows():
        cursor.execute(
            """
            INSERT INTO cleaned_appointments VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """,
            tuple(row),
        )

    conn.close()
    print("Cleaned appointment data saved to `cleaned_appointments`.")


# --------------------- 6. VALIDATION --------------------- #
def validate_table(table_name):
    conn = get_connection()
    df = pd.read_sql(f"SELECT * FROM {table_name} LIMIT 5", conn)
    conn.close()
    print(f"\nTop rows from `{table_name}`:")
    print(df)


# --------------------- MAIN EXECUTION --------------------- #
def main():
    # Step 1: Get completed appointment data
    df = fetch_completed_appointments()

    # Step 2: Create pivot: average rating by provider_id & category
    rating_pivot_df = create_provider_category_rating_pivot(df)

    # Step 3: Save pivot to MySQL
    save_dataframe_to_mysql(rating_pivot_df, "provider_category_rating")

    # Step 4: Save cleaned appointments data
    save_cleaned_appointments(df)

    # Step 5: Validate upload
    validate_table("provider_category_rating")
    validate_table("cleaned_appointments")


if __name__ == "__main__":
    main()
