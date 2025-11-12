# EDA Sem prep DAY - 1

## What is EDA

EDA (Exploratory Data Analysis) is a process of analyzing and visualizing data to understand the underlying patterns, relationships, and trends.

## Why EDA

EDA is important because it helps us to understand the data and make better decisions. It also helps us to identify the relationships between variables and make predictions.

## EDA Process

1. Data Collection
2. Data Cleaning
3. Data Analysis
4. Data Visualization
5. Data Interpretation

## EDA in Python

Python is extensively used for EDA.
It has wide variety of libraries for EDA.

### Libraries for EDA

1. NumPy
2. pandas
3. Matplotlib
4. Seaborn
5. Scipy
6. Plotly
7. Sweetviz

## Numpy

Numpy is a library for numerical computing.
It is used for scientific computing and data analysis.

### Why numpy ?

1. It is fast
2. It is easy to use
3. It is free and open source
4. It is cross platform
5. It is easy to learn
6. It is easy to use

### How does numpy work faster than normal python lists ?

Numpy uses arrays instead of lists.
Arrays are faster than lists.
⚙️ 1. Built in C (not pure Python)

NumPy is written in C, a low-level compiled language.
So, when you use NumPy functions, they run C code under the hood, which is much faster than Python’s interpreted loops.

🧮 2. Vectorized operations

NumPy performs calculations on entire arrays at once, instead of looping through elements one by one.
This means that complex operations happen in a single, optimized step — without the slow overhead of Python’s loops.

🧱 3. Contiguous memory storage

In a NumPy array, all data is stored in one continuous block of memory.
This allows the computer’s processor to quickly access data in sequence, taking full advantage of the CPU’s cache.
By contrast, Python lists store data in scattered memory locations, which slows things down.

🧠 4. Fixed and efficient data types

Every NumPy array has a single, fixed data type (e.g., all floats or all integers).
Because of this, NumPy doesn’t need to check the data type of every element during calculations — it already knows what to expect.
This makes operations more predictable and efficient.

⚡ 5. Uses optimized mathematical libraries

NumPy connects to powerful mathematical libraries such as:

BLAS (Basic Linear Algebra Subprograms)

LAPACK (Linear Algebra Package)

Intel MKL (Math Kernel Library)

These libraries are highly tuned to make use of your computer’s hardware, performing many operations at once using vectorized CPU instructions.

🔄 6. Broadcasting

NumPy can automatically “expand” smaller arrays to match the size of larger ones during operations.
This eliminates the need for manual looping or resizing and speeds up computations while keeping the code simple.

### Installation

```bash
pip install numpy
```

### Importing Numpy

```python
import numpy as np
```

### Creating Numpy Arrays

```python
arr = np.array([1, 2, 3, 4, 5])
```

### Numpy Array Attributes

```python
arr.shape
arr.dtype
arr.size
arr.ndim
arr.itemsize
arr.data
```

### Numpy Array Operations

```python
arr + arr
arr - arr
arr * arr
arr / arr
```

### converting data type of numpy array

```python
arr = arr.astype(float)
```

### Appending to numpy array

```python
arr = np.append(arr, 6)
```

### updating based on condition

```python
arr[arr > 3] *= 2
```

### Slicing numpy array

```python
arr[1:4]
```

### working with 2d numpy arrays

```python
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
```

```python
arr[1, 2] # returns 6
```

```python
arr[1:3, 0:2]  # returns [[4, 5], [7, 8]]
```
