# class MyClass:
#     x = 5

# obj = MyClass()
# # print(x) # will throw error
# print(obj.x) # will show value
# del obj
# print(obj.x)

# class Name:
#     pass

# class wow:
#     x = 'wow'
# w = wow()
# print(w.x)
# ------------------------------------- #
# # __init__() method
# class Dog:
#     def __init__(self,breed,color):
#         self.breed = breed
#         self.color = color
# d = Dog('Labrador','black') # will store the value
# print(d.breed,d.color)

# class Person:
#     def details(self, namewhy , age):
#         self.name = name
#         self.age = age

# p1 = Person()
# p1.details("Emil", 36) # will have to set manually
# print(p1.name,p1.age)

# class Person:
#   def __init__(self, name, age=18):
#     self.name = name
#     self.age = age

# p1 = Person("Emil")
# p2 = Person("Tobias", 25)

# print(p1.name, p1.age)
# print(p2.name, p2.age)

# ------------------------------------- #
# # self parameter
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def greet(self):
#         print("Hello, my name is",self.name)

# p1 = Person('john',36)
# p1.greet()

# class Person:
#     def __init__(self,name,age = 20):
#         self.name = name 
#         self.age = age
# p = Person("John",30) # cannot miss any argument
# print(p.name,p.age) # will print 30 not 20

# class Person:
#     def __init__(self,name):
#         self.name = name

#     def printname(self):
#         print(self.name)

# p = Person("John")
# p2 = Person("Alice")
# p.printname()
# p2.printname()

# class wow:
#     def __init__(wow,name):
#         wow.name = name
#         print("hello" , name)
# p = wow('drishti')

# class Car:
#     def __init__(self,brand,model,year):
#         self.brand = brand
#         self.model = model
#         self.year = year

#     def info(self):
#         print(self.brand,self.model,self.year)

# c = Car('Toyota','Corolla',2020)
# c.info()


# class Person:
#     def __init__(self,name):
#         self.name = name
#     def greet(self):
#         return "hello " + self.name
#     def welcome(self):
#         msg = self.greet()
#         print(msg, "! welcome to our website")

# p = Person("Tobias")
# p.welcome()

# class Car:
#     def __init__(self,brand):
#         self.brand = brand
#     def show(self):
#         print(self.brand)

# c1 = Car("Ford")
# c1.show()
# ------------------------------------- #
# # class properties

# class Student:
#     species = 'Human' # class property
#     def __init__(self,name,grade):
#         self.name = name # instance property
#         self.grade = grade # instance property
# s1 = Student('Anna', 'A')
# print(s1.grade) # accessing instance property
# s1.grade = 'B' # updating instance property
# print(s1.grade)
# try:
#     del s1.grade # deleting instance property
#     print(s1.grade) # will throw error
# except:
#     print("grade property deleted")
# s1.city = 'Indore'
# print(s1.city) # adding instance property
# s1.species = 'cat' # updated class property
# print(s1.species)

# ------------------------------------- #
## __str__() method

# class Person:
#     def __init__(self, name,age):
#         self.name = name
#         self.age = age
#     def __str__(self):
#         return f"{self.name} {self.age}"

# p1 = Person("Emil",20)
# print(p1)
# print(type(p1))
# print(type(p1.__str__()))


# class Rectangle:
#     def __init__(self,width,height):
#         self.width = width
#         self.height = height
#     def area(self):
#         return self.width * self.height
# r1 = Rectangle(5,3)
# print(r1.area())
# ------------------------------------- #
# encapsulation
# getter
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age # private property
    
#     def get_age(self):  # getter method
#         return self.__age

# p = Person('Drishti','22')
# print(p.name)
# # print(p.age) # will throw error
# # using getter method to get private value
# print(p.get_age())


#setter
# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.__age = age

#     def get_age(self):
#         return self.__age
#     def set_age(self,age):
#         self.__age = age

# p = Person("Drishti",22)
# print(p.get_age())
# p.set_age(19)
# print(p.get_age())

# data validation

# class BankAccount:
#     def __init__(self,bal):
#         self.__bal = bal
    
#     def deposit(self,amt):
#         self.__bal += amt
    
#     def get_bal(self):
        
#         if self.__bal <10000:
#             print("minimum balance in account must be >= 10,000")
#         else:
#             return self.__bal

    
# b = BankAccount(1000)
# print(b.get_bal())
# b.deposit(500)
# print(b.get_bal())

# b = BankAccount(10000)
# print(b.get_bal())
# b.deposit(500)
# print(b.get_bal())

# ------------------------------------- #
# access modifiers

# public

# class Greet:
#     def __init__(self,name):
#         self.name = name
    
#     def greet(self):
#         return "good morning "+ self.name

# g = Greet('drishti')
# print(g.greet())

# protected

# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self._age = age

# p = Person("Drishti", 22)
# print(p.name)
# print(p._age)

# private methods
# class Person:
#     def __init__(self,name,age):
#         self.name = name 
#         self._age = age
    
#     def __check_age(self):
#         if self._age>=18:
#             return "Adult!"
#         else:
#             return "Minor"
#     def show_status(self):
#         return self.__check_age()

# p = Person("Drishti", 22)
# print(p.name)
# print(p._age)
# print((p.show_status()))

# ------------------------------------- #
## BLIND ##

# PUBLIC

# class Person:
#     def __init__(self,name):
#         self.name = name
        
# p = Person("Alice")
# print(p.name)

# PROTECTED

# class Car:
#     def __init__(self,brand):
#         self._brand = brand
# c = Car("Toyota")
# print(c._brand) # can do this but not advised

# PRIVATE VAR

# class Dog:
#     def __init__(self,breed):
#         self.__breed = breed 
    
#     def get_breed(self): # getter method to get the private var
#         return self.__breed

# d = Dog("Husky")
# print(d.get_breed())


# PRIVATE METHOD

# class Dog:
#     def __init__(self,name,breed):
#         self.name = name
#         self.breed = breed
    
#     def __action(self):
#         return 'bark'
    
#     def get_action(self):
#         return self.__action()

# d = Dog("Jack","Labrador")
# d1 = d.get_action()
# print(d.name,"can",d1)

# class Dog:
#     def __action(self):
#         return "bark"
#     def get_action(self):
#         print( self.__action() )

# d = Dog()
# d.get_action()

# Name Mangling
# class Dog:
#     def __action(self):
#         return "bark"
    
# d = Dog()
# print(d._Dog__action()) # not recommended

# class ScoreBoard:
#     def __init__(self,score):
#         self.__score = score

#     def get_score(self):
#         return self.__score

# s1 = ScoreBoard(0)
# print(s1.get_score())

# ------------------------------------- #
## ABSTRACTION ##

# from abc import ABC, abstractmethod

# class Greet(ABC): # abstract class
#     @abstractmethod
#     def say_hello(self): # abstract method
#         pass

#     def cheer(self): # concrete method
#         return "yay"

# # needed to implement say_hello() in every child class but no need for cheer()
# class Eng(Greet): # child class 1
#     def say_hello(self): 
#         return "hello"

# class Hin(Greet): # child class 2
#     def say_hello(self):
#         return "namaste"

# class French(Greet): # child class 3
#     def say_hello(self):
#         return "bonjour"

# e = Eng()
# h = Hin()
# f = French()
# print(e.say_hello(),h.say_hello(),f.say_hello())
# print(e.cheer(),h.cheer(),f.cheer())

# class Person:
#     def __init__(self,name,salary):
#         self.name = name
#         self._salary = salary
# class Emp(Person):
#     def get_salary(self):
#         return self._salary
    
# p = Person("Linus",50000)
# e = Emp("John",6000)
# print(p.name,p._salary)# can access but shouldnt
# print(e.get_salary()) # correct approach

# ------------------------------------- #
## INHERITANCE ##

# class Person:
#     def __init__(self,fname,lname):
#         self.fname = fname
#         self.lname = lname
#     def greet(self):
#         return "hello"

# class Child(Person):
#     def __init__(self,fname,lname):
#         Person.__init__(self,fname,lname)

# p = Child("John","Doe")
# print(p.fname,p.lname) # john doe

## super ##
# class Person:
#     def __init__(self,name,rno,branch):
#         self.name = name
#         self.rno = rno
#         self.branch = branch

# class Student(Person):
#     def __init__(self,name,rno,branch,course):
#         super().__init__(name,rno,branch)
#         self.course = course

# s = Student("Drishti",101,'AIML',"CSE")
# print(s.name,s.rno,s.branch,s.course)

