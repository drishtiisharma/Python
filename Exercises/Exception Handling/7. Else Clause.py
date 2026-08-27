# Exercise 7: Else Clause
# Problem Statement: Write a function safe_sqrt(value) that converts user input to a float and calculates its square root. Use the try-except-else pattern so that a success message is printed only when no exception is raised, keeping success and error paths cleanly separated.
import math
def safe_sqrt(value):
    try:
        x = float(value)
        res = math.sqrt(x)
    except ValueError:
        print("enter a valid value")
    else:
        print(f"square root of {value} is : {res:.2f}")

safe_sqrt(102)
safe_sqrt("hello")