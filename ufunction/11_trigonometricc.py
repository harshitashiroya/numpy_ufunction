"""
Trigonometric Functions
NumPy provides the ufuncs sin(), cos() and tan() that take values in
radians and produce the corresponding sin, cos and tan values.
"""

import numpy as np

x = np.sin(np.pi/2)

print(x)

arr = np.array([np.pi/2, np.pi/3, np.pi/4, np.pi/5])
y = np.sin(arr)
print(y)

"""
Convert Degrees Into Radians
By default all of the trigonometric functions 
take radians as parameters but we can convert radians to degrees and vice versa as well in NumPy.

Note: radians values are pi/180 * degree_values.
"""

arr2 = np.array([90,180,270,360])
x1 = np.deg2rad(arr2)
print(x1)

#Radians to Degrees

arr3 = np.array([np.pi/2, np.pi, 1.5*np.pi, 2*np.pi])
x2 = np.rad2deg(arr)
print(x2)

"""
Finding Angles
Finding angles from values of sine, cos, tan. 
E.g. sin, cos and tan inverse (arcsin, arccos, arctan).

NumPy provides ufuncs arcsin(), arccos() and arctan() 
that produce radian values for corresponding sin, cos and tan values given.
"""

x3 = np.arcsin(1.0)
print(x3)

#Angles of Each Value in Arrays

arr4 = np.array([1, -1, 0.1])
x4 = np.arcsin(arr4)
print(x4)

"""
NumPy provides the hypot() function that takes the base and perpendicular values 
and produces hypotenues based on pythagoras theorem.
"""


base = 3
perp = 4
x5 = np.hypot(base, perp)

print(x5)