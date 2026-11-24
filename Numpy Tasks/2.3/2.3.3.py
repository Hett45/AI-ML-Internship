# generate an array of 20 evenly spaced values between 0 and 2pie. compute sin of each value

import numpy as np

arr = np.linspace(0, 2 * np.pi, 20)
print("Array : ", arr)

sin_value = np.sin(arr)
print("Sin Value : ", sin_value)