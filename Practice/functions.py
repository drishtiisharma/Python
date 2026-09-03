## factorial
# def fact(n):
#     f = 1
#     if n in [0,1]:
#         return 1
#     else:
#         for i in range(1,n+1):
#             f*=i
#     return f
# print(fact(5))

## palindrome
# def pal(n):
#     temp = n
#     rev = 0
#     while temp > 0:
#         digit = temp % 10
#         rev = rev * 10 + digit
#         temp = temp // 10
#     return n == rev
# print(pal(121))

## armstrong
# def arm(n):
#     p = len(str(n))
#     s = 0
#     temp =  n
#     while temp > 0:
#         digit = temp % 10
#         s = s + digit ** p
#         temp = temp // 10
#     return n == s
# print(arm(153))

## prime
# def prime(n):
#     if n == [0,1]:
#         return "not prime"
#     else:
#         for i in range(2,n):
#             if n % i == 0:
#                 return "not prime"
#         return "prime"
# print(prime(2))    
# print(prime(25))

## sum of first n num
# def s(n):
#     sum = 0
#     for i in range(1,n+1):
#         sum+=i
#     return sum
# print(s(10))

## sum of all digits
# def digs(n):
#     s = 0
#     for i in range(len(str(n))):
#         digit = n % 10
#         s = s + digit
#         n = n // 10
#     return s
# print(digs(456))
