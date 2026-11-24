# create an int64 array and convert it to float32. compare nbytes before and after.

import numpy as np

arr = np.array([10, 20, 30, 40, 50], dtype=np.int64)

new_arr = arr.astype(np.float32)

print("Original array : ", arr)
print("Original Datatype : ", arr.dtype)
print("Original Memory : ", arr.nbytes)

print("Converted array : ", new_arr)
print("Converted array's datatype: ", new_arr.dtype)
print("Converted array's memory : ", new_arr.nbytes)