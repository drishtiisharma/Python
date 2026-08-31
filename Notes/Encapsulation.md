# Encapsulation
- process of protecting data inside a class.
- keeps data (attribute) and methods together inside the same class.
- controls how the data can be accessed and modified from outside the class.
- hides the internal implementation details of the class.
- main purpose is to provide data protection and controlled access.


# Need of Encapsulation
- prevents accidental and unwanted changes to the important data.
- can validate data before setting it
- we have full control on how data is accessed and modified
- internal implementation can change without affecting external code

Note : Refer to [[Access Modifiers]] before continuing further.
# Private Properties
Can make properties private by using a double underscore __ prefix.

```
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # private property
p = Person('Drishti','22')
print(p.name)
print(p.age) # will throw error
```

**Note**: Private properties cannot be accessed directly from outside the class.

**Solution?**
To access a private property, we can create a **getter** method.
```
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age # private property
    
    def get_age(self):  # getter method
        return self.__age

p = Person('Drishti','22')
print(p.name)
# print(p.age) # will throw error
# using getter method to get private value
print(p.get_age())
```

**Modifying Private Property**
To modify a private property, we can create a **setter** method.

```
class Person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def get_age(self):
        return self.__age
    def set_age(self,age):
        self.__age = age

p = Person("Drishti",22)
print(p.get_age())
p.set_age(19)
print(p.get_age())
```

# Protected Properties
