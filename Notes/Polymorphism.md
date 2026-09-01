# Polymorphism
- The word "polymorphism" means "many forms".
- ability of different objects to respond to the exact same command in their own unique way.

> [!NOTE]
> **Definition:**
> Polymorphism refers to the ability of the same method or operation to behave differently based on object or context.

# Where Polymorphism Appears

## Function Polymorphism
- same function can work with different types of objects
- its behavior depends on type of object/data provided
- helps avoid creating separate functions for each type

Example:
```
def show(c):
    print(type(c),len(c))

show("helloo") # string
show([10,'a',20,30]) # list
show( # dict
    {
        'name' : 'drishti',
        'age' : 22
    }
)
show((10.20,30,450)) # tuple
```
## Class Polymorphism
- different classes have a method with the same name
- each class can implement that method differently
- same method call can therefore produce different behavior

Example:
```
class Dog:
    def sound(self):
        print("woof")
class Cat:
    def sound(self):
        print("meow")
class Duck:
    def sound(self):
        print("quack")

d = Dog()
c = Cat()
du = Duck()

for x in (d,c,du):
    x.sound()
```
## Inheritance Class Polymorphism
- parent class provides a common method
- child classes inherit that method
- child classes can override it to provide their own behavior
- same method call can behave differently for different child objects

Example:
```
class Vehicle:
    def move(self):
        pass
class Car(Vehicle):
    def move(self):
        print(("drives"))
class Ship(Vehicle):
    def move(self):
        print("sails")
class Plane((Vehicle)):
    def move(self):
        print("flies")

c= Car()
s = Ship()
p = Plane()

for x in (c,s,p):
    x.move()
```

# When Polymorphism Appears
This classification is based on when the polymorphic behavior is determines/resolved.

These include:
- [[Compile-Time]]
- [[Run-Time]]
