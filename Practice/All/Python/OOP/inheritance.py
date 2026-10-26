'''
INHERITANCE
===========

allows one class to reuse or extend the functionality of another class

parent class : class being inherited from
child class : class that inherits from the parent class

'''

class Animal:
    def eats(self):
        print("animal eats")
    def sound(self):
        print("animal makes a sound")

class Dog(Animal):
    def bark(self):
        print("dog barks")

class Cat(Animal):
    def meow(self):
        print("cat meows")

a = Animal()
d = Dog()
c = Cat()

d.eats()
c.eats()
d.bark()
c.meow()


# method overriding
class Roles:
    def role(self):
        pass

class Employee(Roles):
    def role(self):
        print("i am an employee")

class Manager(Roles):
    def role(self):
        print("i am a manager")

e =  Employee()
m =  Manager()

for x in (e,m):
    x.role()


'''
SUPER
-----

built-in function used to access and call methods from parent(super class) inside a child class(subclass)


'''

# without super keyword
class Person:
    def __init__(self,name):
        self.name = name

class Employee(Person):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

e = Employee("Alice",6545)
print(e.name)
print(e.salary)

# with super keyword
class Person:
    def __init__(self,fname,lname):
        self.fname = fname
        self.lname = lname

class Employee(Person):
    def __init__(self,fname,lname,salary):
        super().__init__(fname,lname)
        self.salary = salary

e = Employee("Peter","Parker",6545)
print(e.fname)
print(e.lname)
print(e.salary)