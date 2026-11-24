# write a funciton describe(arr) that prints all six attribute of given array.

import numpy as np

arr = np.array([[10, 20, 30],
                [40, 50, 60]], dtype=np.int32)
print(arr) 

def descibe(arr):
    print("Number of dimensions : ", arr.ndim)
    print("Shape : ", arr.shape)
    print("Total elements : ", arr.size)
    print("Data type : ", arr.dtype)
    print("item size : ", arr.itemsize)
    print("Total memory : ", arr.nbytes)
    
descibe(arr)