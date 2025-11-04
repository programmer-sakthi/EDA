import os 
import sys 

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)

def compute():
    users=get_csv(input())
    orders = get_csv(input())
    
    users_orders = pd.merge(users,orders,on='user_id',how='inner')
    print("Inner Join Shape: ",users_orders.shape)
    users_orders = pd.merge(users,orders,on='user_id',how='left')
    print("Left Join Shape: ",users_orders.shape)
    users_orders = pd.merge(users,orders,on='user_id',how='outer')
    print("Outer Join Shape: ",users_orders.shape)
    
if __name__=='__main__':
    compute()
    

    
    
