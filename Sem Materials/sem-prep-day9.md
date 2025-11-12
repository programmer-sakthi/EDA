# YData Profiling to genmerate a report about data

## 1. **Install YData Profiling**

If you haven’t installed it yet, run:

```bash
pip install ydata-profiling
```

> **Note:** YData Profiling is the updated version of `pandas-profiling`.

---

## 2. **Import Libraries**

```python
import pandas as pd
from ydata_profiling import ProfileReport
```

---

## 3. **Load Your Dataset**

You can load any dataset using Pandas. For example:

```python
# Load CSV
df = pd.read_csv('your_dataset.csv')

# Or load from Excel
# df = pd.read_excel('your_dataset.xlsx')

# Check the first few rows
print(df.head())
```

---

## 4. **Generate the Profiling Report**

```python
profile = ProfileReport(df,
                        title="Dataset Profiling Report",
                        explorative=True)
```

**Parameters explained:**

- `title`: Sets the title of your report.
- `explorative=True`: Enables additional interactive analysis features.
- There are many other parameters you can customize, like `minimal=True` to generate a lighter report.

---

## 5. **Save the Report**

You can save the report as an HTML file:

```python
profile.to_file("dataset_report.html")
```

Or display it directly in a Jupyter Notebook:

```python
profile.to_widgets()  # interactive widgets
# or
profile.to_notebook_iframe()
```

---

## 6. **What the Report Includes**

The generated report contains:

- **Overview:** Number of variables, missing cells, duplicate rows, memory usage.
- **Variable Analysis:** Type, distinct values, missing values, summary statistics.
- **Correlations:** Pearson, Spearman, Kendall, and other correlations.
- **Missing Values Heatmap:** Visual patterns of missing data.
- **Warnings:** Detects constant columns, high correlations, or skewed distributions.

---

### ✅ Example Usage

```python
import pandas as pd
from ydata_profiling import ProfileReport

# Load dataset
df = pd.read_csv('titanic.csv')

# Generate report
profile = ProfileReport(df, title="Titanic Dataset Profiling", explorative=True)

# Save report
profile.to_file("titanic_report.html")
```

# Generating a report using sweetviz

Certainly! Here’s how you can generate a detailed profiling (EDA) report of a dataset using **Sweetviz** — very similar to how you’d do it with YData Profiling (formerly pandas‑profiling).

---

## ✅ Step‑by‑Step Guide for Sweetviz

### 1. Install Sweetviz

```bash
pip install sweetviz
```

Sweetviz is a Python library built on Pandas that “generates beautiful, high‑density visualizations to kick‑start EDA with just two lines of code.” ([PyPI][1])

### 2. Import the libraries & load your dataset

```python
import pandas as pd
import sweetviz as sv

df = pd.read_csv("your_dataset.csv")
print(df.head())
```

### 3. Generate the profiling report

#### For a single dataset:

```python
report = sv.analyze(df, target_feat="YourTargetColumn")  # target optional
report.show_html("sweetviz_report.html")
```

#### To compare two datasets (e.g., train vs test):

```python
report = sv.compare([df_train, "Train"], [df_test, "Test"], target_feat="YourTargetColumn")
report.show_html("sweetviz_compare.html")
```

Sweetviz supports comparisons and also target‑analysis (how a target relates to features).

### 4. View the report

- The HTML file ("sweetviz_report.html") will open in your browser and allow interactive exploration of distributions, missing data, correlations, target relationships.
- In Jupyter notebooks you can also use `report.show_notebook()` for inline display.

### 5. What the Sweetviz report includes

- Summary of each feature: type (numerical/categorical/text), missing values, distinct values, most frequent values.
- For numerical features: min/max, quartiles, mean, skewness, kurtosis, etc.
- For categorical features: unique count, top categories, distribution.
- Correlations / associations: numerical‑numerical (Pearson), categorical–categorical (uncertainty coefficient), categorical–numerical (correlation ratio) all handled.
- If comparing datasets: side‑by‑side comparison including differences in distributions & missingness.
- Target analysis (if target provided): how features relate to the target.

---

## 🔍 Example Code

```python
import pandas as pd
import sweetviz as sv

# load dataset
df = pd.read_csv("my_data.csv")

# generate report
report = sv.analyze(df, target_feat="Label")

# save report
report.show_html("my_data_sweetviz_report.html")
```

Or for comparison:

```python
df_train = pd.read_csv("train.csv")
df_test  = pd.read_csv("test.csv")

report_cmp = sv.compare([df_train, "Train"], [df_test, "Test"], target_feat="Label")
report_cmp.show_html("train_vs_test_report.html")
```

---

## 💡 Tips & Things to Watch

- Make sure your dataset is not **too large** (very many features or rows) because correlation / association calculations may become heavy. Sweetviz has a `pairwise_analysis` parameter (on/off) to manage heavy computations.
- For large datasets, you may want to sample or restrict features before generating a full report.
- If you have a “target” (a variable you plan to predict), it’s helpful to provide it to Sweetviz so you can get insights relative to that target.
- Use the report early in your pipeline to catch data quality issues: missing values, duplicates, weird distributions, data leakage (features that correlate too well maybe because they’re calculating indirectly the target). For example, one blog shows how Sweetviz helped discover a bug in “date” feature being overwritten.
- The HTML output is self‑contained and you can share with stakeholders.

# Generating a report using Autowiz

Certainly! If you meant the library **AutoViz** (from the AutoViML project by Ram Seshadri) rather than “Autowiiz”, here’s how to generate an automatic exploratory analysis / profiling‐style report using it.

---

### ✅ What AutoViz does

- Automatically creates visualizations (distributions, correlations, scatter‐plots) for a dataset with _very few lines of code_.
- It also provides some data‐quality / data‐visualization insights (though perhaps not as full‐feature as dedicated profiling libraries).
- Example use‐cases: quickly assess your dataset before modelling, identify outliers, distributions, target vs features.

---

### 🔧 Step‑by‑step guide

1. **Install the library**

   ```bash
   pip install autoviz
   ```

   (Or if needed: `pip install AutoViz` – check the correct package name)
   This is based on instructions in the GitHub README. ([GitHub][1])

2. **Import and load your data**

   ```python
   import pandas as pd
   from autoviz.AutoViz_Class import AutoViz_Class

   df = pd.read_csv("your_dataset.csv")
   ```

3. **Generate the automatic visualisation/report**

   ```python
   AV = AutoViz_Class()

   # If you have a target variable (e.g., for a prediction task):
   target = "YourTargetColumn"

   df2 = AV.AutoViz(
       filename="",        # set to "" if using a DataFrame directly
       sep=",",
       depVar=target,      # or "" if you don't have one
       dfte=df,
       header=0,
       verbose=1,
       lowess=False,
       chart_format="svg",
       max_rows_analyzed=150000,
       max_cols_analyzed=30,
       save_plot_dir="AutoViz_Plots"
   )
   ```

   If you don’t have a target variable:

   ```python
   df2 = AV.AutoViz("", sep=",", depVar="", dfte=df, header=0, verbose=1, lowess=False, chart_format="svg")
   ```

4. **Inspect the output**

   - AutoViz will generate a set of plot files (in the `"AutoViz_Plots"` directory if you specified that) showing: distributions of variables, pair‐wise scatter plots, correlations, etc. ([GitHub][1])
   - Use these visualizations to spot: skewed distributions, missing values, outliers, strong correlations (maybe multicollinearity), variable relationships with the target (if specified).

---

### ⚠️ Important notes / limitations

- AutoViz is great for _visual exploratory analysis_, but it's **not a full‐blown profiling library** like YData Profiling (formerly pandas‑profiling) or Sweetviz. For example, it may not generate a full HTML report with all the detailed metrics and warnings.
- If your dataset is very large (many rows, many columns), you may need to limit `max_rows_analyzed` or `max_cols_analyzed` to avoid performance issues. The docs mention sampling when needed. ([GitHub][1])
- Because it's automated, you may still want to complement it with manual checks (e.g., checking missing‑value patterns, domain‐specific logic) for thorough data profiling.

---

### 🧮 Example full snippet

Here’s a minimal example putting it all together:

```python
import pandas as pd
from autoviz.AutoViz_Class import AutoViz_Class

# Load data
df = pd.read_csv("my_data.csv")

# Initialize
AV = AutoViz_Class()

# Run AutoViz
report_df = AV.AutoViz(
    filename="",        # using DataFrame directly
    sep=",",
    depVar="",          # no target variable
    dfte=df,
    header=0,
    verbose=1,
    lowess=False,
    chart_format="svg",
    max_rows_analyzed=100000,
    max_cols_analyzed=20,
    save_plot_dir="AutoViz_Plots"
)

# The returned `report_df` is the DataFrame that was analyzed (possibly sampled).
print(report_df.head())
```

After this, go to the `AutoViz_Plots/` directory and open the generated plots (or embed in notebook) to explore.

---

# Comparison of Sweetviz and Autowiz and YData Profiling and Streamlit

# 📊 Comparison: YData Profiling vs Sweetviz vs AutoViz vs Streamlit

| Feature / Aspect                  | 🧠 **YData Profiling** (formerly _pandas-profiling_) | 🍬 **Sweetviz**                                                   | 🤖 **AutoViz**                                 | 🌐 **Streamlit (custom dashboard)**                                   |
| --------------------------------- | ---------------------------------------------------- | ----------------------------------------------------------------- | ---------------------------------------------- | --------------------------------------------------------------------- |
| **Purpose**                       | Automated **data profiling** & quality report        | Automated **EDA visualization** with comparison & target analysis | Automated **data visualization engine**        | **Interactive dashboard** for custom EDA (manual or embedded reports) |
| **Installation**                  | `pip install ydata-profiling`                        | `pip install sweetviz`                                            | `pip install autoviz`                          | `pip install streamlit` (+ optional libs)                             |
| **Primary Output**                | Full **HTML report** (summary + visuals + warnings)  | Full **HTML report** (EDA, comparisons, distributions)            | Collection of **plots and charts** in a folder | **Web app** (interactive charts, file uploads, dashboards)            |
| **UI Type**                       | Static or interactive **HTML**                       | Static or interactive **HTML**                                    | Plots (saved or inline)                        | Fully interactive **web app**                                         |
| **Interactivity**                 | ✅ High (explorative mode)                           | ✅ Moderate (scrollable HTML)                                     | ⚙️ Limited (static plots)                      | 🧩 High (customizable filters, widgets)                               |
| **Target Variable Analysis**      | ✅ Yes (auto-detects if specified)                   | ✅ Yes (visualizes relation to target)                            | ✅ Yes (if `depVar` set)                       | ✅ If manually implemented                                            |
| **Data Comparison**               | ⚙️ Limited                                           | ✅ Built-in (compare train/test)                                  | ⚙️ Limited                                     | ✅ Fully customizable                                                 |
| **Missing Value Analysis**        | ✅ Built-in (heatmaps, summaries)                    | ✅ Displays missing counts                                        | ⚙️ Partial                                     | ✅ If coded manually                                                  |
| **Correlation Analysis**          | ✅ Pearson, Spearman, Kendall, Phik                  | ✅ Several types (Pearson, uncertainty coeff.)                    | ✅ Correlation heatmaps                        | ✅ If coded manually                                                  |
| **Text Analysis**                 | ✅ Yes (frequency, lengths, categories)              | ⚙️ Basic                                                          | ❌ None                                        | ✅ If coded manually                                                  |
| **Visual Style**                  | Clean, professional report                           | Vibrant, infographic-like                                         | Analytical plots (matplotlib/seaborn)          | User-defined (Plotly, Seaborn, Altair)                                |
| **Performance (Large Datasets)**  | ⚠️ Can be slow for very large datasets               | ⚠️ Slower on large datasets                                       | ✅ Better scaling (sampling)                   | ✅ Depends on design                                                  |
| **Ease of Use**                   | ⭐⭐⭐⭐☆                                            | ⭐⭐⭐⭐☆                                                         | ⭐⭐⭐☆☆                                       | ⭐⭐⭐⭐☆ (depends on code)                                           |
| **Integration in Notebooks**      | ✅ `to_notebook_iframe()`                            | ✅ `show_notebook()`                                              | ✅ Works inline                                | ✅ Via `streamlit run` (browser)                                      |
| **Integration with Streamlit**    | ✅ Embed HTML report                                 | ✅ Embed HTML report                                              | ✅ Display plots / folder                      | ⚙️ Native (built with Streamlit)                                      |
| **Best For**                      | Full, detailed **data audit report**                 | Quick, visual **EDA with comparisons**                            | Fast **auto visualization** of large datasets  | Building a **custom interactive EDA tool**                            |
| **Output File**                   | `*.html`                                             | `*.html`                                                          | `AutoViz_Plots/*`                              | Web app (`.py` script)                                                |
| **Example Run Time (Medium CSV)** | ~1–3 mins                                            | ~1–2 mins                                                         | ~30–60 sec                                     | Depends on dashboard code                                             |
| **Customization Level**           | Medium (parameters)                                  | Low                                                               | Medium                                         | Very High                                                             |
| **Open Source**                   | ✅ Yes                                               | ✅ Yes                                                            | ✅ Yes                                         | ✅ Yes                                                                |
| **Key Strength**                  | Deep statistical profiling + warnings                | Train/Test comparison + target analysis                           | Handles large data quickly                     | Fully flexible and interactive                                        |
| **Key Limitation**                | Heavy on large data                                  | Less statistical detail                                           | Limited text/missing analysis                  | Requires manual coding                                                |

---

## 🧭 Quick Recommendations

| Scenario                                            | Recommended Tool    | Why                                                     |
| --------------------------------------------------- | ------------------- | ------------------------------------------------------- |
| 🧩 Want **one-click comprehensive data audit**      | **YData Profiling** | Most complete & professional profiling report           |
| ⚖️ Want **comparison between train/test sets**      | **Sweetviz**        | Built-in dataset comparison + target analysis           |
| ⚡ Need **fast visualization for large data**       | **AutoViz**         | Lightweight and optimized sampling                      |
| 🌐 Want an **interactive, shareable app/dashboard** | **Streamlit**       | Customizable, deployable, and supports embedding others |
