# Decorators

A decorator is a function that adds extra behavior to another function without modifying the original code
A decorator:
- takes a function as an argument
- defines a wrapper function
- adds extra behavior inside that wrapper
- returns the wrapper function

## Why do we use it?

Decorators are useful when the **same additional behavior** needs to be applied to multiple functions.

Common uses include:

- Logging
- Authentication/authorization
- Timing a function
- Input validation
- Access control
- Caching
- Debugging
- Changing or processing return values

## Basic structure:

A decorator normally contains:

1. **Decorator function** → receives the original function.
2. **Wrapper/inner function** → performs additional behavior.
3. **Original function call** → executes the original function.
4. **Return wrapper** → replaces the original function with the enhanced version.

```
def decorator(func):
    def wrapper():
        # extra behavior
        return func()
    return wrapper
```

## `@decorator` Syntax

- `@decorator` is Python's **special syntax for applying a decorator** to a function.
- It is written **directly above the function definition**.

**Example**

```
def changecase(func):
    def myinner():
        return func().upper()
    return myinner

@changecase
def myfunction():
    return "Hello"

print(myfunction())
```

## Decorator Function vs Decorated Function

### 1. Decorator Function

- The **decorator function** is the function that **adds extra behavior** to another function.
- It **accepts another function as an argument**.
- It usually creates a **wrapper function** and returns it.

**Example**

```
def changecase(func):
    def myinner():
        return func().upper()
    return myinner
```

Here:

- `changecase` → **decorator function**
- `func` → the function received by the decorator
- `myinner` → wrapper function
- `return myinner` → returns the enhanced version of the function

### 2. Decorated Function

- The **decorated function** is the function **whose behavior is being changed or enhanced** by the decorator.
- It is the function written below `@decorator`.

**Example**

```
@changecase
def myfunction():
    return "Hello Sally"
```

Here:

- `myfunction` → **decorated function**
- `changecase` → **decorator**


## Wrapper Function

A **wrapper function** is a function defined inside the decorator.

Its job is to:

- Add extra behavior.
- Call the original function.
- Optionally modify its input or output.

Example

```
def changecase(func):

    def myinner():
        return func().upper()

    return myinner
```

Here:

- `changecase` → **decorator function**
- `func` → original function received by the decorator
- `myinner` → **wrapper function**
- `func()` → calls the original function
- `.upper()` → adds extra behavior
- `return myinner` → returns the wrapper function

**What Actually Happens with @changecase?**

Suppose:

```
@changecase
def myfunction():
    return "Hello Sally"
```

Python internally treats it as:

```
myfunction = changecase(myfunction)
```


## Decorators with Function Arguments

- A **decorated function can have arguments** just like any normal Python function.
- The important point is that the **wrapper function must also accept those arguments**.
- The wrapper then **passes those arguments to the original function**.

Example:

```
def logger(func):

    def wrapper(name):
        print("wrapper func called...")
        return func(name)
    return wrapper

@logger
def greet(name):
    return "hello " + name

print(greet("drishti"))
```

