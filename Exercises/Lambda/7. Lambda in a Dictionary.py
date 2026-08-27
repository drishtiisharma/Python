# Exercise 7: Lambda in a Dictionary
# Problem Statement: Store four lambda functions in a dictionary under the keys "add", "sub", "mul", and "div". Each lambda should take two numbers and perform the corresponding arithmetic operation. Use the dictionary to build a simple calculator that looks up the operation by key and applies it to two operands.
d = {
    "add":lambda a,b : a+b,
    "sub":lambda a,b : a-b,
    "mul":lambda a,b : a*b,
    "div":lambda a,b : a/b
}
a,b = 10,30
for name,func in d.items():
    print(f"{name}:{func(a,b)}")