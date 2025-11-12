import numpy as np


cityA = np.array(list(map(float, input().split())))
cityB = np.array(list(map(float, input().split())))

# Create 2D array where rows = cities, columns = days
temp_array = np.array([cityA, cityB])

# Find hottest day (0-indexed) for each city
hottest_days = np.argmax(temp_array, axis=1)

# Transpose and flatten
transposed = temp_array.T
flattened = transposed.flatten()

# Display results
print("2D Temperature Array (Cities x Days):", temp_array)
print("Hottest day (0-indexed) for each city:", hottest_days)
print("Transposed Array (Days x Cities):", transposed)
print("Flattened 1D Array:", flattened)


# A data entry operator collects daily temperatures for a week (7 days) from two different cities (City A and City B). You are asked to process this data:
# Take user input for temperatures of each day for both cities as two separate 1D NumPy arrays.
# Create a 2D NumPy array where each row represents a city and each column a day.
# Manipulate the 2D array to:
# Find the hottest day (day number) for each city.
# Transpose the 2D array and flatten it into a 1D array.

# Input format :
# 7 daily temperatures for City A 7 daily temperatures for City B

# Output format :
# 2D NumPy array of shape (2, 7) representing the temperatures. An array indicating the hottest day (0-indexed, 0 = first day) for each city.

# The transposed 2D array. The flattened version (1D array) of the transposed array.

# Code constraints :
# Use only NumPy for array creation and manipulation. Temperatures should be floats (can include decimals). Each array must have exactly 7 values, one for each day

# Sample test cases :
# Input 1 :
# 22.5 23.0 21.8 24.1 25.3 26.0 24.7
#  21.2 22.8 22.4 23.9 24.8 25.1 25.0
# Output 1 :

# 2D Temperature Array (Cities x Days):
# [[22.5 23.  21.8 24.1 25.3 26.  24.7]
#  [21.2 22.8 22.4 23.9 24.8 25.1 25. ]]

# Hottest day (0-indexed) for each city:
# [5 5]

# Transposed Array (Days x Cities):
# [[22.5 21.2]
#  [23.  22.8]
#  [21.8 22.4]
#  [24.1 23.9]
#  [25.3 24.8]
#  [26.  25.1]
#  [24.7 25. ]]

# Flattened 1D Array:
# [22.5 21.2 23.  22.8 21.8 22.4 24.1 23.9 25.3 24.8 26.  25.1 24.7 25. ]
