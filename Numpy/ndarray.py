import numpy as np

# arr = np.array("A") #this output is 0 , because this is zero dimension array

# arr = np.array(["A", "B", "C"]) #this output is 1, because this is one dimensional array

# arr = np.array([["A","B","C"], ["D","E","F"]]) this is two dimensional array , because this output is 2

arr = np.array([[['A']]])
print(arr.ndim)

