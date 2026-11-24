# Create a 1D array of 30 elements and reshape it into (5, 6), (2, 3, 5), and (6, 5). Confirm all have 30 elements. 

import numpy as np

arr = np.arange(1, 31)
print("Original array : ", arr)

arr_5nd6 = arr.reshape(5, 6)
print("Reshaped array into 5*6 :")
print(arr_5nd6)

arr_2nd3nd5 = arr.reshape(2, 3, 5)
print("Reshaped array into 2*3*5 :")
print(arr_2nd3nd5)

arr_6nd5 = arr.reshape(6, 5)
print("Reshaped array into 6*5 :")
print(arr_6nd5)

print("Total elements : ", arr.size)