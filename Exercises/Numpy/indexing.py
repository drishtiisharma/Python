import numpy as np

# accessing 1d arrays
arr1 = np.array([100,200,300,400])
print(arr1[3])
print(arr1[-2])

# ## accessing 2d arrays
arr2 = np.array([
    [100,200,300,400],
    [500,600,700,800]
])
print(arr2[1,2])
print(arr2[-2,-1])

# ## accessing 3d arrays
arr3 = np.array([
    [
        [10,20,30],
        [40,50,60]
    ],
    [
        [70,80,90],
        [100,110,120]
    ]
])
print(arr3[1,0,1])
print(arr3[-2,-2,-2])