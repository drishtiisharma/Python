'''
exception handling
==================

syntax error : flaws in code that violates language rules
exception: logical flaws/error in code that occurs at runtime and interrupts normal execution

try : code that might cause error
except : handles a specific error
else : executes only when try block finishes without an exception
finally : executes whether an error occurs or not
raise : lets us manually generate an exception when a condition iss valid
'''


'''
some built-in exceptions
========================

NameError : variable doesnt exist
TypeError : when two diff types are combined
ValueError : wrong data type value in a specific data type var
ZeroDivisionError : when divisor is zero
ImportError : when imported module doesnt exist
'''

try:
    x = 10
    res = x / 0
except ZeroDivisionError:
    print("nope, cannot divide by zero.")


try:
    num = int(input())
except ValueError:
    print("nuh uh, not an int")


try:
    a =  input("type something...")
    b = 10
    try:
        anss = a+c
    except NameError:
        print("one of them, doesnt exist")
    ans = a+b
except TypeError:
    print("what u just entered doesnt match the type defined")
finally:
    print("it ends...")


try:
    x = 20/10
except ZeroDivisionError:
    print("divisor cannot be zero")
else:
    print(x)
finally:
    print("divison completed")



try:
    age = int(input("enter a negative num: "))
    if age<0:
        raise ValueError("age cant be negative")
except ValueError as e:
    print("reason: ",e)


