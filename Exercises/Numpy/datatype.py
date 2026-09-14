# import numpy as np 

# arr1 = np.array([1,2,3,4],dtype=np.uint64) # uint64
# arr2 = np.array(['hello','world']) # <U5
# arr3 = np.array([True,False]) # bool
# arr4 = np.array([13.4,2.5,3.8,4.357]) # float64
# arr5 = np.array([-1,-2,-3,-4]) # int64
# print(arr1.dtype)
# print(arr2.dtype)
# print(arr3.dtype)
# print(arr4.dtype)
# print(arr5.dtype)


## creating arrays with defined data type
# import numpy as np 
# arr = np.array([10,20,32,'s'],dtype='bool')
# print(arr)
# print(arr.dtype)

## converting to different types
# import numpy as np 
# arr = np.array(['A','B','C'],dtype='i')
# print(arr)
# print(arr.dtype)

# import numpy as np 
# arr = np.array([1.1,2.2,3.3])
# newarr=  arr.astype('int')
# print(newarr)
# print(newarr.dtype)

import numpy as np
arr = np.array([1, 0, 3])
newarr = arr.astype(bool)
print(newarr)
print(newarr.dtype)