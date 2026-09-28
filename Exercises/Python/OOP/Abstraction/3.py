# Create an abstract Animal class requiring every animal to implement a sound() method.

from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    
    def sound(self):
        print("woof")

class Cat(Animal):

    def sound(self):
        print("meow")

c = Cat()
d = Dog()

c.sound()
d.sound()