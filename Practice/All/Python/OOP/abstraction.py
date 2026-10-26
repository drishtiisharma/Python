'''
ABSTRACTION
===========

exposing essential behaviour while hiding implementation details

the inheriting class must implement the abstract method defined in the parent class
or else it'll throw an error by not allowing us to create the object of that inheriting class
'''

from abc import ABC,abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class sq(Shape):
    def __init__(self,side):
        self.side = side
    def area(self):
        return self.side * self.side

class cir(Shape): # must implement abstract method - area, or else will throw error when we try to create its object
    def __init__(self,radius):
        self.radius = radius


s = sq(20)
print(s.area())
# c = cir(20)  will throw error as inheriting class is not implementing the abstract methods

