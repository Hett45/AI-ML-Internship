# create a 4*4 matrix of zeros and then set the diagonal elements to 1

import numpy as np

arr = np.zeros((4, 4), dtype=int)

for i in range(4):
    arr[i, i] = 1
     
print(arr)