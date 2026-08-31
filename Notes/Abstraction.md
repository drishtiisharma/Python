# Abstraction
- Process of hiding unnecessary implementation details and exposing ONLY the essential functionality to the user.
- focuses on WHAT an object does rather than HOW an object does it.

# Abstract Base Class (ABC)
- python mechanism provided by the **abc** module
- allows us to create abstract classes.
- lets us define abstract methods that child classes must implement.
- prevents creating an object of the abstract class directly.
# Implementation 
## Abstract Classes
- is a class that acts as a blueprint for other classes.
- defines what methods a child class must have.
- not meant to create objects directly.
- child classes must implement its abstract methods.
- created using **ABC**.
- to instantiate an abstract class -> create a child class that inherits from it (and implements the abstract method), then create an object of the child class

## Abstract Methods
- is a method that a child class is required to implement.
- defines what a child class must do but not necessarily how to do it.
- created using **@abstractmethod** decorator.
- usually defined inside an abstract class.
- a child class that doesn't implement the abstract method cannot be instantiated.
- are method declarations without a body defined inside -> carries no implementation.
## Concrete Methods
- are fully implemented methods within an abstract class.
- child classes need not implement them just because they have inherited the method from their parent abstract class.
- if a child class of an abstract class which doesn't have any abstract method can be instantiated even without an abstract method.


```
from abc import ABC, abstractmethod

class Greet(ABC): # abstract class
    @abstractmethod
    def say_hello(self): # abstract method
        pass

    def cheer(self): # concrete method
        return "yay"

# needed to implement say_hello() in every child class but no need for cheer()
class Eng(Greet): # child class 1
    def say_hello(self): 
        return "hello"

class Hin(Greet): # child class 2
    def say_hello(self):
        return "namaste"

class French(Greet): # child class 3
    def say_hello(self):
        return "bonjour"

e = Eng()
h = Hin()
f = French()
print(e.say_hello(),h.say_hello(),f.say_hello())
print(e.cheer(),h.cheer(),f.cheer())
```
