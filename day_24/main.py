# Repeat all the examples in https://github.com/Asabeneh/30-Days-Of-Python/blob/master/24_Day_Statistics/24_statistics.md
from numpy import *
from random import *
from matplotlib.pyplot import *
import seaborn as sns
import numpy as np
import random
from scipy import *
from statistics import *

# Creating int numpy arrays
python_list = [1,2,3,4,5]
two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]

numpy_array_from_list = array(python_list)
print(numpy_array_from_list)

# Creating float numpy arrays
numy_array_from_list2 = array(python_list, dtype=float)
print(numy_array_from_list2)

# Creating boolean numpy arrays
bool_list = [0,1,-1,0,0]
numpy_bool_array = array(bool_list, dtype=bool)
print(numpy_bool_array)

# Creating multidimensional array using numpy
numpy_two_dimensional_list = array(two_dimensional_list)
print(numpy_two_dimensional_list)

# Converting numpy array to list
print(numpy_array_from_list.tolist())
print(numpy_two_dimensional_list.tolist())

# Creating Numpy array from tuple
python_tuple = (1,2,3,4,5)
numpy_array_from_tuple = array(python_tuple)
print(numpy_array_from_tuple)

# Shape of numpy array
nums = array([1, 2, 3, 4, 5])
print(nums.shape)
print(numpy_two_dimensional_list.shape)
three_by_four_array = array([[0, 1, 2, 3],
    [4,5,6,7],
    [8,9,10, 11]])
print(three_by_four_array.shape)

# Data type of numpy array
int_lists = [-3, -2, -1, 0, 1, 2,3]
int_array = array(int_lists)
float_array = array(int_lists, dtype=float)
print(int_array.dtype)
print(float_array.dtype)

# Size of a numpy array
numpy_array_from_list = array([1, 2, 3, 4, 5])
two_dimensional_list = array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print(numpy_array_from_list.size)
print(two_dimensional_list.size)

# Mathematical Operation using numpy
# Addition
print(numpy_array_from_list  + 10)
# Subtraction
print(numpy_array_from_list  - 10)
# Multiplication
print(numpy_array_from_list  * 10)
# Division
print(numpy_array_from_list  / 10)
# Modulus
print(numpy_array_from_list  % 3)
# Floor Division
print(numpy_array_from_list  // 10)
# Exponential
print(numpy_array_from_list  ** 2)

# Checking data types
numpy_int_arr = array([1,2,3,4])
numpy_float_arr = array([1.1,2.0,3.2])
numpy_bool_arr = array([-3,-2,0,1,2,3], dtype='bool')

print(numpy_int_arr.dtype)
print(numpy_float_arr.dtype)
print(numpy_bool_arr.dtype)

# Converting types
# Int to Float
numpy_float_arr = array([1,2,3,4], dtype = 'float')
print(numpy_float_arr)

# Float to Int
numpy_int_arr = array([1., 2., 3., 4.], dtype = 'int')
print(numpy_int_arr)

# Int ot boolean
numpy_bool_arr = array([-3, -2, 0, 1,2,3], dtype='bool')
print(numpy_bool_arr)

# Multi-dimensional Arrays
# 2 Dimension Array
two_dimension_array = array([(1,2,3),(4,5,6), (7,8,9)])
print(type(two_dimension_array))
print(two_dimension_array)
print(two_dimension_array.shape)
print(two_dimension_array.size)
print(two_dimension_array.dtype)

# Getting items from a numpy array
two_dimension_array = array([[1,2,3],[4,5,6], [7,8,9]])
print('First row:', two_dimension_array[0])
print('Second row:', two_dimension_array[1])
print('Third row: ', two_dimension_array[2])

print('First column:', two_dimension_array[:,0])
print('Second column:', two_dimension_array[:,1])
print('Third column: ', two_dimension_array[:,2])

# Slicing Numpy array
first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
print(first_two_rows_and_columns)

# How to reverse the rows and the whole array?
print(two_dimension_array[::])

# Reverse the row and column positions
two_dimension_array[::-1,::-1]

# How to represent missing values?
print(two_dimension_array)
two_dimension_array[1,1] = 55
two_dimension_array[1,2] =44
print(two_dimension_array)

# Numpy Zeroes
numpy_zeroes = zeros((3,3),dtype=int,order='C')
print(numpy_zeroes)

# Numpy Ones
numpy_ones = ones((3,3),dtype=int,order='C')
print(numpy_ones)

twos = numpy_ones * 2
print(twos)

# Reshape
first_shape  = array([(1,2,3), (4,5,6)])
reshaped = first_shape.reshape(3,2)
print(reshaped)

flattened = reshaped.flatten()
print(flattened)

# Horitzontal Stack
np_list_one = array([1,2,3])
np_list_two = array([4,5,6])
print(hstack((np_list_one, np_list_two)))

# Generating Random Numbers
random_float = random.random()
print(random_float)

# Generate a random float  number

random_floats = np.random.random(5)
print(random_floats)

# Generating a random integers between 0 and 10
random_int = np.random.randint(0, 11)
print(random_int)

# Generating a random integers between 2 and 11, and creating a one row array
random_int = np.random.randint(2,10, size=4)
print(random_int)

# Generating a random integers between 0 and 10
random_int = np.random.randint(2,10, size=(3,3))
print(random_int)

# np.random.normal(mu, sigma, size)
normal_array = np.random.normal(100, 15, 100)
print(normal_array)

# Matrix in numpy
four_by_four_matrix = matrix(ones((4,4), dtype=float))
print(four_by_four_matrix)
asarray(four_by_four_matrix)[2] = 2
print(four_by_four_matrix)

# Numpy numpy.arange()
# creating list using range(starting, stop, step)
lst = range(0, 11, 2)
print(lst)

# Similar to range arange numpy.arange(start, stop, step)
whole_numbers = arange(0, 20, 1)
print(whole_numbers)

natural_numbers = arange(1, 20, 1)
print(natural_numbers)

odd_numbers =arange(1, 20, 2)
print(odd_numbers)

even_numbers = arange(2, 20, 2)
print(even_numbers)

# Creating sequence of numbers using linspace

# numpy.linspace()
# numpy.logspace() in Python with Example
# For instance, it can be used to create 10 values from 1 to 5 evenly spaced.
print(linspace(1.0, 5.0, num=10))

# not to include the last value in the interval
print(linspace(1.0, 5.0, num=5, endpoint=False))

# LogSpace
# LogSpace returns even spaced numbers on a log scale. Logspace has the same parameters as np.linspace.

# Syntax:
# numpy.logspace(start, stop, num, endpoint)
print(logspace(2, 4.0, num=4))

# to check the size of an array
x = array([1,2,3], dtype=complex128)
print(x)
print(x.itemsize)

# indexing and Slicing NumPy Arrays in Python
np_list = array([(1,2,3), (4,5,6)])
print(np_list)

print(np_list[0])
print(np_list[1])
print(np_list[:,0])
print(np_list[:,1])
print(np_list[:,2])

# NumPy Statistical Functions with Example
# Numpy Functions
# Min np.min()
# Max np.max()
# Mean np.mean()
# Median np.median()
# Varience
# Percentile
# Standard deviation np.std()

np_normal_dis = np.random.normal(5, 0.5, 100)
print(np_normal_dis)
print('min: ', two_dimension_array.min())
print('max: ', two_dimension_array.max())
print('mean: ',two_dimension_array.mean())
print('sd: ', two_dimension_array.std())


print(two_dimension_array)
print('Column with minimum: ', amin(two_dimension_array,axis=0))
print('Column with maximum: ', amax(two_dimension_array,axis=0))
print('=== Row ==')
print('Row with minimum: ', amin(two_dimension_array,axis=1))
print('Row with maximum: ', amax(two_dimension_array,axis=1))

# How to create repeating sequences?
a = [1,2,3]
# Repeat whole of 'a' two times
print('Tile:   ', tile(a, 2))
# Repeat each element of 'a' two times
print('Repeat: ', repeat(a, 2))

# How to generate random numbers?
# One random number between [0,1)
one_random_num = np.random.random()
one_random_in = np.random
print(one_random_num)
# Random numbers between [0,1) of shape 2,3
r = np.random.random(size=[2,3])
print(r)
print(np.random.choice(['a', 'e', 'i', 'o', 'u'], size=10))
## Random numbers between [0, 1] of shape 2, 2
rand = np.random.rand(2,2)
print(rand)
rand2 = np.random.randn(2,2)
print(rand2)
# Random integers between [0, 10) of shape 2,5
rand_int = np.random.randint(0, 10, size=[5,3])
print(rand_int)

np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

sns.set()
hist(np_normal_dis, color="grey", bins=21)
show()

# numpy.dot(): Dot Product in Python using Numpy
# Dot Product
# Numpy is powerful library for matrices computation. For instance, you can compute the dot product with np.dot
# Syntax
# numpy.dot(x, y, out=None)

# Linear algebra
# Dot product: product of two arrays
f = np.array([1,2,3])
g = np.array([4,5,3])
# 1*4+2*5 + 3*6
print(dot(f, g))

# Matmul: matruc product of two arrays
h = [[1,2],[3,4]]
i = [[5,6],[7,8]]
# 1*5+2*7 = 19
print(matmul(h, i))

# Determinant 2*2 matrix
print(linalg.det(i))

Z = zeros((8,8))
Z[1::2,::2] = 1
Z[::2,1::2] = 1
print(Z)

new_list = [ x + 2 for x in range(0, 11)]
print(new_list)

np_arr = array(range(0, 11))
print(np_arr + 2)

temp = array([1,2,3,4,5])
pressure = temp * 2 + 5
print(pressure)

plot(temp,pressure)
xlabel('Temperature in oC')
ylabel('Pressure in atm')
title('Temperature vs Pressure')
xticks(np.arange(0, 6, step=0.5))
show()

# To draw the Gaussian normal distribution using numpy. As you can see below, the numpy can generate random numbers. To create random sample, we need the mean(mu), sigma(standard deviation), mumber of data points.
mu = 28
sigma = 15
samples = 100000

x = np.random.normal(mu, sigma, samples)
ax = sns.distplot(x);
ax.set(xlabel="x", ylabel='y')
show()