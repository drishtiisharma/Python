# Run Time Polymorphism
- Polymorphic behavior is determined while the program is running.
- aka ***Dynamic Polymorphism*** or ***Late Binding***.
- commonly achieved through **==Method Overriding==**.
- actual object's type determines which implementation is executed.
- Python primarily uses it because it's dynamically typed.

Example:
```
class Person:
    def role(self):
        pass

class Student:
    def role(self):
        print("I study")

class Teacher:
    def role(self):
        print("I Teach")

s = Student()
t = Teacher()

for x in (s,t):
    x.role()
```