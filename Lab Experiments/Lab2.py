import pandas as pd

# Input: number of daily sales entries
n = int(input())

# Input: daily sales amounts
sales = list(map(int, input().split()))

# Create Pandas Series
sales_series = pd.Series(sales)

# Input: number of items
m = int(input())

# Input: item details (name and price)
items = []
prices = []
for _ in range(m):
    name, price = input().split()
    items.append(name)
    prices.append(int(price))

# Create DataFrame
item_df = pd.DataFrame({"Item": items, "Price": prices})

# Output
print("Pandas Series (Daily Sales):", sales_series)
print("Pandas DataFrame (Item Details):", item_df)


# A data analyst named Rehan is working on a small project to organize data for a local shop.
# He needs to create:
# A Pandas Series to store daily sales amounts entered by the user.
# A Pandas DataFrame to store item details (item name and price) from user input.
# Your task is to help Rehan by writing a Python program that takes user input to create both a Series and a DataFrame, and then prints them properly formatted.



# Input format :
# The first line contains an integer n, the number of daily sales entries. The second line contains n space-separated integers representing daily sales amounts. The third line contains an integer m, the number of items in the shop. The next m lines each contain two values separated by a space: item_name (string) price (integer)

# Output format :
# In the First line print the Pandas Series created from the list of sales. In the Second line print the Pandas DataFrame created from the dictionary of items.

# Code constraints :
# 1 ≤ n ≤ 100 1 ≤ m ≤ 50 Each sales amount should be a positive integer (1 ≤ sales[i] ≤ 10^6) Item names must be non-empty strings (alphabetic only). Prices must be positive integers (1 ≤ price ≤ 10^5)

# Sample test cases :
# Input 1 :
# 3
# 1000 1500 1200
# 2
# Pen 10
# Pencil 5
# Output 1 :
# Pandas Series (Daily Sales):
# 0    1000
# 1    1500
# 2    1200
# dtype: int64

# Pandas DataFrame (Item Details):
#      Item  Price
# 0     Pen     10
# 1  Pencil      5
