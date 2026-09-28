# Exercise 4: Filter Basics
# Problem Statement: Use filter() with a lambda to extract only the even numbers from a list of integers. Collect the results into a new list and print it.
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new = list(filter(lambda x : x%2 == 0, numbers))
print(new)