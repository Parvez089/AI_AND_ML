# 1. Indexing (Accessing a Single Item)
# Explanation: Indexing allows you to grab a specific, single element using its position index. Python always starts counting from 0. For 2D arrays (matrices), you specify [row_index, column_index].

import numpy as np



martix = np.array([
    [10,20,30],
    [40,50,60]
    ])

print("Row 0,Col 0: ", martix[0,0])
print("Row 0,Col 2: ", martix[0,1])
print("Row 0,Col 2: ", martix[0,2])
print("Row 1,Col 0: ", martix[1,0])
print("Row 1,Col 1: ", martix[1,1])
print("Row 1,Col 2: ", martix[1,2])

print(martix)