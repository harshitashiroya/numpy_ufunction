"""
There are primarily five ways of rounding off decimals in NumPy:

truncation
fix

Use the trunc() and fix() functions.
Remove the decimals, and return the float number closest to zero.

rounding
The around() function increments preceding digit or decimal by 1 if >=5 else do nothing.
E.g. round off to 1 decimal point, 3.16666 is 3.2

floor
The floor() function rounds off decimal to nearest lower integer.
E.g. floor of 3.166 is 3.

ceil
The ceil() function rounds off decimal to nearest upper integer.
E.g. ceil of 3.166 is 4.

"""

import numpy as np

ar = np.array([-3.67123, 3.25536])
print("array is:- ",ar)

print("using fix:-", np.fix(ar))
print("using truncate:-", np.trunc(ar))

print("using rounding:- ",np.round(3.89375,2)) # 2 = round up to the 2 number

print("using floor:- ",np.floor(ar))
print("using ceil:- ",np.ceil(ar))

















