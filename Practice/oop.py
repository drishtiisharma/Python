## abstraction
# from abc import ABC, abstractmethod
# class shape(ABC):
#     @abstractmethod
#     def area(self):
#         pass
# class Circle(shape):
#     def area(self,r):
#         return 3.14*r*r
# class Rectangle(shape):
#     def area(self,l,b):
#         return l*b
# c = Circle()
# r = Rectangle()
# print(
# c.area(10),
# r.area(10,20)
# )


# from abc import ABC, abstractmethod
# class Person(ABC):
#     def role(self):
#         pass
# class Student(Person):
#     def role(self):
#         return "student"
# class Teacher(Person):
#     def role(self):
#         return "Teacher"
# class Staff(Person):
#     def role(self):
#         return "staff"

# s = Student()
# t = Teacher()
# st = Staff()

# print(s.role(),t.role(),st.role())

## encapsulation
# class Student:
#     def __init__(self,name,marks):
#         self.name = name
#         self.__marks = marks
#     def get_marks(self):
#         return self.__marks

# s = Student('drishti',95)
# print(s.name,s.get_marks())

# class Person:
#     def __init__(self, role):
#         self._role = role

# class Student(Person):
#     def show_role(self):
#         print(self._role)   # child class accessing parent variable

# s = Student("student")
# s.show_role()

## polymorphism
# class Animal:
#     def sound(self):
#         pass
# class Dog:
#     def sound(self):
#         print('woof')
# class Cat:
#     def sound(self):
#         print("meow")

# d = Dog()
# c = Cat()
# d.sound()
# c.sound()

# class Animal:
#     def __init__(self,name):
#         self.name = name
#     def sound(self):
#         pass

# class Dog(Animal):

#     def __init__(self,name):
#         super().__init__(name)
    
#     def sound(self):
#         print(self.name,'woofs')


# class Cat(Animal):
#     def __init__(self,name):
#             super().__init__(name)
#     def sound(self):
#         print(self.name,"meows")

# d = Dog('jack')
# d.sound()
# c = Cat('sandy')
# c.sound()

# super
# class Animal:
#     def sound(self):
#         print("animal makes sound")
# class Dog(Animal):
#     def soundd(self):
#         super().sound()
#         print("woofs")

# d = Dog()
# d.soundd()

## inheritance
# class Vehicle:
#     def info(self,brand, color):
#         print('Parent class: Vehicle')
# class Car(Vehicle):
#     def info(self,brand,color):
#         super().info(brand,color)
#         print("car details:")
#         print("brand",brand)
#         print('color',color)
# class Ship(Vehicle):
#     def info(self,brand,color):
#         print("ship details:")
#         print("brand",brand)
#         print('color',color)
# c= Car()
# c.info('toyota','white')
# s = Ship()
# s.info('MCP','green')