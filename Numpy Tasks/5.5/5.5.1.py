# Create two 3×3 random arrays A and B. Compute element-wise product, division, and A raised to power B.

import numpy as np

a = np.random.randint(1, 10, size=(3, 3))
b = np.random.randint(1, 10, size=(3, 3))
print(a)
print(b)

product = a * b
print("\nElement wise product : ")
print(product)

division = a / b
print("\nDivision : ")
print(division)

power = a ** b
print("\nPower : ")
print(power)