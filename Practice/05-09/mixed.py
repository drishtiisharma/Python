## list comprehension
# list = [8,5,6,3,1,4,7,2,3,4]
# sq_list = [x**2 for x in list if x%2==0]
# print(set(sq_list))

## unpacking
t = (1, 2, 3, 4, 5)
first, *middle, last = t
# # first, middle, last = t[0], t[1:-1], t[-1]
# first = t[0]; last = t[-1]; middle = t[1:4]
print(first,last,middle)