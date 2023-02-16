#SUMMATIONS

"""
Addition is done between two arguments
whereas summation happens over n elements.
"""


import numpy as np

ar1 = np.array([1,4,7])
print("array 1 is:- ",ar1)

ar2 = np.array([6,0,12])
print("array 2 is:- ",ar2)

add_arr = np.add(ar1, ar2)
print("addition of arrays is:- ",add_arr)

sum_arr = np.sum([ar1, ar2])
print("sum of arrays is :- ",sum_arr)

# summation using axis

sum_arr_ax1 = np.sum([ar1, ar2], axis=1)
print("sum of arrays on axis 1  is :- ",sum_arr)

sum_arr_ax0 = np.sum([ar1, ar2], axis=0)
print("sum of arrays on axis 0  is :- ",sum_arr)

"""
Cummulative Sum
Cummulative sum means partially adding the elements in array.

E.g. The partial sum of [1, 2, 3, 4] would be 
[1, 1+2, 1+2+3, 1+2+3+4] = [1, 3, 6, 10].

Perfom partial sum with the cumsum() function.
"""

cum_sum_ar1 = np.cumsum(ar1)
print("cum sum of ar1 is:- ",cum_sum_ar1)

cum_sum_ar2 = np.cumsum(ar2)
print("cum sum of ar2 is:- ",cum_sum_ar2)