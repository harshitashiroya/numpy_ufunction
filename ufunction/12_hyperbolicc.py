"""
Hyperbolic Functions
NumPy provides the ufuncs sinh(), cosh() and tanh() that take values in radians
and produce the corresponding sinh, cosh and tanh values..
"""

#Find sinh value of PI/2:

import numpy as np

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
x = np.cosh(arr)
print("cosh :-",x)

y = np.sinh(arr)
print("sinh :-",y)


z = np.arcsinh(1.0)
print("angle is :- ",z)


arr = np.array([0.1, 0.2, 0.5])
i = np.arctanh(arr)
print("each tanh value angle:-",i)