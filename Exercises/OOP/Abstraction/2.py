# Create an abstract Shape class with an abstract area() method and implement it for Circle and Rectangle.

from abc import ABC, abstractmethod

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Circle(Shape):

    def __init__(self,r):
        self.r = r

    def area(self):
        return 3.14* self.r * self.r

class Rectangle(Shape):

    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

c = Circle(7)
r = Rectangle(10,20)

print(c.area())
print(r.area())