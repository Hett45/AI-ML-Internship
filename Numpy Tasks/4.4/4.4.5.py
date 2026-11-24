# Use np.where to classify an array of 10 random scores (0–100): 'A' if ≥ 80, 'B' if ≥ 60, else 'C'. 

import numpy as np

scores = np.random.randint(0, 101, size=10)
print("Random Scores : ", scores)

grades = np.where(scores >= 80, 'A',
         np.where(scores >= 60, 'B', 'C'))

print("Grades : ", grades)