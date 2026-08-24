# def fun(): # runs only when called
#     print("sup")
# fun()
# ------------------------------------- #
# c->f : f = (c*9/5)+32
# f->c : c = (f-32)*5/9
# c->k : k = c+273.15
# k->c : c = k-273.15
# f->k : k = (f-32)*5/9 + 273.15
# k->f : f = (k-273.15) * 9/5 + 32
# def temp():
#     c = float(input())
#     f = (c*9/5) + 32
#     print(f)

# temp()
# ------------------------------------- #
# def bill():
#     price = float(input("Total sum: "))
#     global total
#     total = price + price * 0.18 # 18% tax
#     return total

# bill()
# print("Thanks for using our service, here's the payable amt.: ")
# if total>1500:
#     print(total)
# else:
#     total=total+50
#     print(total)
# ------------------------------------- #
# def greet():
#     return "yo"
# print(greet())
# ------------------------------------- #
# def sup():
#     print("yo") # simple print
#     # return 2+3 # returns none if absent
# print(sup()) # returns whatever value is passed at the end of the function
# ------------------------------------- #
# def ask(fname,lname):
#     print("Howdy? ",fname,lname)
    
# ask('drishti') # will throw error as count(arguments)!=count(ask)
# ------------------------------------- #
# def name(name='drishti'): # default parameter value
#     print("sup",name)
# name()
# name('khushi')
# ------------------------------------- #
# def nums():
#     list = map(int,input().split())
#     for x in list:
#         print(x)

# nums()
# ------------------------------------- #
# def list():
#     return [10,'a',5,'b']
# def tuple():
#     return (10,50,50,10)
# def set():
#     return {10,5,0,14,5}
# def dict():
#     return {'name':'drishti','age':15}

# print(list())
# print(tuple())
# print(set())
# print(dict())

#can return any datatype
# ------------------------------------- #
# def greet(name,/):
#     print("sup",name)
     
# greet('drishti')
# greet(name = 'drishti') # will throw error -> as position only argument
# ------------------------------------- #
# def greet(*,name):
#     print("sup",name)
     
# greet(name = 'drishti') 
# greet('drishti')
# ------------------------------------- #
# def greet(*,name,/): # this wont work
#     print("sup",name)
     
# greet(name = 'drishti') 
# greet('drishti')

# def greet(name,/,*,lastname): 
#     print("sup",name, lastname)

# greet('drishti',lastname ='sharma') # only this will execute
# greet(name = 'drishti', lastname = 'sharma') 
# greet('drishti','sharma')
# greet(name = 'drishti', 'sharma')
# ------------------------------------- #
# def kids(*names):
#     print("both kids' names:", names)
#     print("youngest kid:",names[1])
# kids('drishti','khushi')
# ------------------------------------- #
# def greet(name,age,category,place):
#         print(name,age,category,place)
     
# # greet(name = 'john','56','gen','us') # will throw error as positional argument comes first
# # greet('john',age = '56','gen','us') # will throw error as positional argument will ALWAYS come before ALL keyword arguments
# greet('john','56','gen',place = 'us') # no error; rule followed
# greet('john','56',category = 'gen',place = 'us') # no error; rule followed
# ------------------------------------- #
# def combos(reaction,*rest):
    # for name in rest:
    #     print(reaction, name)
#   print(reaction,'&',rest[2])
    # print(type(rest))

# combos('black','pink','blue','orange') # this works
# # combos('black','pink',*rest = 'blue',*rest = 'orange') # will throw error
# ------------------------------------- #
# def combos(sent,**name):
#     print(sent)
#     print(name['fname'],name['lname']) # accessing like dictionary
#     print(type(name))

# combos("My full name is: ",fname='drishti',lname='sharma') # positional 1st, keyword later
# ------------------------------------- #
# def combos(*sent,**name):
#     print('class:',type(sent),'\n',sent)
#     print('class:',type(name),'\n',name)

# combos('my','full','name','is',fname='drishti',lname='sharma') # positional 1st, keyword later
# ------------------------------------- #
# def my_function(a, b, c):
#   return a + b + c

# numbers = [1, 2, 3]
# result = my_function(*numbers)
# print(result)

# def my_function(name, lastname):
#   return "hello " + lastname + name

# dc = {'name': 'drishti', 'lastname':'sharma'}
# result = my_function(**dc)
# print(result)
# ------------------------------------- #
# def fun():
#     x = 300
#     print(x)
# fun() # will print
# print(x) # will throw error as, x is local variable
# ------------------------------------- #
# def fun():
#     x =  300
#     def inner():
#         print(x)
#     inner()
# fun()
# ------------------------------------- #
# x = 200
# def fun():
#     x = 300
#     print(x)
# print(x) # prints 200
# fun() # prints 300
# ------------------------------------- #
# x = 10
# def fun():
#     global x # updates the global value
#     x = 20
#     print(x)
# fun() # prints 20
# print(x) # prints 20
# ------------------------------------- #
# def out():
#     x = 10
#     def inn():
#         nonlocal x # must be used before any use of x
#         x = 30
#     inn()
#     print(x)
# out()
# ------------------------------------- #
# x = "global"

# def outer():
#   x = "enclosing"
#   def inner():
#     x = "local"
#     print("Inner:", x)
#   inner()
#   print("Outer:", x)

# outer()
# print("Global:", x)
# ------------------------------------- #
# def dec(func):
#     def inn():
#         print("starting...")
#         func()
#     return inn

# @dec
# def func():
#     print("hello")

# func()
# ------------------------------------- #
# def check(func):
#     def wrapper():
#         print("Checking...")
#         func()
#     return wrapper

# @check
# def delete_file():
#     print("File deleted")

# @check
# def download_file():
#     print("File downloaded")

# delete_file()
# download_file()
# ------------------------------------- #
# def check(greet):
#     def wrapper(name):
#         print("checking...")
#         greet(name)
#     return wrapper

# @check
# def greet(name):
#     print("hello",name)

# greet("drishti")
# ------------------------------------- #
# def check(func):
#     def wrapper(*args,**kwargs):
#         print("checking...")
#         func(*args,**kwargs)
#     return wrapper

# @check
# def greet(name):
#     print("hello",name)

# @check
# def addd(a,b):
#     print(a-b)

# greet("drishti")
# addd(a=10,b=20)
# ------------------------------------- #
# def greet(func):
#     def wrapper():
#         print("Good")
#         func()
#     return wrapper

# def time(func):
#     def wrapper():
#         print("evening")
#         func()
#     return wrapper

# @greet 
# @time
# def name():
#     print("drishti")

# name()
# ------------------------------------- #
# def myfunction():
#   return "Have a great day!"

# print(myfunction.__name__)
# ------------------------------------- #
# m = lambda a,b,c : a + b + c # must use the same var name as arguments
# print(m(10,20,30)) 
# ------------------------------------- #
# l = [10,20,30,40]
# res = list(map(lambda x : x * 2, l))
# print(res)
# ------------------------------------- #
# l = [1,20,30,40]
# res = list(filter(lambda x : x % 2 == 0, l))
# print(res)
# ------------------------------------- #
# l = ["cat","environment","bat","rainy"]
# res = sorted(l,key = lambda x: len(x))
# print(res)
# ------------------------------------- #
# l = ["cat","environment","bat","rainy"]
# res = sorted(l,key = lambda x: len(x), reverse = True)
# print(res)
# ------------------------------------- #
# factorial
# def rec(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * rec(n-1)
# n = int(input())
# print(rec(n))
# ------------------------------------- #
# def pr(n):
#     if n == 0:
#         return
#     pr(n-1)
#     print(n)
# pr(5)
# ------------------------------------- #
# reversed string
# def rev(s):
#     if len(s) == 0:
#         return ''

#     return rev(s[1:])+s[0]

# print(rev("helloworld"))
# ------------------------------------- #
# fibonacci number
# def fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# print(fibonacci(6))
# ------------------------------------- #
def num():
    print("giving 1")
    yield 1
    print("giving 2")
    yield 2
    print("giving 3")
    yield 3
g = num()

print(next(g))
print(next(g))
print(next(g))

