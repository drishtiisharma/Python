## Given a list, count how many times each element appears and store the result in a dictionary. Do not use Counter.

# l = ['apple','banana','apple']
# d = {}
# count = 1
# for x in l:
#     if x in d:
#         d[x] += 1
#     else:
#         d[x] = 1
# print(d)

## Using recursion, check whether a given string is a palindrome. Do not use slicing.

# def pal(n,rev=0):
#     if n == 0:
#         return rev
#     else:
#         return pal(n//10,rev*10 + n%10)
# n = 121
# if pal(n) == n:
#     print('palindrome')
# else:
#     print("not palindrome")

## Create a Student class with name and marks. Add a method that calculates the percentage and returns the grade.

# class Student:
#     def __init__(self,name,total,*marks):
#         self.name = name
#         self.total = total
#         self.marks = marks
    
#     def res(self):
#         t = sum(self.marks)
#         per = (t/self.total) * 100

#         if per >= 90:
#             return 'A'
#         elif per >= 80:
#             return 'B'
#         elif per >= 70:
#             return 'C'
#         else:
#             return 'D'

# c = Student('alice',500,80,90,96,80,85)
# print(c.res())

# Take a filename from the user, open the file, and count the total number of lines. Handle the case where the file does not exist.
name = input("enter file name: ")
try:
    with open(name,'r') as f:
        lines = f.readlines()
        print("file exists!")
        print('total lines:',len(lines))
        print(lines)
except FileNotFoundError:
    print("file doesnt exist")