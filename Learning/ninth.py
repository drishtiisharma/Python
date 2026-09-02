# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello"

# print(myfunction())

## decorator with func args

# def logger(func):

#     def wrapper(name):
#         print("wrapper func called...")
#         return func(name)
#     return wrapper

# @logger
# def greet(name):
#     return "hello " + name

# print(greet("drishti"))

## multiple decorators

def log1(func):

    def wrapper(name):
        print("log1 checking...")
        return func(name)
    return wrapper

def log2(func):

    def wrapper2(name):
        print("log2 checking...")
        return func(name)
    return wrapper2

@log1
@log2
def greet(name):
    return "hellooo " + name

print(greet('drishti'))