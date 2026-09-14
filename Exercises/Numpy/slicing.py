import numpy as np

# slicing 1d arrays
arr1 = np.array([100,200,300,400])
print(arr1[3])
print(arr1[-2])
print(arr1[1:3])
print(arr1[-3:-1])
print(arr1[1::2])

## slicing 2d arrays
# arr2 = np.array([
#     [100,200,300,400],
#     [500,600,700,800]
# ])
# print(arr2[1,2])
# print(arr2[-2,-1])
# print(arr2[0:2,1:3])

## slicing 3d arrays
# arr3 = np.array([
#     [
#         [10,20,30],
#         [40,50,60]
#     ],
#     [
#         [70,80,90],
#         [100,110,120]
#     ]
# ])
# print(arr3[1,0,1])
# print(arr3[-2,-2,-2])
# print(arr3[0:2,0:2,1:])