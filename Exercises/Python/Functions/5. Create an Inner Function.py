# Exercise 5. Create an Inner Function
def outer(a,b):
    def inner(a,b):
        return a + b 
    add = inner(a,b)
    return add+5


print(outer(10,5))