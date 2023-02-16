"""
Finding GCD (Greatest Common Denominator)
The GCD (Greatest Common Denominator), also known as HCF (Highest Common Factor)
s the biggest number that is a common
factor of both of the numbers.
"""

import numpy as np

num1 = 9
num2 = 6

x = np.gcd(num1,num2)
print(x)


y = np.gcd.reduce(([7,8,9]))
print(y)