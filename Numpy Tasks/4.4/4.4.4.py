# Create a 6×6 identity-like matrix using np.eye, then set all values in rows 2–4 and columns 2–4 to 5.

import numpy as np

arr = np.eye(6, dtype=int)
print(arr)

arr[2:5, 2:5] = 5
print("\nNew array : ")
print(arr)