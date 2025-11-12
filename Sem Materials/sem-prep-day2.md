# EDA Sem prep DAY - 1

## What is pandas

pandas is a library for data analysis and data manipulation.
It is built on top of Numpy and provides data structures and functions needed to work with structured data.

## Why pandas

1. It is fast
2. It is easy to use
3. It is free and open source
4. It is cross platform
5. It is easy to learn
6. It is easy to use

## Difference between pandas and numpy

We prefer pandas to work with numerical data as it provides data structures and functions needed to work with structured data.
Pandas allows labeling of data which is not possible in numpy.
Pandas consume more memory than numpy.
Pandas is slower than numpy.
Pandas : DataFrames and Series
Numpy : Arrays

## Panda Series

A Pandas Series is a one-dimensional array-like object that can hold data of any type (integer, float, string, etc.). It is labelled, meaning each element has a unique identifier called an index. You can think of a Series as a column in a spreadsheet or a single column of a database table. Series are a fundamental data structure in Pandas and are commonly used for data manipulation and analysis tasks. They can be created from lists, arrays, dictionaries, and existing Series objects. Series are also a building block for the more complex Pandas DataFrame, which is a two-dimensional table-like structure consisting of multiple Series objects.

## Panda DataFrame

A Pandas DataFrame is a two-dimensional table-like structure that can hold data of any type (integer, float, string, etc.). It is labelled, meaning each element has a unique identifier called an index. You can think of a DataFrame as a spreadsheet or a database table. DataFrames are a fundamental data structure in Pandas and are commonly used for data manipulation and analysis tasks. They can be created from lists, arrays, dictionaries, and existing DataFrames objects. DataFrames are also a building block for the more complex Pandas Panel, which is a three-dimensional table-like structure consisting of multiple DataFrames objects.

## Difference between Series and DataFrame

| **Feature**          | **Series**                         | **DataFrame**                 |
| -------------------- | ---------------------------------- | ----------------------------- |
| **Dimension**        | One-dimensional                    | Two-dimensional               |
| **Homogeneity**      | Elements must be homogeneous       | Can be heterogeneous          |
| **Mutability**       | Immutable (size cannot be changed) | Mutable (size can be changed) |
| **Computation Type** | Element-wise computations          | Column-wise computations      |
| **Functionality**    | Functionality is less              | Functionality is more         |
| **Alignment**        | Alignment not supported            | Alignment is supported        |

## Installation

```bash
pip install pandas
```

## Importing pandas

```python
import pandas as pd
```

## Creating pandas DataFrame

```python
df = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 34, 42],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})
```

## Accessing pandas DataFrame

```python
df['Name']
df['Age']
df['City']
```

## Slicing pandas DataFrame

```python
df[0:2]
```

## Updating pandas DataFrame

```python
df['Age'] = df['Age'] + 1
```

## Deleting pandas DataFrame

```python
df.drop('Age', axis=1)
```

## Filtering pandas DataFrame

```python
df[df['Age'] > 30]
```

## Sorting pandas DataFrame

```python
df.sort_values('Age', ascending=False)
```

## Grouping pandas DataFrame

```python
df.groupby('City').sum()
```

## Merging pandas DataFrame

```python
df1 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 34, 42]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})
df = pd.merge(df1, df2, on='Name')
```

## Types of Merge

1. Inner Merge - Common rows
2. Outer Merge - All rows ( missing values as NaN )
3. Left Merge - Left table rows ( missing values as NaN )
4. Right Merge - Right table rows ( missing values as NaN )

### Inner Merge

```python
df1 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'Age': [28, 22, 34, 42]
})
df2 = pd.DataFrame({
    'Name': ['John', 'Anna', 'Peter', 'Linda'],
    'City': ['New York', 'Paris', 'Berlin', 'London']
})
df = pd.merge(df1, df2, on='Name', how='inner') # default merge ( no need to use how parameter )
```

### Outer Merge

```python
df = pd.merge(df1, df2, on='Name', how='outer')
```

### Left Merge

```python
df = pd.merge(df1, df2, on='Name', how='left')
```

### Right Merge

```python
df = pd.merge(df1, df2, on='Name', how='right')
```

## 🧽 2. Removing Missing Values

```python
df.dropna()               # Remove rows with any missing values
df.dropna(axis=1)         # Remove columns with any missing values
df.dropna(how='all')      # Remove rows only if all values are missing
df.dropna(subset=['Name', 'Age'])  # Keep rows only if certain columns are non-null
```

---

## 🪣 3. Filling Missing Values

```python
df.fillna(0)  # Fill missing values with a specific value

# Fill missing values with the mean of a column
df['Age'].fillna(df['Age'].mean(), inplace=True)

# Forward fill (propagate previous value forward)
df.fillna(method='ffill')

# Backward fill (use next valid value)
df.fillna(method='bfill')
```

---

## ⚙️ 4. Replacing Specific Values

```python
df.replace('?', np.nan, inplace=True)
```

---

## 📊 5. Checking for Any Missing Values in the Entire DataFrame

```python
df.isnull().values.any()
```
