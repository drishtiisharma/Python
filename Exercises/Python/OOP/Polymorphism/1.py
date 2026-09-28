# Create different animal classes where each has a sound() method behaving differently.

class Animal():
    def sound(self):
        print("animal makes sound")

class Dog(Animal):
    def sound(self):
        print("woof")

class Cat(Animal):
    def sound(self):
        print("meow")

a = Animal()
d = Dog()
c = Cat()

a.sound()
d.sound()
c.sound()