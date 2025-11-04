import os 
import sys 

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)

def compute():
    df=get_csv(input())
    print("Initial DataFrame Preview")
    print(df.head())
    
    print()
    print("Missing Values Count")
    missing=df.isnull()
    print(missing.sum())
    
    print()
    print("Dropped rows with missing 'cuisine_type'.")
    print()
    print("DataFrame After Dropping Missing Values")
    
    df = df.dropna(subset = ['cuisine_type'])
    print(df.head())
    
    missing=df.isnull()
    print("Final Missing Values Count")
    print(missing.sum())
    
    
if __name__=='__main__':
    compute()
