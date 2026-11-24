# Normalise an array of 10 random values (make mean=0, std=1). Verify with .mean() and .std().

import numpy as np

arr = np.random.rand(10)
print(arr)

mean = arr.mean()
std = arr.std()

normalized_arr = (arr - mean) / std
print("normalized array : ")
print(normalized_arr)