import numpy as np 
# # creating a copy
# arr = np.array([10,20,30,'hello','how','are','you',12.3,15.68,True,False])

# x = arr.copy()
# x[0] = 11
# print(x)
# print(arr)


# # creating a view
# a = np.array([10,20,30])
# # changes in view affect the og array
# print("before change in view,OG:",a)
# b = a.view()
# b[0] = 11
# print("after change in view,OG:",a)

# #changes in the og array affects the view
# print("before changes in og array,VIEW:",b)
# a[2] = 24
# print("after changes in og array,VIEW:",b)


## checking if array owns its data

z = np.array([10,210,30])
m = z.copy()
n = z.view()
print(m.base)
print(n.base)
