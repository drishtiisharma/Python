import numpy as np

## 0 dimension array
# arr0 = np.array(10)
# print(arr0,'dimension: ',arr0.ndim)

## 1 dimension array
# arr1 = np.array(['a','b','c'])
# print(arr1,'dimension: ',arr1.ndim)

## 2 dimension array
# arr2 = np.array([
#     [10,20,30],
#     ['hello','world','drishti']
# ])
# print(arr2,'dimension: ',arr2.ndim)

## 3 dimension array.
# arr3 = np.array([
#     [
#         [1,2,3],
#         [4,5,6]
#     ],
#     [
#         [7,8,9],
#         [10,11,12]
#     ]
# ])
# print(arr3,'dimension: ',arr3.ndim)

## higher dimensions
arr4 = np.array([1,2,3,4,5],ndmin=4)
print(arr4,'dimension:',arr4.ndim)