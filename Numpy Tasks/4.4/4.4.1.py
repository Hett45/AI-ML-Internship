# given arr = np.arange(1, 26).reshape(5, 5), extract the 3*3 sub-matrix from the center.

import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
print(arr)

sub_matrix = arr[1:4, 1:4]
print(sub_matrix)