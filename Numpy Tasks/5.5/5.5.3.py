# Given a 4×5 matrix of random integers 1–50, find: overall sum, row-wise max, column wise mean, and the index of the global minimum. 

import numpy as np

arr = np.random.randint(1, 51, size=(4, 5))
print(arr)

total_sum = np.sum(arr)
print("/nTotal sum : ", total_sum)

row_max = np.max(arr, axis=1)
print("Row wise max : ", row_max)

col_mean = np.mean(arr, axis=0)
print("Column wise min : ", col_mean)

min_index = np.unravel_index(np.argmin(arr), arr.shape)
print("Global minimum index : ", min_index)
print("Global minimum value : ", arr[min_index])