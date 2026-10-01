# 2. Slicing (Extracting a Range or Sub-section)
# Explanation: Slicing lets you extract a portion (range) of an array using the syntax [start:stop]. The stop index is exclusive (it goes up to, but doesn't include, that number). For 2D arrays, you slice rows and columns separated by a comma: [row_start:row_end, col_start:col_end].

import numpy as np

arr = np.array([10,20,30,40,50])

print("Slice [1:4]: ", arr[1:4])

mat = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
    ])

print("Top-left 2x2:\n", mat[:2,:2])

