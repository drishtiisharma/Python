**Access modifier**s in Python control which parts of a class can be accessed from **outside the class**, from **within the class**, or **by subclasses**. They help control how data and methods are accessed and used.
# Types of Access Modifiers
### Public Properties
-  Members (variables or methods) declared as public can be accessed from anywhere in the program.
- By default, all members are public in Python.

```
class Person:
    def __init__(self,name):
        self.name = name
        
p = Person("Alice")
print(p.name)
```

### Protected Properties
- A member is considered protected if its name starts with a single underscore (_).
- Convention only: It suggests that the member should not be accessed outside the class except by subclasses.
- Still, Python allows direct access if explicitly called.

```
class Car:
    def __init__(self,brand):
        self._brand = brand
c = Car("Toyota")
print(c._brand) # can do this but not advised

```
### Private Properties
- A method starting with __ is considered private.
- It is mainly intended to be used inside the class.
- It cannot normally be called from outside using its original name.
- Other methods of the same class can call it normally.
- Private methods are useful for internal/helper logic that users of the class don't need to call.
#### Private Variable
- cannot be accessed outside the class
- need a getter method to access a private variable

```
class Dog:
    def __init__(self,breed):
        self.__breed = breed 
    
    def get_breed(self): # getter method to get the private var
        return self.__breed

d = Dog("Husky")
print(d.get_breed())
```

#### Private Method
- starts with double underscore __ in the classname and is intended to be used only inside the class
- usually called by other methods within the class to handle the internal logic

```
class Dog:
    def __action(self):
        return "bark"
    def get_action(self):
        print( self.__action() )

d = Dog()
d.get_action()
```

Here, Python automatically applies the **Name Mangling** to it behind the scenes.
That is, internally Python changes: __ action to _ Dog __ action (We don't need to write this ourselves). It does so to avoid the accidental name conflicts with subclasses or other attributes/methods.

**Note**: Name Mangling happens to both variables and methods

```
class Dog:
    def __action(self):
        return "bark"
    
d = Dog()
print(d._Dog__action()) # NOT recommended -> as is an internal implementation detail, not meant to be used like this
```

