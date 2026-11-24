# Create a column vector from [10, 20, 30, 40] using np.newaxis. Add it to a 4×3 matrix using broadcasting. 

import numpy as np

arr = np.array([10, 20, 30, 40])
print(arr)

column = arr[:, np.newaxis]
print(column)

matrix = np.arange(1, 13).reshape(4, 3)
print(matrix)

result = matrix + column
print(result)

print("Shape : ", result.shape)