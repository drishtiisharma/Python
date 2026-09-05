# x = int(input())
# rev = 0
# while x > 0:
#     digit = x % 10
#     rev = rev*10 + digit
#     x //= 10
# print(rev)

## or

# digits = len(str(x))
# for _ in range(digits):
#     digit = x % 10
#     rev = rev*10 + digit
#     x //= 10  


# print(rev)

# x = 1246
# sum = 0
# while x > 0:
#     digit = x % 10
#     sum+=digit
#     x //=10
# print(sum)

# n = int(input())
# for i in range(1,n+1):
#     sum = 0
#     for j in range(1,i+1):
#         sum+=j
#         print(j,end='')
#     print(':',sum)
#     print()