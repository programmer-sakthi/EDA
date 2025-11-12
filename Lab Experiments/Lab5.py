import pymysql
import pandas as pd

HOST = "localhost"
USER = "rootuser"
PASSWORD = "rootuser"
DATABASE = "rootuser"
try:
    connection = pymysql.connect(
        host=HOST, user=USER, passwd=PASSWORD, database=DATABASE
    )
except Exception as e:
    print("Database connection failed:", e)
    exit()

try:
    query = "SELECT * FROM appointments WHERE LOWER(status) = 'completed';"
    df = pd.read_sql(query, connection)
except Exception as e:
    print("Error fetching appointment data:", e)
    connection.close()
    exit()

df.columns = df.columns.str.strip()
df = df.drop_duplicates()

try:
    pivot_df = pd.pivot_table(
        df,
        values="provider_rating",
        index="provider_id",
        columns="category",
        aggfunc="mean",
        fill_value=0,
    ).reset_index()
except Exception as e:
    print("Error creating pivot table:", e)
    connection.close()
    exit()

try:
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS provider_category_rating;")

    cols = ", ".join(
        [
            f"`{col}` FLOAT" if col != "provider_id" else "`provider_id` VARCHAR(20)"
            for col in pivot_df.columns
        ]
    )
    create_query = f"CREATE TABLE provider_category_rating ({cols});"
    cursor.execute(create_query)

    for _, row in pivot_df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        insert_query = f"INSERT INTO provider_category_rating VALUES ({placeholders})"
        cursor.execute(insert_query, tuple(row))
    connection.commit()
except Exception as e:
    print("Error saving pivot table:", e)
    connection.close()
    exit()

try:
    cursor.execute("DROP TABLE IF EXISTS cleaned_appointments;")
    col_defs = ", ".join([f"`{col}` VARCHAR(255)" for col in df.columns])
    cursor.execute(f"CREATE TABLE cleaned_appointments ({col_defs});")

    for _, row in df.iterrows():
        placeholders = ", ".join(["%s"] * len(row))
        insert_query = f"INSERT INTO cleaned_appointments VALUES ({placeholders})"
        cursor.execute(insert_query, tuple(row))
    connection.commit()
except Exception as e:
    print("Error saving cleaned appointments:", e)
    connection.close()
    exit()

# -------------------------------------------------------
# STEP 6: VALIDATION – FETCH TOP 5 ROWS
# -------------------------------------------------------
try:
    provider_preview = pd.read_sql(
        "SELECT * FROM provider_category_rating LIMIT 5;", connection
    )
    cleaned_preview = pd.read_sql(
        "SELECT * FROM cleaned_appointments LIMIT 5;", connection
    )

    print("Table `provider_category_rating` uploaded successfully.")
    print("Cleaned appointment data saved to `cleaned_appointments`.\n")

    print("Top rows from `provider_category_rating`:\n", provider_preview, "\n")
    print("Top rows from `cleaned_appointments`:\n", cleaned_preview)
except Exception as e:
    print("Error during validation:", e)
finally:
    connection.close()


# Description:

# Create the Python script connects to a MySQL database and performs a complete workflow for extracting, transforming, analyzing, and storing data from an appointments dataset. It uses the pymysql library for MySQL interaction and pandas for data manipulation. The script is modular, cleanly structured, and designed for automation or integration into larger data pipelines.

# Functionality Overview

# Data Extraction

# Fetches all appointment records where the status is 'Completed' (case-insensitive).

# Loads the data into a pandas DataFrame for further processing.

# Pivot Table Creation

# Builds a pivot table that shows the average provider rating grouped by provider_id and category.

# This allows analysis of provider performance across different service types.

# Saving Pivot Table to MySQL

# Dynamically creates a MySQL table (provider_category_rating) from the pivot table.

# Automatically detects and maps data types from pandas to SQL.

# Inserts cleaned and transformed pivot data into the database.

# Saving Cleaned Appointments

# Creates a table named cleaned_appointments in MySQL with a fixed schema.

# Inserts all cleaned completed appointment records into this table for future analysis or reporting.

# Validation

# Retrieves and prints the top 5 rows from both provider_category_rating and cleaned_appointments tables to verify that data upload was successful.

# Database details:

# HOST: localhost

# DB: rootuser

# Default USER: rootuser

# Default PWD: rootuser


# Note: Tables and Values are Prepopulated.

# Input format :
# No Console Input

# Output format :
# Confirmation that pivot and cleaned data are successfully saved to MySQL.

# Preview of the first 5 rows from each saved table (provider_category_rating and cleaned_appointments) for validation.

# Messages clearly indicating the progress and success of each processing step.

# Sample test cases :
# Input 1 :
# Output 1 :
# Table `provider_category_rating` uploaded successfully.
# Cleaned appointment data saved to `cleaned_appointments`.

# Top rows from `provider_category_rating`:
#   provider_id  Hair Care  Nail Care  Skin Care  Wellness
# 0      PRV501        4.8        0.0        0.0       0.0
# 1      PRV502        0.0        0.0        4.7       0.0
# 2      PRV504        0.0        0.0        0.0       4.9
# 3      PRV505        0.0        4.6        0.0       0.0

# Top rows from `cleaned_appointments`:
#   appointment_id user_id  ...     specialization provider_rating
# 0        APT0001  USR001  ...       Hair Stylist             4.8
# 1        APT0002  USR002  ...      Dermatologist             4.7
# 2        APT0004  USR004  ...  Massage Therapist             4.9
# 3        APT0005  USR005  ...    Nail Technician             4.6

# [4 rows x 26 columns]
