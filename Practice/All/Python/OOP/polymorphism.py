'''
POLYMORPHISM
============

same method name can produce diff behaviour depending on the object

'''

class Dog:
    def sound(self):
        print("woof")
class Cat:
    def sound(self):
        print("meow")

d = Dog()
c = Cat()

for x in c,d:
    x.sound()