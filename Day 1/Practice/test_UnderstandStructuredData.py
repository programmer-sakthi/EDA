import os 
import sys 
import pandas as pd
import numpy as np


def get_file_path(file_name):
    return os.path.join(sys.path[0],file_name)
    
def compute():
    file_path=get_file_path(input())
    dp=pd.read_csv(file_path)
    print(dp.head())
    first_10_ele=dp['final_amount'].head(10).to_numpy()
    
    print("NumPy Array of First 10 final_amount values:")
    print(first_10_ele)
    print("Shape:",first_10_ele.shape)
    print("Data type:",first_10_ele.dtype)
    first_10_ele=np.where(first_10_ele<500 , first_10_ele+50 ,first_10_ele )
    print("Updated final_amounts array (values < 500 increased by 50):")
    print(first_10_ele)
    
    print()
    
    print("Explanation: Used np.where() to conditionally add 50 to values under 500.")
    
    print()
    
    print("Columns of Payments DataFrame:",dp.columns.tolist())
    print("Data types of columns:\n",dp.dtypes)
    
    print()
    
    print("a) Payment Method and Final Amount columns:")
    print(dp[['payment_method','final_amount']])
    
    print()
    print("b) Records with payment_method as 'Credit Card':")
    
    credit_card=dp[dp['payment_method']=='Credit Card']
    print(credit_card)
    
    print()
    total_discount=dp['discounted_amount(INR)'].sum()
    total_discount=f"{total_discount:.2f}"
    print("c) Total Discounted Amount across all transactions: ₹",total_discount)
    
if __name__=='__main__':
    compute()