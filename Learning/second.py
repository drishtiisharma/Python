# x,y,z =  map(float,input().split())
# print(x,y,z)
# ------------------------------------- #
# s = "Coding on CodeChef"
# t = s.split()
# for x in t:
#     c = len(x)
#     print(x,'-',c)
# ------------------------------------- #
# x = int(input())
# y = int(input())

# print(x + y)
# ------------------------------------- #
# x,y,z = map(int,input().split())
# if x<y and y<z:
#     print("Increasing")
# elif x>y and y>z:
#     print("Decreasing")
# else:
#     print("Neither")
# ------------------------------------- #
# t = 10,20,30
# t[2] = 40
# print(t)
# ------------------------------------- #
# student_grades = {"Alice": 85, "Bob": 72, "Charlie": 90, "David": 65, "Eva": 88, "John": 45}

# name = str(input())
# if name in student_grades:
#     print(student_grades[name])
# else:
#     print("Not Found")
# ------------------------------------- #
# l = list(map(int,input().split()))
# s = l[0] * l[2]
# print (s)
# ------------------------------------- #
# n = int(input())
# i=f=1
# while i<=n:
#     f = f*i
#     i = i+1
# print(f)
# ------------------------------------- #
# for i in range(1):
#     print("sup")
# ------------------------------------- #
# n = int(input())
# s = 0
# for i in range(1,n+1):
#     s = s + i
# print(s) 
# ------------------------------------- #
# l = list(map(int,input().split()))
# for x in l:
#     if x > 10:
#         continue
#     else:
#         print(x*x)
# ------------------------------------- #
# n = map(int,input().split())
# for i in n:
#     p = i**(i+1)
#     print(p)
#     break
# ------------------------------------- #
# def isEven(num):
#     return num%2==0
# t = int(input())
# for i in range(t):
#     num = int(input())
#     if isEven(num):
#         print("Even")
#     else:
#         Printy("Odd")
# ------------------------------------- #
# l = '''
# Make a choice:
# 1. Addition
# 2. Subtraction
# 3. Multiplication
# '''
# while True:
#     print("enter 2 nums:")
#     a,b = map(int,input().split())
#     print(l)
#     choice = int(input())

#     match choice:
#         case 1:
#             print("Sum:",a+b)
#         case 2:
#             print("Difference:",a-b)
#         case 3:
#             print("Product",a*b)
#         case _:
#             print("Enter a Valid Choice")

#     q = input("want to try again? (Y/N)")
#     if q == 'n' or q == 'N':
#         print('Exited.')
#         break
# ------------------------------------- #
# i = 0
# while i<10:
#     i+=1
#     if i == 2:
#         continue
#     print(i)
# ------------------------------------- #
# i = 0
# while i < 6:
#  i+=1
#  if i == 3:
#   continue # break will stop the loop at 2
#  print(i)
# ------------------------------------- #
# for i in range(1,10,2): # can also increment through a 3rd parameter
#     print(i)
# ------------------------------------- #