#The Lowest Common Multiple is the smallest number that is a common multiple of two numbers.

import numpy as np

num1 = 9
num2 = 6

x = np.lcm(num1,num2)
print(x)

"""
The reduce() method will use the ufunc, in this case the lcm() function, on each element, 
and reduce the array by one dimension.
"""

y = np.lcm.reduce(([7,8,9]))
print(y)