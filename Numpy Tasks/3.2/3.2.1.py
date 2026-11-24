# create a (4, 3, 2) array of ones. print it's ndim, shape, size and total memory in bytes.

import numpy as np

arr = np.ones((4, 3, 2))
print(arr)

print("Number of dimensions : ", arr.ndim)
print("Shape : ", arr.shape)
print("Total Elements : ", arr.size)
print("Total Memory in bytes: ", arr.nbytes)