# Inheritance
- allows one class to acquire properties and methods of another class.
- existing class -> Parent/Base class.
- new (inheriting) class -> Child/Derived class.
- child class can use the parent class' attributes and methods without rewriting them.
- child class can also add its own attributes and methods.
- child class can override a parent method to provide its own implementation.
- represents an ***is-a*** relationship; ex. : Dog is an Animal, Car is a Vehicle.

**Creating a Child Class**
 To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.

> [!NOTE]
> **Notes**:
> - If we add a method in the child class with the same name as a function in the parent class, the inheritance of the parent method will be overridden.
> - The child's `__init__()` function **overrides** the inheritance of the parent's `__init__()` function:
> ```
> class Person:
>     def __init__(self,fname,lname):
>         self.fname = fname
>         self.lname = lname
>     def greet(self):
>         return "hello"
> class Child(Person):
>     def __init__(self,fname,lname):
>         self.fname = lname
>         self.lname = fname
>     def greet(self):
>         return "namaste"
> > p = Child("John","Doe")
> print(p.fname,p.lname) # doe john
> print(p.greet()) # namaste
> ```
> 
> - To keep the inheritance of the parent's `__init__()` function, add a call to the parent's `__init__()` function:
> ```
> class Person:
>     def __init__(self,fname,lname):
>         self.fname = fname
>         self.lname = lname
>     def greet(self):
>         return "hello"
> 
> class Child(Person):
>     def __init__(self,fname,lname):
>         Person.__init__(self,fname,lname)
> 
> p = Child("John","Doe")
> print(p.fname,p.lname) # john doe
> ```

## super() 
used inside a child class to access the parent class' methods or constructors.

```
class Person:
    def __init__(self,name,rno,branch):
        self.name = name
        self.rno = rno
        self.branch = branch

class Student(Person):
    def __init__(self,name,rno,branch,course):
        super().__init__(name,rno,branch)
        self.course = course

s = Student("Drishti",101,'AIML',"CSE")
print(s.name,s.rno,s.branch,s.course)

```
