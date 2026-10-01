# 4.Boolean Masking (filtering by Condition)

# Explanation: Boolean masking lets you filter data using a condition (like arr > 5). NumPy creates a True/False "mask" behind the scenes and returns only the elements where the condition is True.

import numpy as np

arr = np.array([5,12,3,18,25,7])

mask = arr > 10
print("Boolean Mask: ", mask)

filtered_values = arr[arr > 10]

print("Values greater than 10:", filtered_values)