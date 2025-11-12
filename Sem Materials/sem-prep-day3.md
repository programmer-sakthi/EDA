# CRUD Operations in Pandas DataFrames

CRUD stands for **Create, Read, Update, and Delete**—the four basic operations for managing data. In pandas, DataFrames make these operations easy and efficient.

---

## 1. Create DataFrame

You can create a DataFrame from dictionaries, lists, or arrays.

```python
import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Paris', 'London']
}
df = pd.DataFrame(data)
```

---

## 2. Read (Access) Data

- **Access columns:**

```python
df['Name']
```

- **Access rows by index:**

```python
df.loc[0]       # By label
# or
df.iloc[0]      # By position
```

- **Access multiple columns/rows:**

```python
df[['Name', 'Age']]
df.loc[0:1]     # Rows 0 and 1
```

---

## 3. Update Data

- **Update column values:**

```python
df['Age'] = df['Age'] + 1
```

- **Update specific cell:**

```python
df.at[1, 'City'] = 'Berlin'
```

- **Update based on condition:**

```python
df.loc[df['Name'] == 'Alice', 'Age'] = 28
```

---

## 4. Delete Data

- **Delete a column:**

```python
del df['City']
# or
df.drop('City', axis=1, inplace=True)
```

- **Delete a row:**

```python
df.drop(1, axis=0, inplace=True)  # Delete row with index 1
```

- **Delete rows based on condition:**

```python
df = df[df['Age'] > 28]  # Keep only rows where Age > 28
```

---

## 5. Add Data (Rows/Columns)

- **Add a new column:**

```python
df['Country'] = ['USA', 'France', 'UK']
```

- **Add a new row:**

```python
df.loc[len(df)] = ['David', 40, 'Madrid', 'Spain']  # If columns are Name, Age, City, Country
```

---

## 6. Resetting and Setting Index

- **Reset index:**

```python
df.reset_index(drop=True, inplace=True)
```

- **Set a column as index:**

```python
df.set_index('Name', inplace=True)
```

---

## Summary Table

| Operation | Method/Function | Example |
|-----------|-----------------|---------|
| Create    | pd.DataFrame    | pd.DataFrame(data) |
| Read      | df['col'], df.loc[] | df['Name'], df.loc[0] |
| Update    | df.at[], df.loc[]   | df.at[1, 'City'] = 'Berlin' |
| Delete    | df.drop(), del      | df.drop('City', axis=1) |

---

**Tip:** Always use `inplace=True` in functions like `drop()` if you want to modify the DataFrame directly, otherwise a new DataFrame is returned.
