'''
iterators
---------

an object that contains countable number of values

consists of methods __iter__() and __next__()


'''

tuple = 10,20,420,521,56
it=iter(tuple)
for x in range(2):
    print(next(it))