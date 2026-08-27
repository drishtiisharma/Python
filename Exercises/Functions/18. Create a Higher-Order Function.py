# Exercise 18. Create a Higher-Order Function
# A Higher-Order Function is a function that treats other functions as parameters. This allows you to write extremely generic code that can do anything depending on what logic you “plug into” it.

def apply_operation(func,x,y):
    return func(x,y)

def add(a,b): return a+b
def sub(a,b): return a-b

a = apply_operation(add,10,20)
print(a)