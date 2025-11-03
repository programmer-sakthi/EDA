import os 
import sys 

import pandas as pd 

def get_csv(file):
    path=os.path.join(sys.path[0],file)
    return pd.read_csv(path)
    
def compute():
    users=get_csv(input())
    orders = get_csv(input())
    restaurants = get_csv(input())
    
if __name__=='__main__':
    compute()
    

    
    