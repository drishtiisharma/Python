# Data Types

## What are Data Types?

A **data type** defines the type of value that a variable can store. Python has several built-in data types used to represent different kinds of data.

### Core Data Types

The **4 core data types** are:

|No.|Data Type|Example|
|--:|---|---|
|1|`int`|`10`|
|2|`float`|`10.5`|
|3|`str`|`"Python"`|
|4|`bool`|`True` / `False`|

Python has **12 built-in data types**, which can be grouped as follows:

|Category|Data Types|
|---|---|
|Numeric|`int`, `float`, `complex`|
|Sequence|`str`, `list`, `tuple`, `range`|
|Mapping|`dict`|
|Set|`set`, `frozenset`|
|Boolean|`bool`|
|None|`NoneType`|
# 1. Numeric Data Types

Numeric data types are used to store numbers.

|Data Type|Description|Example|
|---|---|---|
|`int`|Whole numbers without decimal points|`10`, `-5`, `100`|
|`float`|Numbers containing decimal points|`10.5`, `3.14`|
|`complex`|Numbers containing real and imaginary parts|`3 + 4j`|

Example:

```python
a = 10          # int
b = 10.5        # float
c = 3 + 4j      # complex
```

# 2. Sequence Data Types

Sequence data types store multiple values in an ordered collection.

|Data Type|Description|Example|
|---|---|---|
|`str`|Sequence of characters|`"Python"`|
|`list`|Ordered, mutable collection|`[10, 20, 30]`|
|`tuple`|Ordered, immutable collection|`(10, 20, 30)`|
|`range`|Sequence of numbers, commonly used in loops|`range(5)`|

### Comparison of Sequence Types

|Feature|`str`|`list`|`tuple`|`range`|
|---|---|---|---|---|
|Ordered|Yes|Yes|Yes|Yes|
|Mutable|No|Yes|No|No|
|Allows duplicates|Yes|Yes|Yes|Yes|
|Example|`"abc"`|`[1, 2, 3]`|`(1, 2, 3)`|`range(3)`|

# 3. Mapping Data Type

Python has one built-in mapping data type: **`dict` (dictionary)**.

A dictionary stores data in **key-value pairs**.

Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
```

|Feature|`dict`|
|---|---|
|Stores data as|Key-value pairs|
|Ordered|Yes|
|Mutable|Yes|
|Keys|Must be unique|
|Values|Can be duplicated|

> **Note:** Dictionaries were considered unordered in older versions of Python. Since **Python 3.7**, dictionaries preserve insertion order as a language guarantee.

# 4. Set Data Types

Set types are used to store **unique values**.

Python has two set data types:

- `set`
    
- `frozenset`

|Feature|`set`|`frozenset`|
|---|---|---|
|Ordered|No|No|
|Mutable|Yes|No|
|Allows duplicates|No|No|
|Can be modified|Yes|No|
|Example|`{1, 2, 3}`|`frozenset({1, 2, 3})`|

Example:

```python
numbers = {1, 2, 2, 3}

print(numbers)
# {1, 2, 3}
```

The duplicate value `2` is automatically removed.

# 5. Boolean Data Type

The Boolean data type is represented by **`bool`**.

It has only two possible values:

- `True`
    
- `False`


Example:

```python
is_python = True
is_java = False
```

### `bool()` Function

The `bool()` function evaluates a value and returns either `True` or `False`.

|Value|`bool(value)`|
|---|---|
|`True`|`True`|
|`False`|`False`|
|`1`|`True`|
|`0`|`False`|
|`"Python"`|`True`|
|`""`|`False`|
|`[1, 2]`|`True`|
|`[]`|`False`|
|`None`|`False`|

Example:

```python
print(bool(10))       # True
print(bool(0))        # False
print(bool("Hello"))  # True
print(bool(""))       # False
```

# 6. None Type

Python has a special data type called **`NoneType`**.

Its only value is:

```python
None
```

`None` represents the **absence of a value** or a value that has not been assigned.

Example:

```python
result = None

print(result)
# None
```

The type of `None` is `NoneType`:

```python
print(type(None))
# <class 'NoneType'>
```


# Total Built-in Data Types

Python has **12 commonly listed built-in data types**:

| No. | Category | Data Type |
|---:|---|---|
| 1 | **Numeric** | `int` |
| 2 | | `float` |
| 3 | | `complex` |
| 4 | **Sequence** | `str` |
| 5 | | `list` |
| 6 | | `tuple` |
| 7 | | `range` |
| 8 | **Mapping** | `dict` |
| 9 | **Set** | `set` |
| 10 | | `frozenset` |
| 11 | **Boolean** | `bool` |
| 12 | **None** | `NoneType` |

# Primitive and Derived Data Types

Python is an **object-oriented language**. It uses classes to define its data types, including its basic or primitive types.

### Primitive Data Types

The commonly considered primitive/basic data types are:

|Data Type|Example|
|---|---|
|`int`|`10`|
|`float`|`10.5`|
|`complex`|`2 + 3j`|
|`bool`|`True`|
|`str`|`"Hello"`|
|`NoneType`|`None`|

### Derived Data Types

Derived/collection data types include:

|Data Type|Example|
|---|---|
|`list`|`[1, 2, 3]`|
|`tuple`|`(1, 2, 3)`|
|`set`|`{1, 2, 3}`|
|`frozenset`|`frozenset({1, 2, 3})`|
|`dict`|`{"a": 1, "b": 2}`|
# Type Conversion

**Type conversion** means converting a value from one data type to another.

Python provides built-in functions such as:

|Function|Converts To|Example|
|---|---|---|
|`int()`|Integer|`int("10")` → `10`|
|`float()`|Float|`float("10.5")` → `10.5`|
|`complex()`|Complex number|`complex(5)` → `(5+0j)`|
|`str()`|String|`str(10)` → `"10"`|
|`bool()`|Boolean|`bool(1)` → `True`|

Example:

```python
x = "10"

a = int(x)
b = float(x)
c = complex(x)

print(a)  # 10
print(b)  # 10.0
print(c)  # (10+0j)
```

> **Note:** Not every value can be converted successfully into every data type. For example, `int("hello")` raises a `ValueError`.

# Checking the Data Type

Python provides the built-in **`type()`** function to determine the data type of a value.

Example:

```python
x = 10
y = 10.5
z = "Python"

print(type(x))  # <class 'int'>
print(type(y))  # <class 'float'>
print(type(z))  # <class 'str'>
```

# Random Numbers

Python has a built-in module called **`random`** that can be used to generate random values.

Example:

```python
import random

number = random.randint(1, 10)

print(number)
```

`randint(1, 10)` generates a random integer between **1 and 10**, inclusive.

# Quick Summary

|Category|Data Types|
|---|---|
|**Core**|`int`, `float`, `str`, `bool`|
|**Numeric**|`int`, `float`, `complex`|
|**Sequence**|`str`, `list`, `tuple`, `range`|
|**Mapping**|`dict`|
|**Set**|`set`, `frozenset`|
|**Boolean**|`bool`|
|**None**|`NoneType`|
|**Primitive/Basic**|`int`, `float`, `complex`, `bool`, `str`, `NoneType`|
|**Derived/Collection**|`list`, `tuple`, `set`, `frozenset`, `dict`|
