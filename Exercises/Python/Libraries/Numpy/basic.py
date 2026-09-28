# import numpy as np

# arr_list = [10,20,'hello']
# arr_np =np.array([10,20,'hello'])

# print(arr_list,type(arr_list))
# print(arr_np,type(arr_np))
# print(np.__version__)

## tuple -> numpy array

import numpy as np
tup = (10,20,30,40)
ndarr = np.array(tup)
print(type(tup),type(ndarr))
print(tup)
print(ndarr)