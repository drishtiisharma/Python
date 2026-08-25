# # iterators
# t = ('apple',10,'banana',20,'cherry',30)
# it=iter(t) # take the iterable 't' and create an iterator from it, then store that iterator in 'it'
# print(next(it))
# print(next(it))
# print(next(it))
# ------------------------------------- #
# # iterable strings
# string = 'sprint'
# it=iter(string)
# print(next(it))
# print(next(it))
# print(next(it))
# ------------------------------------- #
# iterator to return numbers starting from 1
# class Nums:

#     # when using as an iterator, start from 1
#     def __iter__(self): 
#         self.a=1
#         return self 
    
#     # give the current num and increase by 1
#     def __next__(self): 

#         if self.a <=5:
#             x = self.a
#             self.a += 1
#             return x
#         else:
#             raise StopIteration
        
        
# myclass = Nums() # creating an object of the class
# it=iter(myclass) # start this object as an iterator

# for x in it:
#     print(x)
# ------------------------------------- #
# # date time
# from datetime import datetime

# # datetime.now returns the year, month, date, hour, minute, second, microsecond
# x = datetime.now()
# print(x.date())
# print(x.time())
# print(x.year)
# print(x.month)
# print(x.day)
# print(x.hour)
# print(x.minute)
# print(x.second)
# print(x.microsecond)
# print(x.weekday())
# print(x.isoweekday())
# print(x.strftime("%d-%m-%y"))
# print(x.isoformat())
# print(x.today())
# ------------------------------------- #
# from datetime import datetime
# x = datetime(2020, 5, 17) # returns time as 00:00:00
# print(x)
# ------------------------------------- #
# # format codes in datetime
# from datetime import datetime
# x = datetime.now()
# print(x.strftime("%a"))  # Mon
# print(x.strftime("%A"))  # Monday
# print(x.strftime("%w"))  # 1 (day of the week)
# print(x.strftime("%d"))  # 24 (day of the month)
# print(x.strftime("%b"))  # Aug
# print(x.strftime("%B"))  # August
# print(x.strftime("%m"))  # 08
# print(x.strftime("%y"))  # 26
# print(x.strftime("%Y"))  # 2026
# print(x.strftime("%H"))  # 11 (24hr format)
# print(x.strftime("%I"))  # 11 (12hr format)
# print(x.strftime("%p"))  # AM (am/pm)
# print(x.strftime("%M"))  # 39 (out of 59m)
# print(x.strftime("%S"))  # 51 (out of 59s)
# print(x.strftime("%f"))  # 094962 (microsecond)
# print(x.strftime("%z"))  # '' (empty, because no timezone is set)
# print(x.strftime("%Z"))  # '' (empty, because no timezone is set)
# print(x.strftime("%j"))  # 236 (day no. out of 365)
# print(x.strftime("%U"))  # 34 (week no. as sunday as 1st day of week)
# print(x.strftime("%W"))  # 34 (week no. as monday as 1stt day of week)
# print(x.strftime("%c"))  # Mon Aug 24 11:39:51 2026
# print(x.strftime("%C"))  # 20 (century)
# print(x.strftime("%x"))  # 08/24/26 (local version of date)
# print(x.strftime("%X"))  # 11:39:51 (local version of time)
# print(x.strftime("%%"))  # %
# print(x.strftime("%G"))  # 2026
# print(x.strftime("%u"))  # 1
# print(x.strftime("%V"))  # 35
# ------------------------------------- #
# # built-in math functions
# x = min(5,14,52,454)
# y = max(4521,45,1545.152,451)
# z = abs(10-35)
# a = pow(2,3)
# b = round(4.3)
# c = divmod(9,7)

# # sum can only sum up iterables like list, tuple or range, not two or more individual elements
 
# m = [10,20,30,40,50]
    
# # sum(range(1, 6)) 
# # sum([1, 2, 3, 4, 5])   
# # sum((1, 2, 3, 4, 5))   
 
# print(x)
# print(y)
# print(z)
# print(a)
# print(b)
# print(c)
# print(sum(m,3)) 

# ------------------------------------- #
# import math

# x = math.sqrt(144)
# y = math.ceil(1.4564541) # rounds upward to the nearest integer
# z = math.floor(1.4564541) # rounds downward to the nearest integer
# a = math.pi 

# print(x)
# print(y)
# print(z)
# print(a)
# ------------------------------------- #
# JSON -> python
# import json
# # some json data
# x =  '{ "name":"John", "age":30, "city":"New York"}'
# # parsing x
# # print(x)
# y = json.loads(x)
# # print(y)
# print(x[5]) # will return 'm'
# print(y['age'])
# ------------------------------------- #
# # python -> json
# import json
# # a python object (dict)
# x = {
#     'name':'drishti',
#     'age':19,
#     'city': 'indore'
# }
# print(x) # prints dict
# y = json.dumps(x)
# print(y) # prints json
# ------------------------------------- #
# import json

# x =  [10,20,304,50]
# print(type(x))
# y = json.dumps(x)
# print(type(y))

# a = 15.312
# print(type(a))
# b = json.dumps(a)
# print(type(b))

# m = True
# print(type(m))
# n = json.dumps(m)
# print(type(n))

# ------------------------------------- #
# import json
# x = '{"name": "John", "age": 30}'
# print(type(x))
# print(x)
# y = json.loads(x)
# print(type(y))
# print(y)
# ------------------------------------- #
# formatting json with json.dumps()
# import json

# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
# # indent
# y = json.dumps(x, indent = 3)

# #separators
# y = json.dumps(x, indent = 3, separators=(" ~ "," = "))
# print(y)
# # sort_keys
# y = json.dumps(x, indent = 3, sort_keys = True)
# print(y)
# ------------------------------------- #
# regex
# import re
# s = "the rain in spain"

# t = re.findall("ai",s) # finds all occurences and returns a list
# print(len(t))
# print(t)

# x = re.search("ai",s) # finds the first match
# print(x.start()) # finds the position

# r = re.split("\s",s) # splits acc to specified pattern and returns the pieces as a list
# print(r)

# m = re.split("\s",s,1)
# print(m)

# n = re.sub("spain","summer",s)
# print(n)
# ------------------------------------- #
# 

# ------------------------------------- #

# import re

# txt = "The rain in Spain"

# #Check if the string has any a, r, or n characters:

# x = re.findall("[arn]", txt)

# print(x)

# if x:
#   print("Yes, there is at least one match!")
# else:
#   print("No match")
# ------------------------------------- #
# import re

# pattern = r"[\w.%+-]+"
# text = "user.name_123%+-"
# match = re.match(pattern, text)
# print(match.group())
# ------------------------------------- #
# import mod
# mod.num(10)
# ------------------------------------- #
# import mod as mx # renaming module / using an alias
# print(mx.person1['age'])
# ------------------------------------- #
# from mod import num
# num(20)

# from mod import person2
# person2['name'] = 'jen'
# print(person2['name'])

# import platform
# x = dir(platform)
# print(x)
# ------------------------------------- #
# from mod2 import sub
# print(sub(20,30))
from datetime import datetime

x = datetime.now()
print(x.strftime("%H %p"))
