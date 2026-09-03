# def func(a,b):
#     if a*b <=1000:
#         return a*b
#     else:
#         return a+b

# x = int(input())
# y = int(input())

# print(func(x,y))

# for x in range(0,10):
#     y = x-1
#     if x == 0:
#         y = 0
    
#     print(x,"+",y,":",x+y)

# str = 'pynative'
# for x in range(0,len(str),2):
#    print(str[x])

# str = 'pynative'
# words = str[0::2]
# for x in words:
#     print(x)

# str = 'pynative'
# n = int(input())
# words = str[n:]
# print(words)

# using a 3rd variable
# a = int(input())
# b = int(input())
# c = b
# b = a
# a = c
# print(a,b)

# without using a 3rd variable
# a = int(input())
# b = int(input())
# print(a,b)
# a = a+b
# b = a-b
# a = a-b
# print(a,b)

# another way
# a = int(input())
# b = int(input())
# print(a,b)
# a,b = b,a
# print(a,b)

# factorial
# f = 1
# n = int(input())
# for i in range(f,n+1):
#     f *= i
# print(f)

# fruits = ["apple", "banana", "cherry", "date", "elderberry"]
# fruits.append('mango')
# print(fruits)
# fruits.pop(1)
# print(fruits)

# text = "Python"
# for x in range(len(text)-1,0,-1):
#     print(text[x])
## or 
# words = text[::-1]
# print(words)

# count = 0
# sentence = "Learning Python is fun!"
# vowels ='aeiou'
# for x in sentence.lower():
#     if x in vowels:
#         count += 1

# print(count)

# nums = [45, 2, 89, 12, 7]
# print(max(nums))
# print(min(nums))
## other way
# max = nums[0]
# min = nums[0]
# for x in nums:
#     if max<=x:
#         max = x
#     elif min>x:
#         min = x
#     else:
#         pass
# print(max,min)


# data = [1, 2, 2, 3, 4, 4, 4, 5]
# out = []
# for x in data:
#     if out.count(x) == 0:
#         out.append(x)
# print(out)

# x = [10, 20, 30, 40, 30]
# if x[0] == x[len(x)-1]:
#     print("matcheddd")
# else:
#     print(":(")

# str = "Emma is good developer. Emma is a writer"
# sub = input()
# c = str.count(sub)
# print(c)

# for x in range(1,6):
#     for y in range(x):
#         print(x,end =' ')
#     print('\n')