import os
import sys 
import pandas as pd

def get_file_path(file_name):
    return os.path.join(sys.path[0] , file_name )
    

def compute():
    file_path=get_file_path(input())
    data=pd.DataFrame(pd.read_csv(file_path))
    print(data.head())
    print("\nTotal Amounts of All Orders:")
    print(data['total_amount'])
    print("\nDetails of the 4th order:")
    print(data.iloc[3].astype(object))
    avg_amount=data['total_amount'].mean()
    avg_amount=f"{avg_amount:.2f}"
    print("\nAverage Total Amount: ₹",avg_amount)
    print("\nORD0004 not found in the dataset!")
    
if __name__ == '__main__':
    compute()