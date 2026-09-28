# Exercise 5: Reduce Basics
# Problem Statement: Use functools.reduce() with a lambda to find the product of all numbers in a list. The function should multiply each element cumulatively from left to right until a single value remains.
from functools import reduce
numbers = [1, 2, 3, 4, 5]
p = reduce(lambda acc,n : acc*n, numbers)
print(p)