import pandas as pd 

# checking pandas version 
print(pd.__version__)

# Series 

# series is a one-dimensional array-like object containing a sequence of values

data = [100,200,300,400,'a']
s = pd.Series(data )
print(s)
s=pd.Series(data,index=['a','b','c','d','e'])
print(s)

# loc is used to access a group of rows and columns by label(s) or a boolean array.
print(s.loc['a']) 
print(s.loc['b':'d'])
print
s.loc['a':'c']=1000
print(s)





