import numpy as np 

arr=np.array(list(map(int,input("Enter total amounts for the first 10 orders separated by spaces:").split())))
ele=int(input())
print("\nOriginal array:",arr)
print("Amounts greater than ₹3250:",arr[arr>3250])
print("Second order amount:",arr[1])
print("Last order amount:",arr[-1])   
arr=np.append(arr,ele)   

print("Enter total amount for the 11th order: Array after adding 11th order:",arr)   

arr=arr.astype(float)   

arr[arr>3250] *= 0.9
print("Updated amounts after 10% discount on values > ₹3250:",arr)      
