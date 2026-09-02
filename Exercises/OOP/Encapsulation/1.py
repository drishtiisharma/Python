# Create a Student class with public attributes for name and age, and display them.

class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
s = Student('drishti',22)
print(s.name,s.age)