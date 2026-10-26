'''
ARGUMENTS
---------
actual value passed to the function when we call it


PARAMETERS
----------
variables written in a function's definition


'''


def greet(name): # name is a parameter
    print("hello",name)

greet('john') # 'john' is an argument


def student(name,age=18):
    print(name,age)

student("max")
student("alex",20)
student(age= 23,name='gwen')

'''
*args
-----
allows a function to accept any number of positional arguments - available as a tuple


**kwargs
--------
allows a function to accept any number of keyword arguments - available as a dictionary

'''
def addn(*args):
    print(args)
    print(type(args))

    res = 0
    for number in args:
        res += number

    return res

print(addn(10,5,85))
print(addn(18,55,6.74,45))

def intro(**kwargs):
    print(kwargs)
    print(type(kwargs))

    for key,value in kwargs.items():
        print(key,":",value)

intro(name='alice',age = 20)
intro(name='jessica',age = 48,city = 'nyc')

def desc(name,**kwargs):
    print(name)
    print(kwargs)

desc('Python',type='language',discovered=1991)

# unpacking

def add(a,b,c):
    return a+b+c
numbers = [564,7465,496]
print(add(*numbers))