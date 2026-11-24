# build a 5*5 cheackerboard pattern using slicing and zeros.

import numpy as np

arr = np.zeros((5, 5), dtype=int)

arr[::2, 1::2] = 1
arr[1::2, ::2] = 1

print(arr)