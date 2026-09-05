## factorial
# n = int(input())
# f = 1
# for i in range(1,n+1):
#     f*=i
# print(f)

## palindrome
# def palindrome(x):
#     if x < 0:
#         return False
#     og = x
#     rev = 0

#     while x > 0:
#         digit = x % 10
#         rev = (rev*10) + digit
#         x = x // 10 
#     return og == rev

# print(palindrome(121))
# print(palindrome(1234))

# str = "racecar"
# new = str[::-1]
# if str == new:
#     print("palindrome")
# else:
#     print("nope")

## armstrong number

# def armstrong(x):
#     p = len(str(x))

#     sum = 0
#     temp = x 

#     while temp>0:
#         digit = temp % 10
#         sum += digit ** p
#         temp = temp // 10
#     return sum == x

# print(armstrong(153))

# prime no
# def prime(n):
#     if n<=1:
#         return False
#     for i in range(2,n):
#         if n % i == 0:
#             return False
#     return True

# print(prime(23))

# armstrong series

# s = int(input())
# e = int(input())

# for n in range(s,e+1):
#     temp = n
#     sum = 0
#     power = len(str(n))

#     while temp > 0:
#         digit = temp % 10
#         sum += digit ** power
#         temp//=10
    
#     if sum == n:
#         print(n)

# palindrome series

# s = int(input())
# e = int(input())

# for n in range(s,e+1):
#     rev = 0
#     temp = n
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp //= 10
#     if rev == n:
#         print(n)

## fibonacci

# n = int(input())
# a = 0 
# b = 1
# for i in range(n):
#     print(a)
#     a,b = b,a+b

# def fib(n):
#     a,b = 0,1
#     for i in range(n):
#         print(a)
#         a,b = b,a+b
# fib(3)

# def sum(n):
#     x = 0
#     for i in range(0,n):
#         x+=i
#     return x
# print(sum(3))
