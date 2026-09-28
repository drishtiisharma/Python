# Create a class using a protected attribute and demonstrate how it can be accessed by a child class.
class Parent:
    def __init__(self,name,age):
        self.name = name
        self._age = age

class Child(Parent):
    def __init__(self,name,age):
        super().__init__(name,age)
        print(self._age)

c = Child('drishti',20)
p = Parent("khushi",19)
print(p._age) # can do this but shouldn't do
print(c._age) # can do this but shouldn't do
