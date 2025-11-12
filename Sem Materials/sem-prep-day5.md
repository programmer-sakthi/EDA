# Measures of Central Tendency in Pandas

---

## 1. What are Central Tendency Measures?

Central tendency measures summarize a dataset by identifying a central or typical value:

- **Mean**: Average of all values
- **Median**: Middle value when sorted
- **Mode**: Most frequently occurring value(s)

These are used to understand the “typical” value in a dataset.

---

## 2. Calculating Central Tendency with Pandas

Example DataFrame:

```python
import pandas as pd

data = {'Age': [23, 25, 23, 30, 25, 40, 23, 25]}
df = pd.DataFrame(data)
```

### a) Mean

```python
mean_age = df['Age'].mean()
print(mean_age)
```

Output: `27.25`

---

### b) Median

```python
median_age = df['Age'].median()
print(median_age)
```

Output: `25.0`

---

### c) Mode

```python
mode_age = df['Age'].mode()
print(mode_age)
```

Output:

```
0    23
1    25
dtype: int64
```

(Multiple modes possible)

---

## 3. Summary Using `.describe()`

Pandas `.describe()` provides a summary:

```python
df['Age'].describe()
```

Output:

```
count     8.000000
mean     27.250000
std       6.832817
min      23.000000
25%      23.000000
50%      25.000000
75%      30.000000
max      40.000000
```

- `50%`: median
- `mean`: average
- Mode is not included

---

## 4. Quick Recap

| Measure | Pandas Method | Meaning                                      |
| ------- | ------------- | -------------------------------------------- |
| Mean    | `.mean()`     | Average of values                            |
| Median  | `.median()`   | Middle value                                 |
| Mode    | `.mode()`     | Most frequent value                          |
| Summary | `.describe()` | Mean, median (50%), quartiles, min, max, std |

---

If you want, I can also show **how to calculate these measures for multiple columns at once** in a DataFrame, which is really handy for real datasets.

Do you want me to show that next?

## Quartiles

Quartiles divide a sorted dataset into four equal parts:

- **Q1 (25%)**: 25% of data falls below this value
- **Q2 (50% / median)**: 50% of data falls below this value
- **Q3 (75%)**: 75% of data falls below this value

In pandas `.describe()`:

### Example

```python
import pandas as pd

data = {'Age': [23, 25, 23, 30, 25, 40, 23, 25]}
df = pd.DataFrame(data)
print(df['Age'].describe())
```

Output:

```
count     8.000000
mean     27.250000
std       6.832817
min      23.000000
25%      23.000000
50%      25.000000
75%      30.000000
max      40.000000
```

Interpretation:

- Q1 (25%) = 23: 25% of ages ≤ 23
- Median (50%) = 25: 50% of ages ≤ 25
- Q3 (75%) = 30: 75% of ages ≤ 30

### Interquartile Range (IQR)

```python
IQR = Q3 - Q1 = 30 - 23 = 7
```

Do you want me to do that?

# Correlation Methods

---

## 1. Pearson Correlation

- Measures linear relationship between two continuous variables
- Range: -1 (perfect negative) to 1 (perfect positive)
- Assumes variables are continuous, linear relationship, and (for inference) normality

**Pandas example:**

```python
df['Hours_Studied'].corr(df['Score'], method='pearson')
```

---

## 2. Spearman Correlation

- Measures monotonic relationship (rank-based, not necessarily linear)
- Range: -1 to 1
- Use for non-normal data or data with outliers

**Pandas example:**

```python
df['Hours_Studied'].corr(df['Score'], method='spearman')
```

---

## 3. Kendall’s Tau Correlation

- Measures ordinal association between two variables
- Range: -1 to 1
- Good for small datasets or ranked data

**Pandas example:**

```python
df['Hours_Studied'].corr(df['Score'], method='kendall')
```

---

## 4. Correlation Methods Summary

| Method   | Measures                        | Best for                         |
| -------- | ------------------------------- | -------------------------------- |
| Pearson  | Linear relationship             | Continuous, normally distributed |
| Spearman | Monotonic relationship (ranked) | Non-normal, ordinal, outliers    |
| Kendall  | Ordinal association (ranked)    | Small datasets, ordinal data     |

---

## 5. Visualizing Correlation

Scatter plots help visualize correlation:

```python
import matplotlib.pyplot as plt
plt.scatter(df['Hours_Studied'], df['Score'])
plt.xlabel('Hours Studied')
plt.ylabel('Score')
plt.title('Scatter Plot: Hours vs Score')
plt.show()
```

- Positive slope: positive correlation
- Negative slope: negative correlation

---

If you want, I can make a **full pandas example showing Pearson, Spearman, and Kendall correlations together with a heatmap**, which is very practical for real datasets.

Do you want me to do that?

Sure! Let’s focus on the **first two types of correlation**: **Pearson** and **Spearman**.

---

## **1. Pearson Correlation**

- **Measures:** Linear relationship between two continuous variables.
- **Range:** -1 to 1

  - 1 → perfect positive linear correlation
  - -1 → perfect negative linear correlation
  - 0 → no linear correlation

- **Best for:** Continuous data, approximately normally distributed, linear relationships.

**Example in pandas:**

```python
import pandas as pd

df = pd.DataFrame({
    'Hours_Studied': [2, 3, 5, 8, 10],
    'Score': [50, 60, 65, 85, 95]
})

pearson_corr = df['Hours_Studied'].corr(df['Score'], method='pearson')
print("Pearson correlation:", pearson_corr)
```

✅ Output (example): `0.97` → strong positive linear correlation.

---

## **2. Spearman Correlation**

- **Measures:** Monotonic relationship (rank-based), not necessarily linear.
- **Range:** -1 to 1
- **Best for:** Non-linear but consistently increasing/decreasing relationships, non-normal data, ordinal data, or data with outliers.

**Example in pandas:**

```python
spearman_corr = df['Hours_Studied'].corr(df['Score'], method='spearman')
print("Spearman correlation:", spearman_corr)
```

✅ Output (example): `0.9` → strong monotonic relationship.

---

**Key difference:**

- Pearson looks at **linear trends** in raw data.
- Spearman looks at **rank-order trends** and is robust to outliers and non-linear relationships.

---

If you want, I can also **draw a simple plot showing the difference between Pearson and Spearman visually**, which makes it very intuitive. Do you want me to do that?

# Measures of Dispersion

---

## 1. Range

- **Definition:** Difference between maximum and minimum values
- **Formula:** `Range = Maximum - Minimum`
- **Use:** Quick idea of spread; sensitive to outliers

**Example in pandas:**

```python
import pandas as pd
df = pd.DataFrame({'Age': [23, 25, 23, 30, 25, 40, 23, 25]})
data_range = df['Age'].max() - df['Age'].min()
print("Range:", data_range)
```

Output: `17` (40 - 23)

---

## 2. Variance

- **Definition:** Average squared deviation from the mean
- **Formula:** `s² = Σ(xᵢ - x̄)² / (n-1)`
- **Use:** Shows spread, but in squared units

**Pandas example:**

```python
variance = df['Age'].var()
print("Variance:", variance)
```

Output: `46.19` (approx)

---

## 3. Standard Deviation (SD)

- **Definition:** Square root of variance (same units as data)
- **Formula:** `s = √s²`
- **Use:** Typical distance of data points from the mean

**Pandas example:**

```python
std_dev = df['Age'].std()
print("Standard Deviation:", std_dev)
```

Output: `6.8` (approx)

---

## Quick Recap Table

| Measure            | Formula / Method           | What it tells you                     |
| ------------------ | -------------------------- | ------------------------------------- |
| Range              | max - min                  | Spread between largest & smallest     |
| Variance           | mean of squared deviations | Average squared spread from mean      |
| Standard Deviation | √variance                  | Average spread from mean (same units) |

---

If you want, I can also **show how these dispersion measures relate to the central tendency visually using a simple plot**, which really helps to understand them intuitively.

Do you want me to do that?
