import numpy as np

##Compute the sum of the diagonal element of a given array
m = np.arange(9).reshape(3,3)
print("Original matrix:")
print(m)
result =  np.trace(m)
print("Condition number of the said matrix:")
print(result)