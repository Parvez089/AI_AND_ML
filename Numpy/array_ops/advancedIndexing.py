import numpy as np

matrix = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

rows = np.array([0,1,2])
cols = np.array([2,1,0])

print("Diagonal elements: ", matrix[rows,cols])