# Exercise 1: Basic Try-Except
# Problem Statement: Write a Python program that asks the user to enter a number. If the input is not a valid integer, raise a ValueError and display a helpful error message instead of crashing.
try:
    x = int(input("enter a num: "))
except ValueError:
    print("enter a valid integer")