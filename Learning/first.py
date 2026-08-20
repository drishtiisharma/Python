# print("hello world!")
# -------------------- #
# if 5>6:
#     print("greater")
# else:
#     print("smaller")
# -------------------- #
# print("sup?"); x= 10; y=20; print("x+y = ",x+y) #valid but unecessary
# -------------------- #
# x="11"
# y="24"
# print(x+y)
# can only concatenate str to str
# -------------------- #
# print('hello world") # cant use mismatching quotes either both single or double quotes
# -------------------- #
# print("hello",end=' ')
# print("world")
# -------------------- #
# print("im",25)
# print("im ",25)
# print("im","ironman")
# print("im"," ironman")
# -------------------- #
# '''
# hello
# how are you
# im good
# '''
# print("helloooo")
# -------------------- #
# x = 10.2
# print(int(x))
# -------------------- #
# x = 10
# y = 10.2
# print(type(x),type(y))
# -------------------- #
# x = 10
# x = 20
# print(x) # will print 20
# -------------------- #
# x,y,z = "orange",102,10.2
# print(x,y,z)
# -------------------- #
# x=y=z="mango"
# print(x,y,z)
# -------------------- #
# list1=['orange',"yellow","pink"]
# tuple1=(10,20,30)
# x,z,y = list1
# a,b,c = tuple1
# print(a,b,c)
# print(x,y,z)
# -------------------- #
# x = "awesome"
# def myfunc():
#     y = " and user friendly"
#     print("python is "+x)
# myfunc()
# print(y) # this wont work
# -------------------- #
# x = "awesome" # global variable
# def r():
#     x = "easy to use" # local variable
#     print("python is "+x) # will pickup local variable
# r()
# -------------------- #
# x = 10
# def f():
#     global x
#     x = 20
#     print(x)
# f() # 20
# print(x) # prints 20 - because of 'global' change
# -------------------- #
# l = [10,20,30]
# l[0]=40
# print(l) # updated as lists are mutable
# t = (10,20,30)
# t[0]=50
# print(t) # will throw error as tuples are immutable
# -------------------- #
# x = range(0,5)
# print(x) # creates a range object, doesnt create/print a list
# print(list(x)) # prints the list
# y = list(range(0,7))
# print(y)
# y[0]=7
# print(y) # updated
# z = tuple(range(0,7))
# print(z)
# z[0]=7
# print(z) # error thrown as tuples are immutable
# -------------------- #
# d = {
#     'name':'drishti sharma',
#     'age':22
# }
# print(d)
# -------------------- #
# l=[1,3,3]
# t=(1,3,3)
# s={1,3,3} # eliminates the duplicate, prints rest
# print(l,t,s)
# -------------------- #
# s={1,2,3}
# s.remove(2)
# s.add(4)
# print(s)
# -------------------- #
# s = {1,2,3}
# s.remove(3)
# print(s)
# s = frozenset(s)
# s.add(4)
# print(s)
# -------------------- #
# x = 5
# y = 3.14
# z = "Hello"
# print(type(x),type(y),type(z))
# -------------------- #
# x=3+5j
# print(x,type(x))
# -------------------- #
# import random
# print(random.randrange(1,10))
# -------------------- #
# x = 'hello my name is "drishti"'
# y = "and my surname is 'sharma'"
# print(x,y)
# -------------------- #
# x = '''
# python
# is 
# an interpreted
# language
# '''
# print(x) # gets printed as it is 
# -------------------- #
# a = "hello, world"
# print(len(a))
# print(a[5])
# -------------------- #
# for x in ("drishti"):
#     print(x)
# -------------------- #
# txt="python is a beginner friendly language"
# print("leap" in txt)
# -------------------- #
# x = "character"
# print(len(x))
# print(x[2:6])
# print(x[1:8:2])
# print(x[9:0:-1])
# print(x[-2])
# print(x[-9:-1])
# print(x[-9:])
# -------------------- #
# a = " Document Parsing"
# print(a.lower())
# print(a.upper())
# print(a.strip())
# print(a.replace('a','o'))
# print(a.split())
# x = "upper"
# print(x.replace('p','l')) # replaces all p with l
# -------------------- # 
# c = 3
# txt = f"i ate {c} apples"
# print(txt)
# -------------------- # 
# s = 12.3
# txt = f"i saved {s:.2f} dollars"
# print(txt)
# t = 12
# txt = f"2 dozens bananas has {t*2} bananas"
# print(txt)
# -------------------- # 
# print(bool("hello")) #true
# print(bool(115)) #true
# print(bool("no")) #true
# print(bool(" ")) #true
# print(bool(-1)) #true
# print(bool(True)) #true
# print(bool("")) #false
# print(bool(0)) #false
# print(bool(0.00)) #false
# print(bool()) #false
# print(bool(())) #false 
# print(bool([])) #false
# print(bool({})) #false
# print(bool(False)) #false
# def myf():
#     return False # can return anything
# print(myf()) 
# -------------------- #
# s = {"apple","banana","green", "yellow"}
# print(s) # unordered sequence
# -------------------- #
# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:6])
# print(thislist[2:]) # same as 2:7, will print till the end
# -------------------- #
# myl= ["a","b","a","c"]
# myl.remove("a") #removes the 1st occurence in case of duplicates
# print(myl) 
# -------------------- #
# l = [1,2,3,4,5,7]
# l.pop() # removes the last item by default if the index is not specified
# print(l)
# -------------------- #
# l = [1,2,3,4,5,7]
# del l[2] # deletes specific item
# del l # deletes the whole list
# print(l)
# -------------------- #
# l = [1,2,3,4,5,7]
# l.clear() #list remains, only the values are deleted
# print(l)
# -------------------- #
# thislist = ["a","B","b"]
# thislist.sort() # in this case capital will always come first
# print(thislist)
# -------------------- #
# thislist = ["a","B","b"]
# thislist.sort(key=str.lower) # in this case capital will always come first
# print(thislist)
# -------------------- #
# x = [10,20,30,40,10,50]
# print(x.index(10)) # prints index of only 1st occurence
# -------------------- #
# x = [30,20,10]
# x.reverse()
# print(x) # updates the list -> saves in reverse order
# -------------------- #
# x = 10,20,30
# print(type(x)) #tuple created -> can also be created without () parantheses
# -------------------- #
# t = 10,30
# y = (20,) # gets treated as tuple
# t = t + y
# print(t) 
# z = (52) # gets treated as int
# -------------------- #
# t = 'pen','table','bottle' #packing
# print(t) 
# x, y, z = t # unpacking
# print(x,y,z)
# -------------------- #
# t = 'pen','table','bottle'
# print(t) 
# (*x,)= t # values will be assigned to a single var with the use of *
# print(x)
# -------------------- #
# t = {1,True,False,0}
# print(t) #True = 1, False= 0, only 1 of each gets printed
# -------------------- #
# s = {10,20,30}
# t = {40,60,70}
# s.update(t) # gets added
# print(s) # prints in any order as a single set
# -------------------- #
# s = {10,20,30}
# t = 50,60,40 # can be any object
# s.update(t)
# print(s) 
# -------------------- #
# s = {10,20,3,'apple'}
# s.remove(4) # if value doesnt exist raises an error
# s.discard(4) # if value doesnt exist doesnt raise an error, does nothing
# print(s)
# -------------------- #
# x = {10,20,30,50}
# x.pop() # pops random number
# print(x)
# -------------------- #
# x = {10,20,30,50}
# x.clear() #removes item, set exists
# print(x)
# -------------------- #
# s1 = {10,20}
# s2 = {20,30,40}
# s3 = s1.union(s2)
# # or can also use
# # s3 =  s1 | s2
# print(s3)
# -------------------- #
# s1 = {10,20}
# s2 = {30,40}
# s2.update(s1)
# print(s2)
# -------------------- #
# s1 = {10,20}
# s2 = {20,30,40}
# s3 = s1.intersection(s2) # will print only the duplicate
# print(s3)
# -------------------- #
# s1 = {10,20,40}
# s2 = {20,30,40}
# s3 = s1.difference(s2) 
# print(s3)
# -------------------- #
# s1 = {10,20,40}
# s2 = {20,30,40}
# s3 = s1.symmetric_difference(s2) 
# print(s3)
# -------------------- #
# s = frozenset({10,20,30})
# # s.pop() # throws error as frozen sets are immutable, cannot even add/remove elements
# del s
# print(s)
# -------------------- #
# a = {
#     'name':'drishti',
#     'age':22
# }
# print(len(a)) #counts key value pairs
# -------------------- #
# a = dict(name='abc',country='xyz')
# print(a)
# -------------------- #
# d = {
#     'name': "drishti",
#     'age' : 22
# }
# print(d.keys()) # returns keys
# -------------------- #
# d= {
#     'name':'abc',
#     'age': 18,
#     'city': 'indore'
# }
# print(d.keys())
# dkeys = d.keys()
# d['drink']='coffee'
# print(dkeys) # updates in dict shows in keys
# -------------------- #
# d = {
#     'color':'green',
#     'brand':'thumbs up'
# }
# print("keys: ",list(d.keys()))
# print("values: ",list(d.values()))
# print("items: ",list(d.items()))
# -------------------- #
# d = {
#     'color':'green',
#     'brand':'thumbs up'
# }
# d['color'] = 'blue'
# print("items: ",list(d.items()))
# -------------------- #
# d = {
#     "rno":101,
#     "name": "rachel"
# }
# d.update({'pno':301})
# print(d)
# -------------------- #
# d = {
#     'color': 'orange',
#     'fruit': 'lemon',
#     'taste':'sour'
# }
# print(d)
# d.pop('taste')
# print(d)
# -------------------- #
# d = {
#     'color': 'orange',
#     'taste':'sour',
#     'fruit': 'lemon'
# }
# print(d)
# d.popitem()
# print(d)
# -------------------- #
d = {
    'color': 'orange',
    'taste':'sour',
    'fruit': 'lemon',
    'count':3
}
print(d)
e = d.pop('color')
print(e)