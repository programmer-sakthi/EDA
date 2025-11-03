import pandas as pd 

# checking pandas version 
print(pd.__version__)

# creating a series 
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

# creating a dataframe 
df = pd.DataFrame({
    'A': 1,
    'B': 2,
    'C': 3,
    'D': 4,
    'E': 5
})
print(df)

# reading a csv file 
df = pd.read_csv('coffee_sales.csv')
print(df)

# display first 5 rows 
print(df.head())

# display last 5 rows 
print(df.tail())



