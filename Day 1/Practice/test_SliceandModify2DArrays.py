import os 
import sys 
import numpy as np

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)

def compute():
    dp=get_csv(input())
    print(dp.head(10))
    print()
    
    print("2D NumPy Array (first 10 rows - amount, discounted_amount, final_amount):")
    selected_dp=dp[['amount(INR)','discounted_amount(INR)','final_amount']]
    numpy_2d=selected_dp.to_numpy()
    numpy_2d=numpy_2d[0:10]
    print(numpy_2d)
    
    
    print()
    print("Sliced Array (first 5 rows, first 2 columns):")
    print(numpy_2d[0:5,0:2])
    
    print()
    print("Updated 2D Array (discounted_amount < 1200 set to 1200):")
    mask=numpy_2d[:,1] <1200 
    numpy_2d[mask , 1] = 1200
    print(numpy_2d)
    print()  

    avg_final_amount=np.mean(numpy_2d[:,2])
    avg_final_amount=round(avg_final_amount,2)
    print("Average Final Amount: ₹",avg_final_amount)

if __name__=='__main__':
    compute()

