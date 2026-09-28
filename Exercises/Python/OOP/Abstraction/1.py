# Create an abstract Vehicle class with an abstract start() method and implement it in Car and Bike.

from abc import ABC, abstractmethod
class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("car")

class Bike(Vehicle):
    def start(self):
        print("bike")

b = Bike()
c = Car()
b.start()
c.start()

