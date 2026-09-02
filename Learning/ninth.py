# def changecase(func):
#     def myinner():
#         return func().upper()
#     return myinner

# @changecase
# def myfunction():
#     return "Hello"

# print(myfunction())

## decorator with func args

def logger(func):

    def wrapper(name):
        print("wrapper func called...")
        return func(name)
    return wrapper

@logger
def greet(name):
    return "hello " + name

print(greet("drishti"))