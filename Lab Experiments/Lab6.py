# no csv file so no answer


# A school data analyst named Rehan has been provided with a dataset containing information about students’ demographics and their test scores.
# He wants to analyze students’ performance in Math, Reading, and Writing by calculating key statistical measures and relationships between the scores.
# Some students’ data may be incomplete, so your program should ignore rows with missing values before performing any calculations.
# Your task is to help Rehan by writing a Python program that:
# Reads the dataset input from the user.
# Removes rows with any missing values.
# Calculates and displays the Mean, Median, Mode, and Standard Deviation for Math Score, Reading Score, and Writing Score.
# Calculates the Correlation between these three score columns.

# To handle missing values use the code mentioned below:

# df.replace("", pd.NA, inplace=True)
# df.dropna(inplace=True)

# Also convert all the numeric columns to int using astype(int)

# Input format :
# First line taking data set as a input from the directory.

# Output format :
# Print statistical summary for numeric columns after removing rows with missing values in the form of data frame using row names as: Math Score, Reading Score,Writing Score Print correlation matrix for numeric columns after removing rows with missing values.


# Code constraints :
# 1 ≤ n ≤ 1000 math score, reading score, and writing score are integers (0 ≤ score ≤ 100) All categorical fields (gender, race/ethnicity, etc.) are strings. Dataset must have no missing values in numeric columns. Correlation values should be printed up to 2 decimal places.


# Sample test cases :
# Input 1 :
# sample1.csv
# Output 1 :

# Statistical Summary:
#                 Mean  Median  Mode  Standard Deviation
# Math Score     65.03    65.0    58               15.68
# Reading Score  67.91    69.0    64               15.51
# Writing Score  66.62    68.0    74               15.76

# Correlation Matrix:
#                math score  reading score  writing score
# math score           1.00           0.85           0.83
# reading score        0.85           1.00           0.96
# writing score        0.83
