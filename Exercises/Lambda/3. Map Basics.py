# Exercise 3: Map Basics
# Problem Statement: Use map() with a lambda to convert a list of temperatures from Celsius to Fahrenheit. The conversion formula is F = (C × 9/5) + 32. Collect the results into a new list and print it.
# f = (c*9/5) + 32
celsius = [0, 20, 37, 100]
fahrenheit = list(map(lambda x : (x*9/5)+32, celsius)) # map() returns a lazy iterator, so wrap it in list() to get a concrete list you can print.
print(fahrenheit)