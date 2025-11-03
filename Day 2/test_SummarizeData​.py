import os 
import sys 

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)
    
def print_total_revenue(orders):
    total_revenue=orders.groupby('payment_method')['total_amount'].sum().reset_index()
    total_revenue=total_revenue.rename(columns={'total_amount':'total_revenue'})
    print("Total revenue by payment method:")
    print(total_revenue)

def print_avg_order_amount(orders,users):
    user_orders=pd.merge(orders,users,on='user_id')
    user_orders=user_orders.groupby('city')['total_amount'].mean().reset_index()
    user_orders=user_orders.rename(columns={'total_amount': 'avg_order_amount'})
    print("Average order amount by city:")
    print(user_orders)
    
def print_num_order_per_restaurant(orders,restaurants):
    order_count=orders.groupby('restaurant_id')['order_id'].count().reset_index()
    order_count=order_count.rename(columns={'order_id' : 'total_orders'})
    print("Number of orders per restaurant:")
    print(order_count)

def print_city_wise_order_amount(orders,users):
    user_orders=pd.merge(orders,users,on='user_id')
    user_orders=user_orders.groupby('city').agg( 
        sum = ("total_amount" , 'sum'),
        mean = ("total_amount" , 'mean'),
        count = ("order_id" , 'count'),
        ).reset_index()
    print("City-wise order amount summary statistics:")
    print(user_orders)
        
    
    
    
def print_city_wise_total_and_avg_amount_and_avg_ratings(orders,users,restaurants):
    user_orders=pd.merge(orders,users,on='user_id' , how='left')
    user_restaurant_order = pd.merge(user_orders , restaurants , on= ['user_id','restaurant_id'] , how='left')
    user_restaurant_order = user_restaurant_order.groupby('city').agg(
        total_amount=("total_amount",'sum'),
        avg_amount=("total_amount",'mean'),
        avg_rating=("rating",'mean')
    ).reset_index()
    print("City-wise total & average order amounts, average ratings:")
    print(user_restaurant_order)
    
    
    
def city_and_payment_method_wise_total_order_amount(orders,users,restaurants):
    user_orders=pd.merge(orders,users,on='user_id')
    user_orders = user_orders.groupby(['city' , 'payment_method']).agg(
        total_amount_by_city_payment= ('total_amount', 'sum')
    ).reset_index()
    
    print("City and payment method wise total order amounts:")
    print(user_orders)

    
def compute():
    users=get_csv(input())
    orders = get_csv(input())
    restaurants = get_csv(input())
    print_total_revenue(orders)
    print()
    print_avg_order_amount(orders,users)
    print()
    print_num_order_per_restaurant(orders,restaurants)
    print()
    print_city_wise_order_amount(orders,users)
    print()
    print_city_wise_total_and_avg_amount_and_avg_ratings(orders,users,restaurants)
    print()
    city_and_payment_method_wise_total_order_amount(orders,users,restaurants)
    


if __name__=='__main__':
    compute()
    

    
    