'''
lambda function
---------------

small anonymous function written in a single line

'''
# map : applies a function to every element of the iterable
nums = [7,8,54,65,4,9]
squares = list(map(
    lambda n: n **2,
    nums
))
print(type(squares),squares)

# filter : keeps elements for which a function returns a true result

numbers = [1, 2, 3, 4, 5, 6]

evens = list(filter(
    lambda n : n % 2 == 0,
    numbers
))
print(evens)

