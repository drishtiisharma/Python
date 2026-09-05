def deco1(func):
    def wrapper1():
        print("deco1 called")
        return func()
    return wrapper1

def deco2(func):
    def wrapper2():
        print("deco2 called")
        return func()
    return wrapper2

@deco1
@deco2
def greet():
    return "hellooo"

print(greet())