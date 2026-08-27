# Exercise 2: Division Safety
# Problem Statement: Create a function safe_divide(a, b) that divides a by b. If b is zero, handle the ZeroDivisionError and return None instead of letting the program crash.
def safe_divide(a,b):
    try:
        res = a/b
        print(res)
    except ZeroDivisionError:
        print("None")

safe_divide(10,2)
safe_divide(10,0)