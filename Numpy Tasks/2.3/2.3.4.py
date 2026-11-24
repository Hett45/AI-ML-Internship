# create a 3*3 random integer array with value between 10 and 99. find it's minimum and maximum values.

import numpy as np

arr = np.random.randint(10, 100, size = (3, 3))
print(arr)

minimum_value = np.min(arr)
print("Minimum value : ", minimum_value)

maximum_value = np.max(arr)
print("Maximum value : ", maximum_value)