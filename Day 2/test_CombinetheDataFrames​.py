import os
import sys
import pandas as pd

def load_csv(filename):
    """Helper function to load a CSV file from script directory."""
    path = os.path.join(sys.path[0], filename)
    if not os.path.exists(path):
        print(f"Error: File '{filename}' not found in script directory!")
        sys.exit()
    return pd.read_csv(path)

def main():
    # ---- Step 1: Ask user for Users CSV ----
    users_file = input().strip()
    users_df = load_csv(users_file)
    # print("\n--- Users DataFrame Loaded ---")
    print(users_df.head(), "\n")

    # ---- Step 2: Ask user for Orders CSV ----
    orders_file = input("Enter the Orders CSV filename (with .csv extension): ").strip()
    orders_df = load_csv(orders_file)
    print("\n--- Orders DataFrame Loaded ---")
    print(orders_df.head(), "\n")

    # ---- Step 3: Merge ----
    df_merge = pd.merge(users_df, orders_df, on="user_id", how="inner")
    print("\n--- Merged DataFrame using pd.merge() ---")
    print(df_merge.head(), "\n")

    # ---- Step 4: Join ----
    df_join = users_df.set_index("user_id").join(
        orders_df.set_index("user_id"),
        how="inner"
    ).reset_index()

    print("\n--- Joined DataFrame using DataFrame.join() ---")
    print(df_join.head(), "\n")

if __name__ == "__main__":
    main()
