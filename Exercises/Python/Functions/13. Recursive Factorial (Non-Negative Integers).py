# Exercise 13. Recursive Factorial (Non-Negative Integers)
def fact(num):
    if num:
        return num * fact(num-1)
    elif num<=1:
        return 1

print(fact(5))

