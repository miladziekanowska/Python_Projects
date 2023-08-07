# This is a non-notebook version of 101 Numpy Excercises 
# If you wish to solve these on your own, please visit the link:
# https://www.machinelearningplus.com/python/101-numpy-exercises-python/

# 1. Importing numpy and printing version
import numpy as np
import sys
print(np.version.version)

# 2. Create a 1D array of numbers from 0 to 9
array_1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 3. Create a 3×3 numpy array of all True’s
bool_array = np.ones([3, 3], dtype=bool)

# 4. Extract all odd numbers from arr
array_4 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array_4 = array_4[array_4 % 2 == 1]  

# 5. Replace all odd numbers in arr with -1
array_5 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
array_5[array_5 % 2 == 1] = -1

# Q. Replace all odd numbers in arr with -1 without changing arr
array_6 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
out = np.where(array_6 % 2 == 1, -1, array_6)

# 7. Convert a 1D array to a 2D array with 2 rows
array_7 = np.arange(10)
array_7 = array_7.reshape(2, -1) # -1 automates the number of columns

# 8. Stack arrays a and b vertically
a8 = np.arange(10).reshape(2,-1)
b8 = np.repeat(1, 10).reshape(2,-1)
np.concatenate([a8, b8], axis=0)

# 9. Stack the arrays a and b horizontally.
a9 = np.arange(10).reshape(2,-1)
b9 = np.repeat(1, 10).reshape(2,-1)
np.concatenate([a9, b9], axis=1)

# 10. Create the following pattern without hardcoding. Use only numpy functions and the below input array a.
a10 = np.array([1,2,3])
a10 = np.r_[np.repeat(a10, 3), np.tile(a10, 3)]

# 11. Get the common items between a and b
a11 = np.array([1,2,3,2,3,4,3,4,5,6])
b11 = np.array([7,2,10,2,7,4,9,4,9,8])
np.intersect1d(a11, b11)

# 12. From array a remove all items present in array b
a12 = np.array([1,2,3,4,5])
b12 = np.array([5,6,7,8,9])
np.setdiff1d(a12, b12)

# 13. Get the positions where elements of a and b match
a13 = np.array([1,2,3,2,3,4,3,4,5,6])
b13 = np.array([7,2,10,2,7,4,9,4,9,8])
array_13 = np.where(a13==b13)

# 14. Get all items between 5 and 10 from a.
a14 = np.array([2, 6, 1, 9, 10, 3, 27])
a14[(a14 >= 5) & (a14 <= 10)]

# 15. Convert the function maxx that works on two scalars, to work on two arrays.
def maxx(x, y):
    if x >= y:
        return x
    else:
        return y

pair_max = np.vectorize(maxx, otypes=[float])

a15 = np.array([5, 7, 9, 8, 6, 4, 5])
b15 = np.array([6, 3, 4, 8, 9, 7, 1])

pair_max(a15, b15)

# 16. Swap columns 1 and 2 in the array arr.
array_16 = np.arange(9).reshape(3,3)
array_16[:, [1, 0]] = array_16[:, [0, 1]]

# 17. Swap rows 1 and 2 in the array arr:
array_17 = np.arange(9).reshape(3,3)
array_17[[1, 0],:] = array_17[[0, 1],:]

# 18. Reverse the rows of a 2D array arr.
array_18 = np.arange(9).reshape(3,3)
# or  array_18[::-1]
np.flip(array_18, axis=0)

# 19. Reverse the columns of a 2D array arr.
array_19 = np.arange(9).reshape(3,3)
np.flip(array_19, axis=1)
# or   array_19[:, ::-1]

# 20. Create a 2D array of shape 5x3 to contain random decimal numbers between 5 and 10.
array_20 = np.random.uniform(5,11, size=(5,3))

# 21. Print or show only 3 decimal places of the numpy array rand_arr.
array_21 = np.random.random((5,3))
np.round(array_21, decimals=3)

# 22. Pretty print rand_arr by suppressing the scientific notation (like 1e10)
np.random.seed(100)
array_22 = np.random.random([3,3])/1e3
np.set_printoptions(suppress=True, precision=6)

# 23. Limit the number of items printed in python numpy array a to a maximum of 6 elements.
array_23 = np.arange(15)
np.set_printoptions(threshold=6)

# 24. Print the full numpy array a without truncating.
# Input
np.set_printoptions(threshold=6)
a24 = np.arange(15)
# Solution
np.set_printoptions(threshold=sys.maxsize)

#25. Import the iris dataset keeping the text intact.
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data'
iris = np.genfromtxt(url, delimiter=',', dtype='object')
names = ('sepallength', 'sepalwidth', 'petallength', 'petalwidth', 'species')


# 26. Extract the text column species from the 1D iris imported in previous question.
columns_26 = iris[:5]


# more to come