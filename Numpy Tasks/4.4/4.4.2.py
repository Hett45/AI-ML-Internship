# reverse every row of a 4*4 random integer matri using slicing

import numpy as np

arr = np.random.randint(10, 100, size = (4, 4))
print(arr)

reversed_arr = arr[:, ::-1]
print("\nReversed array : ")
print(reversed_arr)