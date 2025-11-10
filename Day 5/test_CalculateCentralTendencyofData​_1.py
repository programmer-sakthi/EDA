# 2nd question not solved ~ fucking tired to do stupid charts ^_^

import os 
import sys 

import pandas as pd 

def get_csv(file):
  path=os.path.join(sys.path[0],file)
  return pd.read_csv(path)
  
def compute():
  
  df = get_csv(input())
  filtered = df[df['order_status'] == 'Completed']
  mean = filtered['total_amount'].mean()
  median = filtered['total_amount'].median()
  mode = filtered['total_amount'].mode()[0]
  
#   mean = f"{mean:.2f}"
#   median = f"{median:.2f}"
  print("Central Tendency Measures of order amounts (₹):")
  print("Mean:",round(mean,2))
  print("Median:",median)
  print("Mode:",mode)
  
  
  print("Summary Statistics of Order Amounts:")
  summary = filtered['total_amount'].describe()
  print(summary)
  
if __name__=='__main__':
  compute()
  

  
  
