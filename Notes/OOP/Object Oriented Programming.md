## Introduction
- Python is an object oriented programming language
- Object oriented means building computer programs using small, independent packages called objects that act like real-world things.'

## Difference between OOP and Procedural Programming


| OOP                                                                                                   | POP                                                                                           |
| ----------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------- |
| program is structured into classes and objects                                                        | program is divided into small functions                                                       |
| follows a bottom up design, which involves building individual objects first and then connecting them | follows top-down design, i.e. it starts with the main task and breaks it into smaller modules |
| data security is high                                                                                 | data security is low                                                                          |
| high code reusability                                                                                 | low code reusability                                                                          |
| scales exceptionally well                                                                             | becomes difficult to maintain and scale                                                       |
| adding new features is highly flexible                                                                | adding new data requires modifying existing functions                                         |
| Pure  OOP languages: Java, C#, Ruby, Smalltalk                                                        | Pure POP languages: C, Pascal, FORTRAN, COBOL                                                 |
Languages that support both Paradigms : Python, C++, JavaScript, PHP

## What is an Object? (generally)
- object is a single item in a computer program
- groups related information and actions together in one place
- helps organize code so it is easier to read and change
- object has two main parts:
1. Data(attributes) : what the object **has** ; ex: dog's name, color, age etc. 
2. Actions(methods) : what the object **can do** ; ex: dog can bark, run, eat, etc. 
- **Note** : almost everything in python is an object with properties and methods
## Benefits of OOP
- can reuse existing code easily
- easy to fix
- hides sensitive data and protects accidental changes
- different people can work on different parts of the code at the same time

## Problems that existed before OOP
- **Lack of data ownership** (global variable nightmare)
>  If a variable is available to the entire program, then any function can change it; sometimes the change could be correct but for the times it is wrong for, you wouldn't know which function changed it and will have to search through the whole program to find the problem.

- **Tight coupling** (rippling collapse)
>All parts of the program were so deeply intertwined that the code became terrifyingly fragile, because functions relied directly on the exact internal structure of other functions, so changing a single variable name or updating a feature would trigger a domino effect or errors. Developers were trapped in a vicious cycle where fixing one bug accidentally created five new ones, making it virtually impossible to update, upgrade or change the software once it reached a certain size.

- **Forced code duplication** (copy-paste explosion)
> If the system needed 10 slightly different types of user accounts or game enemies, developers had to copy, paste, and tweak the same code 10 separate times because there was no way to share common traits automatically. So if a bug was discovered in the shared logic, engineers had to find and fix it manually in all 10 places.


## What are Classes?
- classes defines what an object should look like.
- its a blueprint/master design/template that tells the computer how to build specific things ; more like the set of instructions and rules for making the item 
- ex: class Dog : defines that a dog has things like name, breed, age and can perform actions like bark, eat etc.

## Rules for Naming a Class
- start from a letter or underscore
- special symbols are not allowed
- no python keywords
- case sensitive

Class style guide according to Coding Standards
- PascalCase
- keep names short and descriptive (use nouns rather than verbs)
- private classes (that are meant to be accessed within the file only) may use a leading underscore ex.  (_ InternalDatabase)

## What are Objects?
- is the real item built directly from the master design/blueprint/template
- as class is used to describe the structure and behavior, object is the real thing that follows that structure
- ex : a specific dog created from Dog class, with its own name and age.

## Creating a Class and an Object
To create a class, we use the keyword ***class***
ex: creating a class MyClass, with property named x:

```
class MyClass:
	x = 5
```

Now, we use the class named MyClass to create objects by creating an object named obj and printing the value of x.
```
obj = MyClass()
print(obj.x)
```
We can delete objects by using the ***del*** keyword.
```
del obj
```


Similarly, we can create multiple objects and each object is independent and has its own copy of class properties.

**Pass in class**
class definitions cannot be empty but for some reason if our class is empty we can simply use the ***pass*** statement to avoid getting an error

___
## The `__init__ ()` method
- All the classes have a built-in method called the ___ init __ () method
- is a special method that runs automatically when we create an object
- used to assign values to the object properties or to perform actions that are necessary when the object is being created
- values can be assigned directly while the object is being created
## Self Parameter
- means - "this specific item"
- lets an object point to itself so it can use its own unique data and features
- used as a placeholder for future object's name
- tells the computer - "apply this action or data only to **ME**, the specific item currently running the code"
- this ensures that if a bank has millions of different bank account objects, depositing money into one account will only increase **MY** balance, leaving everyone else's money completely untouched.
- must be the first parameter of any method in the class
- doesnt have to be the keyword 'self'- could be any word given its the 1st parameter of the method

**Note:** While we _can_ use a different name, it is strongly recommended to use ***self*** as it is the convention in Python and makes our code more readable to others.

## Class Properties
- a variable that stores data related to a class or object
- can **access** them using dot notation ex. : obj.property
- can **modify** an object's property directly ex. : p1.age = 36
- can **delete** the object's property using del keyword ex. : del p1.age
- are defined directly inside the class, outside methods. They are generally shared by all objects unless an object has its own property with the same name.
- can **add** a new property to a specific object at any time, ex.: p1.age = 25

## Class Methods
Difference between Method and a Function

| Method                                                                 | Function                                                   |
| ---------------------------------------------------------------------- | ---------------------------------------------------------- |
| exists inside and belongs to a specific object or class                | belongs to entire program                                  |
| called using an object and dot operator; ex. : account.calculate_tax() | called directly using its name; ex. : calculate_tax()      |
| associated with OOP                                                    | associated with procedural programming                     |
| must include at least one parameter                                    | can be defined without any parameteres i.e. zero arguments |

**Note**: All methods must have **self** as their first parameter

## The `__str__()` Method
 why do we use __ str __()
 - defines the human readable representation of an object
 - mainly used when we want to print an object directly
 - for small programs p.age, p.name etc are fine but __ str __ () becomes useful when we want a standard presentation of the object that python can use whenever the object needs to be converted to text

# OOP Core Principles
- [[Encapsulation]]
- [[Abstraction]]
- [[Inheritance]]
- [[Polymorphism]]

