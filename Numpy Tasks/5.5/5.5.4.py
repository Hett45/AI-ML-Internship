# Use broadcasting to create the multiplication table for numbers 1–9 as a 9×9 matrix. No loops allowed.

import numpy as np

a = np.arange(1, 10)
b = np.arange(1, 10)

table = a[:, np.newaxis] * b
print(table)