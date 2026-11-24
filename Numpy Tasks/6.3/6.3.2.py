# Stack two 3×4 arrays vertically and horizontally. Print the shape of each result. 

import numpy as np

A = np.arange(1, 13).reshape(3, 4)
B = np.arange(13, 25).reshape(3, 4)
print(A)
print(B)

vertical = np.vstack((A, B))
print(vertical)

horizontal = np.hstack((A, B))
print(horizontal)
