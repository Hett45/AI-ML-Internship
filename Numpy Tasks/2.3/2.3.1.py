# create a 1d array of integers from 5 to 50 in steps of 5. print it's shape and dtype.

import numpy as np

arr = np.arange(5, 51, 5)

print("Array : ", arr)
print("Shape : ", arr.shape)
print("Datatype : ", arr.dtype)