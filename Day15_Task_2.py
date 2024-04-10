import numpy as np

arr1 = np.random.rand(3, 3)
print(arr1)
print(arr1.ndim)
print(arr1.shape)

arr2 = np.random.rand(1, 2, 3)
print(arr2)
print(arr2.ndim)
print(arr2.shape)

arr3 = np.random.rand(3, 2, 1)
print(arr3)
print(arr3.ndim)
print(arr3.shape)

arr4 = np.random.rand(2, 2, 2, 2)
print(arr4)
print(arr4.ndim)
print(arr4.shape)
