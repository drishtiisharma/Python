# Exercise 4: Type Error Guard
# Problem Statement: Write a function add_values(a, b) that returns the sum of two values. If the arguments are of incompatible types (for example, a string and an integer), catch the TypeError and return a descriptive error message instead of crashing.
def add_values(a,b):
    
    try:
        return a+b
    except TypeError:
        return "ONLY int!"

print(add_values(10,"20"))
