"""
How To Create Your Own ufunc
To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

The frompyfunc() method takes the following arguments:

function - the name of the function.
inputs - the number of input arguments (arrays).
outputs - the number of output arrays.
"""

import numpy as np

def add(x,y):
    return  x + y


add = np.frompyfunc(add,2,1)
"""
np.frompyfunc(add,2,1) 

add = name of function
2 = no.of i/p arrays
1 = no.of o/p arrays
"""

print(add([1,2,3],[6,7,8]))

print(type(np.add))  # check the function type- ufunc



if type(np.add) == np.ufunc:
  print('add is ufunc')
else:
  print('add is not ufunc')