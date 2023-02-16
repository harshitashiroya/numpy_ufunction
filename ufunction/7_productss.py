"""
use the prod() function.

"""

import numpy as np

ar = np.array([1,2,3,4,5])
print("array1 is:-",ar)

x = np.prod(ar)
print("product of array is 1*2*3*4*5 :-",x)

ar2 = np.array(([6,7,8,9,20]))
print("array2 is:-",ar2)
pro_ar2 = np.prod(ar2)
print("product of array2 is  :-",pro_ar2)


y = np.prod([ar,ar2])  # 1*2*3*4*5*6*7*8*9*20
print("product of 2 array is:-",y)

#product over axis

ax_ar = np.prod([ar,ar2],axis=1)
print("axis-1",ax_ar)

"""
Cummulative Product
Cummulative product means taking the product partially.

E.g. The partial product of [1, 2, 3, 4] 
is [1, 1*2, 1*2*3, 1*2*3*4] = [1, 2, 6, 24]

Perfom partial sum with the cumprod() function.
"""

cum_arr = np.cumprod(ar)
print("Cummulative Product:-",cum_arr)