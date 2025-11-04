import os 
import sys
import pandas as pd
filename=input()
file_path=os.path.join(sys.path[0],filename)

dp=pd.read_csv(file_path)

print("Enter the CSV filename (with .csv extension):")
print("---Orders DataFrame Loaded---")

print(dp.head())

print("Total Amounts of All Orders:")
print(dp['total_amount'])

print("Details of the 4th order:")
print(dp.loc[3])


avg_total=dp['total_amount'].mean()
print()
avg_total=round(avg_total,2)
print("Average Total Amount: ₹",avg_total)
print()



print("Updated details for ORD0004:")
dp.loc[dp['order_id']=='ORD0004' , ['payment_method'] ] = ["UPI"]
print(dp.loc[dp['order_id']=='ORD0004'])