# Exercise 8: Chaining Map & Filter
# Problem Statement: Given a list of integers that includes negative numbers, use filter() to remove all negatives, then use map() to square the remaining values. Chain the two operations so no intermediate named variable is required.
numbers = [-3, -1, 0, 2, 4, -2, 5, 7]
op = list(
    map(
        lambda x: x**2,(filter(lambda x : x>=0, numbers))
    ))
print(op)