import numpy as np

'''da1 = np.zeros((5))
da2 = np.zeros((5,5))
da3 = np.zeros((5,5,5))

arr = np.array([1,2,3,4,5])
print(da3)
print(arr)
print(np.__version__)
print(arr[2])
print(type(arr))

print(arr[0:3:2])
print(arr.dtype)'''

arr = np.array([1.1, 2.1, 3.1])

newarr = arr.astype('i')

print(newarr)
print(newarr.dtype)

