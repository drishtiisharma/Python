# Factorial: of a number n is the product of all positive integers from 1 to n
n = int(input())
fact = 1
for i in range(1,n+1):
    fact = fact * i # fact(1) to n(i)
print(fact)