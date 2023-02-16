#LOGS

"""
NumPy provides functions to perform log at the base 2, e and 10.
We will also explore how we can take log for any base by creating a custom ufunc.
All of the log functions will place -inf or inf in the elements if the log can not be computed.
"""

"""
The arange(1, 10) function returns an array with integers 
starting from 1 (included) to 10 (not included).
"""


import numpy as np

# log2()

ar = np.arange(10,20)
print("array in range 10 to 20:- ",ar)
print("\n")
print("log2() :- ",np.log2(ar))
print("\n")
print("log10() :- ",np.log10(ar))
print("\n")
print("log_e() or log():- ",np.log(ar))


"""
Log at Any Base
NumPy does not provide any function to take log at any base, 
so we can use the frompyfunc() function  along with 
inbuilt function math.log() with two input parameters 
and one output parameter:
"""

from math import log
print("\n")
np_log = np.frompyfunc(log,2,1) # 2 i/p, 1 o/p
print("log using math func:- ",np_log(100,15))