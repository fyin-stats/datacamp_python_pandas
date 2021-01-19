#### https://medium.com/better-programming/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d
####

# load the library
import numpy as np

# numpy is a fundamental library that most of the widely used Python data processing libraries are built upon
# pandas, OpenCV
# can efficiently share data with TensorFlow, Keras, etc
# possible to run numpy on GPU

# central concept of numpy -- n-dimensional array
# vectors - 1D arrays
# matrices - 2D arrays
# 3D and above

# ################################################
# numpy array vs python list
# ################################################
# they both serve as containers with fast item getting and setting and somewhat slower inserts and removals
# of elements

# hands-down simplest example, when numpy arrays beat lists is arithmetic
# other than that, NumPy arrays are
# more compact
# faster than lists when the operation can be vectorized
# slower than lists when you append elements to the end
# usually homogeneous: can only work fast with elements of one type

# examples
a = [1,2,3]
[q*2 for q in a]

#
a = np.array([1,2,3])
a * 2

#
a = [1,2,3]
b = [4,5,6]
[q+r for q, r in zip(a,b)]

#
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b

# numpy: append() at O(N)
# list: append() at O(1)

# Vectors, the 1D arrays
# vector initialization
a = np.array([1., 2., 3.])

#
b = np.zeros(3, int)

#
c = np.zeros_like(a)

# np.zeros_like, _like counterpart


# monotonic sequence in numpy
# np.arange(start, stop, step)
# np.linspace(start, stop, num)


# random arrays
#
np.random.randint(0, 10, 3) # np.random.randint (open at the right-hand end)
# vs random.randint (closed at the right-hand end)

#
np.random.rand(3) # uniform, x \in [0,1)

#
np.random.uniform(1, 10, 3)

# np.random.randn(3) # standard normal, mu = 0, sigma = 1

# np.random.normal(5,2,3) # normal, mu = 5, sigma = 2

# vector indexing
# numpy is brilliant at providing easy ways of giving it back
# view vs copy

# python list
# a = [1, 2, 3]
# b = a # no copy
# c = a[:] # copy
# d = a.copy() # copy

# numpy array
# a = np.array([1,2,3])
# b = a # no copy
# c = a[:] # no copy
# d = a.copy() # copy

# all of those methods including fancy index are mutable, they allow modification of the original array
# contents through assignment, as shown above. they don't store the data and reflect the changes
# in the original array if it happens to get changed after being index

#
a = [1, 2, 3]

#
a[1:2] = [5,6] # won't work in numpy, use np.insert, np.append, etc. instead

# getting data from numpy arrays is boolean indexing, which allows using all kinds of logical operatoins

# boolean indexing is also writable
# np.where
# np.clip

# vector operations
# vectors operations are shifted to the C++ level and allow us to avoid the costs of slow Python
# loops, numpy allows the manipulation of whole arrays just like ordinary numbers
#
np.array([3,4])**2

# most of the math functions have numpy counterparts that can handle vectors
# np.sqrt
# np.exp
# np.log

# dot product
# np.dot

# cross product
# np.cross

# trignometry
# np.sin
# np.arcsin

np.sin([np.pi, np.pi/2])

# np.hypot

# arrays can be rounded as a whole
np.floor([1.1, 1.5, 1.9, 2.5])

# np.ceil
# np.round
# np.max
# np.argmax


# a.sort()
# sorted(a)
# a.sort(key=f)
# a.sort(reversed=False) # ascending / descending

# numpy arrays
# a.sort()
# np.sort(a) # returns new sorted array

#######################
# Searching for an element in a vector
# numpy does not have an index method
#

########################
# comparing floats
# np.allclose(a,b)
# compares arrays of floats with a given tolerance
# vs 0.1 + 0.2 == 0.3
# vs math.isclose(0.1+0.2, 0.3)

# matrices, the 2D arrays
# there used to be a dedicated matrix class in Numpy
# but it is deprecated now
# matrix, and 2D array interchangeably
#

a = np.array([[1,2,3],[4,5,6]])

#
a.dtype
a.shape

# random matrix generation
# vs random.randint
np.random.randint

#
np.random.rand

#
np.random.uniform(1, 10, [3,2]) # uniform in [1, 10) on a 3 by 2 matrix

# the axis argument
# a.sum()
# a.sum(axis=0)
# a.sum(axis=1)
# axis = 0, sum over the first index
# axis = 1, sum over the second index

#
# Matrix arithmetic
# outer product, * (regardless of which matrix appears at first)
# inner product, @, matrix product

# transpose

# newaxis

#
a = np.arange(1, 7, 1)

#
a.reshape(-1, 1) # -1 argument tells reshape to calculate one of the dimension sizes automatically
a.reshape(1, -1)
a.reshape(2,3) # also = a.reshape(2,-1)

# np.squeeze
# a[:, np.newaxis]
# a[:, None]

# matrix manipulations
# np.hstack()
# np.vstack()

# np.hstack
# np.hsplit
# np.vstack
# np.vsplit(x, [3])

# np.tile(a, (2,3))
# b = a.repeat(3, axis=1)

# np.delete to delete specific rows / columns
# np.insert for the inverse operations insert
# np.insert(h, [1,2], 0, axis = 1)
# np.append, O(N) works slowly for large arrays
# np.pad

# meshgrids
# Aij = j - i
# python way
# c = [[j-i) for j in range(3)] for i in range(2)]
# a = np.array(c)

# the numpy way
# I, J = np.meshgrid(i, j, sparse = True, indexing = 'ij')
# J-I

# the meshes can be useful for indexing arrays
# I, J = np.indices(a.shape)
#

# Matrix statistics
# np.unravel_index(a.argmin(), a.shape)

# np.any((), axis = 1)
# np.any((), axis = 0)

# matrix sorting
# a.sort(axis = 0)
# a.sort(axis = 1)

# a[a[:,0].argsort()] sorts the array by the first column
# kind = 'stable'

# pd.DataFrame(a).sort_values().to_numpy()
#



################################################
# 3D and above
################################################
# np.arange(1, 9).reshape(2,2,2)

# 3D array, i goes deeper, j goes down (vertical), k goes wide (horizontal)
# RGB colors creation
# np.vstack
# np.hstack
# np.dstack


##################################################
# numpy exercices
##################################################
# https://github.com/rougier/numpy-100/blob/master/100_Numpy_exercises.ipynb