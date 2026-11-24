# from the array  [34, -5, 12, 0, -8, 99, 47, -1], extract all negative values and replace them with their absolute values in the original values.

import numpy as np

arr = np.array([34, -5, 12, 0, -8, 99, 47, -1])
print("Original array : ", arr)

negative_values = arr[arr < 0]
print("Negative values : ", negative_values)

arr[arr < 0] = np.abs(arr[arr < 0])
print("Updated array : ", arr)