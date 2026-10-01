# 3. Fancy Indexing(Picking Arbitray Positions)

# Explanation: Fancy indexing allows you to pass a list of indices instead of a single number or a continuous slice. This lets you pull out rows or columns in any custom order you want.

# Example code: 

import numpy as np

matrix = np.array([
    [10,20,30],
    [40,50,60],
    [70,80,90],
])

print("Recordered rows: \n", matrix[[2,1,0]])
