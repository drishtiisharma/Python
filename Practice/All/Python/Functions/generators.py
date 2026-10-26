'''
generators
----------

function that produces values one at a time using the same yield keyword instead of returning all values at once

useful when working with large amounts of data becausse they can produce values as needed rather than storing an entire result in memory

'''


def getnums():
    yield 1
    yield 2
    yield 3

numbers = getnums()
print(next(numbers))
print(next(numbers))