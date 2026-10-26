'''
OBJECT ORIENTED PROGRAMMING
===========================

class : defines what an object should be like
object : is created based on that classs

examples:
class : fruit
objects of 'fruit' class : mango,apple,strawberry


** almost everything in python is an object

'''

class VariablePrint:
    x = 24

vp = VariablePrint()
print(vp.x)


class Students:
    def __init__(self,name):
        self.name = name 
    def display(self):
        print(self.name, "is studying")

s1 = Students("Alice")
s2 = Students("Bob")

for x in (s1,s2):
    x.display()


# constructors


'''
__new__() : a special method that creates a new object


__init__() : initializes that object by assigning its attributes. 

Python calls __new__() first and then __init__().

'''
class Student:
    def __new__(cls,name):
        print("creating an object")
        return super().__new__(cls)
    def __init__(self,name):
        print("object initialized")
        self.name =  name

s1 = Student("Alice")
print(s1.name)