'''
DECORATOR
---------

is a function that adds extra functionality to another function without changing the original function's code

'''

def deco(greet):
    def wrapper():
        print("before function")
        greet()
        print("after function")

    return wrapper

@deco
def greet():
    print("hellooo")

greet()


# passing argument
def deco(greet):
    def wrapper(name):
        greet(name)

    return wrapper

@deco
def greet(name):
    print("hellooo",name)

greet('drishti')

# multiple decorators
def say_hi(func):
    def wrapper(name):
        print("hiiii")
        func(name)
    return wrapper

def greet(func):
    def wrapper(name):
        print("have a great day!")
        func(name)
    return wrapper

@say_hi
@greet
def func(name):
    print(name)


func("janice")