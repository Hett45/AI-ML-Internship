# Create a 6×4 array, split it into 3 equal pieces along the row axis, and print each piece.

import numpy as np

arr = np.arange(1, 25).reshape(6, 4)
print(arr)

pieces = np.split(arr, 3, axis=0)
for i, piece in enumerate(pieces):
    print(f"\nPiece {i + 1}:")
    print(piece)
    print("Shape:", piece.shape)