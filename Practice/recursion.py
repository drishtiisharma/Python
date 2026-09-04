# def count(n):
#     if n == 0:
#         return
#     else:
#         count(n-1)
#         print(n)

# n = int(input())
# count(n)

# def rev(n):
#     if n == 0:
#         return
#     else:
#         print(n)
#         rev(n-1)
# rev(10)

# def fact(n):
#     if n in [0,1]:
#         return 1
#     else:
#         return n * fact(n-1)
    
# print(fact(5))

# def sum(n):
#     if n == 0:
#         return 0
#     else:
#         return n + sum(n-1)
 
# print(sum(10))

# def sdigits(n):
#     if n == 0:
#         return 0
#     else:
#         return n % 10 + sdigits(n//10)
    
# print(sdigits(123))

# def count(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + count(n//10)
# print(count(456))

# def p(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * p(a,b-1)
# print(p(2,3))

# def fib(n):
#     if n <= 1:
#         return n
#     else:
#         return fib(n-1) + fib(n-2)
# for i in range(3):
#     print(fib(i))




# ==================== Beginner ==================== #

## fact with recursion
# def fact(n):
#     if n in[0,1]:
#         return 1
#     else:
#         return n*fact(n-1)
# print(fact(5))


## print nums from 1 to n
# def show(i,n):
#     if i>n:
#         return 
#     else:
#         print(i)
#         show(i+1,n)
# show(1,10)


## print nums from 1 to n
# def show(i,n):
#     if i>n:
#         return
#     else:
#         print(n)
#         show(i,n-1)
        
# show(1,10)

## sum of first n natural numbers
# def s(n):
#     if n < 0:
#         return 0
#     else:
#         return n + s(n-1)

# print(s(10))

## sum of digits of a number
# def s(n):
#     if n == 0:
#         return 0
#     else:
#         return (n % 10) + s(n//10)
# print(s(123))
    
## count digits of a number
# def count(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + count(n // 10)
# print(count(0))
# print(count(12345))

## power of a number — a^b
# def p(a,b):
#     if b == 0:
#         return 1
#     else:
#         return a * p(a,b-1)

# print(p(2,3))


## even numbers from 1 to n
# def eve(n):
#     if n == 0:
#         return []
#     else:
#         res = eve(n-1)
#         if n % 2 == 0:
#             res.append(n)
#         return res
# print(eve(10))


## odd numbers from 1 to n
# def odd(n):
#     if n == 0:
#         return []
#     else:
#         res = odd(n-1)
#         if n % 2 != 0:
#             res.append(n)
#         return res
# print(odd(10))

## product of digits
# def prod(n):
#     if n == 0:
#         return 1
#     else:
#         return (n%10) * prod(n//10)
# print(prod(45))





# ==================== Random ==================== #

# def show(n):
#     if n == 0:
#         return 0
#     else:
#         print(n)
#         show(n-1)
# show(5)

# def digs(n):
#     if n == 0:
#         return 0
#     else:
#         return (n%10) + digs(n//10)
# print(digs(583))

# def count(n):
#     if n == 0:
#         return 0
#     else:
#         return 1 + count(n//10)
# print(count(48392))

def maximum(n):
    if len(n) == 1:
        return n[0]
    else:
        x = maximum(n[1:])
        if n[0]>x:
            return n[0]
        else:
            return x

print(maximum([4, 9, 2, 7, 5]))