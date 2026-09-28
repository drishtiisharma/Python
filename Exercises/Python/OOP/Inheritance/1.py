# Create a Person class and inherit it into Student and Teacher, adding student-specific information.

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
class Student(Person):
    def __init__(self,name,age,grade):
        super().__init__(name,age)
        self.grade = grade

class Teacher(Person):
    def __init__(self,name,age,salary):
        super().__init__(name,age)
        self.salary = salary

s = Student('alice',22,'A')
t = Teacher('john',34,32000)
print(s.name,s.age,s.grade)
print(t.name,t.age,t.salary)