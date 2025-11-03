import numpy as np 

# checking numpy version 
print(np.__version__)

# creating a 0D array aka Scalar 
arr = np.array(42)
print(arr)
print(type(arr))

# creating an 1D array using numpy 
arr = np.array((1, 2, 3, 4, 5))  # you can also pass a tuple to this 
print(arr)
print(type(arr))   #arrays created using numpy will have the type ndarray 



# creating a 2D array
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(type(arr))

# creating a 3D array
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr)
print(type(arr))

# data types in ndarray 
arr = np.array([1, 2, 3, 4, 5], dtype='S')
print(arr)
print(arr.dtype)


# finding the dimension of the array
print(arr.ndim)

#finding the shape of the array
print(arr.shape)

# matrix multiplication 
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])
print(np.dot(a, b))

# numpy array indexing 

# multi dimensional indexing 
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr[0])
print(arr[0,0])
print(arr[0, 0, 0])

# 1D array indexing 
arr = np.array([1, 2, 3, 4, 5])
print(arr[0])


# Slice arrays 

# 1D array slicing 
arr = np.array([1, 2, 3, 4, 5])
print(arr[1:5])

# 2D array slicing 
arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr[0:2, 0:2]) #prints the first two rows and first two columns
print(arr[ : , 1]) #prints the second column


# Scalar Arithmetic 
arr = np.array([1, 2, 3, 4, 5])
print(arr + 1)
print(arr - 1)
print(arr * 2)
print(arr / 2)
print(arr % 2)
print(arr ** 2)


# Vectorized math operations 

arr=np.array([1.4, 2.3, 3.2, 4.1, 5.0])
print(np.sqrt(arr))
print(np.floor(arr))
print(np.ceil(arr))
print(np.exp(arr))
print(np.pi)


# Element wise arithmetic 

arr1 = np.array([1, 2, 3, 4, 5])
arr2 = np.array([6, 7, 8, 9, 10])
print(arr1 + arr2)
print(arr1 - arr2)
print(arr1 * arr2)
print(arr1 / arr2)
print(arr1 % arr2)
print(arr1 ** arr2)


# Comparision Operators 

scores = np.array([1, 2, 3, 4, 5])
print(scores > 3)
print(scores >= 3)
print(scores < 3)
print(scores <= 3)
print(scores == 3)
print(scores != 3)

scores[scores > 3] = 0
print(scores)


# Aggregate functions 

print(np.sum(arr))   # returns sum 
print(np.mean(arr))  # returns mean 
print(np.max(arr))   # returns max 
print(np.min(arr))   # returns min 
print(np.std(arr))   # returns standard deviation 
print(np.var(arr))   # returns variance 
print(np.argmin(arr))   # returns index of min 
print(np.argmax(arr))   # returns index of max

# Aggregate functions on 2D arrays 

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(np.sum(arr, axis=0))   # returns sum of each column 
print(np.sum(arr, axis=1))   # returns sum of each row 


# Filtering

ages = np.array([1, 2, 3, 4, 5])
print(ages[ages > 3]) # boolean indexing 
two_d_ages = np.array([[1, 2, 3], [4, 5, 6]])
print(two_d_ages[two_d_ages > 3])

print(two_d_ages[ (two_d_ages > 3) | (two_d_ages < 9)])
print(two_d_ages[ (two_d_ages > 3) & (two_d_ages < 9)])

new_ages = np.where(two_d_ages > 3, 1, 0)
print(new_ages)

# Random Numbers
# Generate a single random number from a uniform distribution between 0 and 1
print(np.random.rand())

# Generate a sample of 5 random numbers from a normal distribution with mean 0 and standard deviation 1
print(np.random.randn(5))

# Generate a sample of 5 random numbers from a uniform distribution between 0 and 1
print(np.random.rand(5))

# Generate a sample of 5 random integers between 0 and 10
print(np.random.randint(0, 11, 5))

# Generate a sample of 5 random integers between 0 and 4
print(np.random.choice(5, 5))




# Broadcasting:
# Rules:
# 1. If the arrays differ in their number of dimensions, the shape of the
#    arrays is padded with ones on the left side up to the maximum number of
#    dimensions.
# 2. Arrays are broadcast together element wise.
# 3. Size 1 dimensions can be pre-pended to either array in order to make the
#    arrays broadcastable.

arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([4, 5, 6])
print(arr1 + arr2)

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4, 5, 6]])
print(arr1 + arr2)

arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4], [5], [6]])
print(arr1 + arr2)



# Broadcasting rules can be overridden by using the `newaxis` attribute.
arr1 = np.array([[1, 2, 3]])
arr2 = np.array([[4], [5], [6]])[:, np.newaxis]
print(arr1 + arr2)







