# Inner Classes
- class defined inside another class.
- outer class containing 1 or more inner classes.
- useful for grouping related/helper classes.
- improve code organization when class is only relevant to an outer class.
- inner classes **do not** automatically access the outer class instance.

Example:
```
class Outer:
    def show(self):
        print('outer')
    
    class Inner:
        def display(self):
            print('inner')

o = Outer()
i = o.Inner()
o.show()
i.display()
```
## Accessing Inner Class from Outside
- create object of outer class first.
- use that object to access the inner class.
- then, create an object of the inner class.

Example:
```
class Outer:
    class Inner:
        def display(self):
            print(("yo"))
o = Outer()
i = o.Inner()
i.display()
```
## Accessing Outer Class from Inner Class
- inner class does not automatically get access to the outer object's `self`.
- to access outer-class attribute/methods:
1. pass the outer object to the inner class.
2. store it inside the inner class.
3. use that reference to access the outer class.

Example:
```
class Outer:
    def __init__(self):
        self.name = 'drishti'

    class Inner:
        def __init__(self,outer):
            self.outer = outer
        def display(self):
            print(self.outer.name)

o = Outer()
i = o.Inner(o)
i.display()
```
# Multiple Inner Classes
- an outer class with multiple inner classes.
- each inner class can represent a different component or responsibility.
- outer class can create and use objects of these inner classes.

Example:
```
class Outer:
    def __init__(self):
        self.name = 'drishti'

    class Inner:
        def __init__(self,outer):
            self.outer = outer
        def display(self):
            print(self.outer.name)

o = Outer()
i = o.Inner(o)
i.display()
```
