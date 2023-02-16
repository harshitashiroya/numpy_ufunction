"""
What is a Set
A set in mathematics is a collection of unique elements.

Sets are used for operations involving frequent intersection, union and difference operations.

Create Sets in NumPy
We can use NumPy's unique() method to find unique elements
from any array. E.g. create a set array, but remember that the set arrays should only be 1-D arrays.
"""
 
import numpy as np

arr = np.array([1, 1, 1, 2, 3, 4, 5, 5, 6, 7])
x = np.unique(arr)
print(x)


"""
Finding Union
To find the unique values of two arrays, use the union1d() method.
"""


arr1 = np.array([1, 2, 3, 4])
arr2 = np.array([3, 4, 5, 6])

newarr = np.union1d(arr1, arr2)

print(newarr)


"""
Finding Intersection
To find only the values that 
are present in both arrays, use the intersect1d() method.
"""

newarr2 = np.intersect1d(arr1, arr2, assume_unique=True)

print(newarr2)

"""
Find the difference of the set1 from set2:
"""


newarr3 = np.setdiff1d(arr1, arr2, assume_unique=True)
print(newarr3)

"""
Finding Symmetric Difference
To find only the values that are 
NOT present in BOTH sets, use the setxor1d() method.
"""

newarr3 = np.setxor1d(arr1, arr2, assume_unique=True)

print(newarr3)