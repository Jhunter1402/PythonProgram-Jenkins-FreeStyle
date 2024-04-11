import numpy as np

arr1 = np.array([[[1, 2, 3, 4], [5, 6, 7, 8]], [['a', 'b', 'c', 'd'], ['e', 'f', 'g', 'h']]])
print(arr1)
print(arr1.ndim)
print(arr1[0,1,3])
print(arr1[:, :, 2:])
print(arr1[1, 1:2, 1:3])
print(arr1[0, :, 3])
