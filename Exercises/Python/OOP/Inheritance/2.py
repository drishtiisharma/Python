# Create a Vehicle class containing common vehicle properties and inherit it into Car

class Vehicle:
    def __init__(self,brand,color):
        self.brand = brand
        self.color = color

class Car(Vehicle):
    def __init__(self,brand,color):
        super().__init__(brand,color)

c = Car('toyota','white')
print(c.brand,c.color)