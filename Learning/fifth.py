# x = 12.6
# print(int(x)) # prints 12
# y = 'hello'
# print(int(y)) # throws ValueError
# ------------------------------------- #
# try except
# try:
#     print(x)
# except:
#     print("value not given")
# ------------------------------------- #
# try:
#     x = 10 / 0
# except ZeroDivisionError:
#     print("you shouldnt be doing that")
# ------------------------------------- #
# try:
#     x = int(input())
#     if x>100:
#         raise ValueError("the number must not exceed 100...")
#     print(x / 10)
# except TypeError:
#     print("enter only nums")
# except ZeroDivisionError:
#     print("you cant do that...")
# else:
#     print("you successfully divided the num!!")
# finally:
#     print("......")
# ------------------------------------- #
# # using packages
# from camelcase import CamelCase
# y = "helloworld"
# print(CamelCase().hump(y))
# ------------------------------------- #
# none
# x = None
# print(x) # None
# print(type(x)) # <class 'NoneType'>
# ------------------------------------- #
# result = None
# res = 30
# if result is None or res is None:
#     print("No result yet")
# else:
#     print("..........")
# ------------------------------------- #
# print(bool(None)) # False
# ------------------------------------- #
# def myfunc():
#     x = 5

# print(myfunc())
# # returns None because there's no return statement
# ------------------------------------- #
# # string formatting
# name = "Drishti"
# print(f"Hello {name}")

# print(f"{20*3}")

# #format specifying
# print(f"Price : {206:.2f}")

# price = 5900000
# txt = f"The price is {price:,} dollars"
# print(txt)

# quantity = 3
# itemno = 567
# price = 49
# print(f"I want {quantity} pieces of item number {itemno} for {price:.2f} dollars.")
