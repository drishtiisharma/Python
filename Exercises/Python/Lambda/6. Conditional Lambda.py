# Exercise 6: Conditional Lambda
# Problem Statement: Write a lambda that takes a single integer and returns the string "even" if the number is divisible by 2, or "odd" otherwise. Assign it to a variable named parity and test it on several values.
parity =  lambda x :"even" if x%2==0 else "odd"
print(parity(4))
print(parity(7))
print(parity(0))
print(parity(22.44))