# add()

import numpy as np

ar1 = np.array([10, 20, 12, 30, 45])
ar2 = np.array([5,7,2,10,9])

print("array 1:-",ar1)
print("array 2:-",ar2)

add_arr = np.add(ar1,ar2)
print("addition :-",add_arr)

sub_arr = np.subtract(ar1,ar2)
print("subtaction is :-",sub_arr)

mul_arr = np.multiply(ar1,ar2)
print("Multiplication is:-",mul_arr)

div_arr = np.divide(ar1, ar2)
print("division is:- ",div_arr)


"""
The power() function rises the values from the first array to the power of the values of the second array, 
and return the results in a new array.
"""

pow_arr = np.power(ar1,ar2)
print("power is:- ",pow_arr)

"""
Remainder
Both the mod() and the remainder() functions return the remainder 
of the values in the first array corresponding to the values in the second array, 
and return the results in a new array.
"""

mod_arr = np.mod(ar1,ar2)
print("remainder or mod of the array is:- ",mod_arr)

rem_arr = np.remainder(ar1, ar2)
print("mod of the array is:- ",rem_arr)


"""
Quotient and Mod
The divmod() function return both the quotient and the the mod. 
The return value is two arrays, the first array contains 
the quotient and second array contains the mod.
"""

qut_arr = np.divmod(ar1,ar2)
print("quotient and mod of array is:-",qut_arr)

"""
The first array represents the quotients, 
(the integer value when you divide 10 with 5,...

2nd array represents remainder...
"""



new_arr = np.array([1,-2,-90,5,7,-78])
print("new array is:-",new_arr)

ab_arr = np.absolute(new_arr)
print("absolute array is:-", ab_arr)