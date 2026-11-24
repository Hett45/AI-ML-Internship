# Apply np.sin and np.cos to 100 evenly spaced angles from 0 to 2π. Verify that sin²(x) + cos²(x) ≈ 1 for all values. 

import numpy as np

angles = np.linspace(0, 2*np.pi, 100)

sin_values = np.sin(angles)
cos_values = np.cos(angles)

result = sin_values**2 + cos_values**2

print("Sine values:", sin_values)
print("Cosine values:", cos_values)
print("Verification:", result)

print("All values approximately equal to 1:",
      np.allclose(result, 1))