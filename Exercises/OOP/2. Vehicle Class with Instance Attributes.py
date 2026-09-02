# Problem Statement: Write a Python program to create a Vehicle class with two instance attributes: max_speed and mileage. Create an object of the class and print both attributes.


class Vehicle:
    def __init__(self,max_speed,mileage):
        self.max_speed = max_speed
        self.mileage = mileage

v = Vehicle(120,20)
print(v.max_speed,v.mileage)