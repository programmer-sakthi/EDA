import os 
import sys 
import pandas as pd


user_file=input()
order_file=input()

user_df=pd.read_csv(os.path.join(sys.path[0],user_file))
order_df=pd.read_csv(os.path.join(sys.path[0],order_file))

inner_df = pd.merge(user_df , order_df )
print(inner_df.shape)

left_df = pd.merge(user_df , order_df , how="left")
print(left_df.shape)