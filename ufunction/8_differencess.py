"""
Differences
A discrete difference means subtracting two successive elements.
E.g. for [1, 2, 3, 4], the discrete difference would be [2-1, 3-2, 4-3] = [1, 1, 1]
To find the discrete difference, use the diff() function.
"""


import numpy as np

ar = np.array([1,2,3,4,5])
print("array1 is:-",ar)

diff_arr = np.diff(ar)
print(diff_arr)

#Compute discrete difference of the following array twice:

new_diff = np.diff(ar,2)
print(new_diff)
