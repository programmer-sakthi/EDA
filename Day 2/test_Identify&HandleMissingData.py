import os
import sys
import pandas as pd

def get_csv_path(file):
    return os.path.join(sys.path[0] , file)
   
def compute():
    users = pd.read_csv(get_csv_path(input()))
    orders = pd.read_csv(get_csv_path(input()))
    rest = pd.read_csv(get_csv_path(input()))
    reviews = pd.read_csv(get_csv_path(input()))
   
   
    print("Users DataFrame Loaded")
    print(users.head())
   
    print("\nOrders DataFrame Loaded")
    print(orders.head())
   
    print("\nRestaurants DataFrame Loaded")
    print(rest.head())
   
    print("\nReviews DataFrame Loaded")
    print(reviews.head())
   
   
    orders_users = pd.merge(orders , users , how = 'left')
    full_orders = pd.merge(orders_users , rest  ,on='restaurant_id' ,  how = 'left' , suffixes =('_user' , '_restaurant'))
    print("\nOrders + Users + Restaurants Preview")
    print(full_orders.loc[:4 , ['name_user' , 'name_restaurant']])
   
    print("\nRestaurants + Orders Info")
    rest_orders = pd.merge(rest , orders , on = 'restaurant_id', how = 'left')
    print(rest_orders.info())
   
    print("\n\nRestaurants + Reviews Info")
    rest_reviews = pd.merge(rest , reviews , on = 'restaurant_id', how = 'right' , suffixes=('_restaurant' , '_review'))
    print(rest_reviews.info())
   
    print("\n\nUsers + Reviews Info")
    rest_reviews = pd.merge( reviews, users , on = 'user_id', how = 'left')
   
    print(rest_reviews.info())# print(full_orders.columns)
    print()
    # print(rou.head())
   
if __name__ == '__main__':
    compute()