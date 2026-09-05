# Tuple

A **tuple** is a collection used to store multiple items in a single variable.

### Characteristics of Tuples

- **Ordered** – Items maintain their order.
- **Indexed** – Items can be accessed using index values.
- **Immutable** – Items cannot be changed after the tuple is created.
- **Allows duplicates**.
- Uses **round brackets `()`**.
- Indexing starts from **`0`**.
- A tuple can be created **with or without parentheses**.

Example:

```python
fruits = ("apple", "banana", "orange", "apple")
```

A tuple can also be created without parentheses:

```python
fruits = "apple", "banana", "orange"
```

# Accessing Tuple Items

Tuple items are accessed using their index.

```python
fruits = ("apple", "banana", "orange")

print(fruits[0])    # apple
print(fruits[-1])   # orange
```

|Index|0|1|2|
|--:|---|---|---|
|Value|apple|banana|orange|

# Tuple Operations

|Operation|Description|Example|
|---|---|---|
|`len()`|Returns the number of items|`len(t)`|
|`index()`|Returns the index of the first occurrence|`t.index("apple")`|
|`count()`|Returns the number of occurrences|`t.count("apple")`|
|`+`|Combines two tuples|`t1 + t2`|
|`*`|Repeats a tuple|`t * 3`|
|`in`|Checks if an item exists|`"apple" in t`|
|`not in`|Checks if an item does not exist|`"apple" not in t`|
|Slicing|Extracts a portion of a tuple|`t[1:4]`|
|`del`|Deletes the entire tuple|`del t`|

## `len()`

Returns the number of items in a tuple.

```python
t = (10, 20, 30)

print(len(t))
# 3
```

## `index()`

Returns the index of the **first occurrence** of a specified value.

```python
t = (10, 20, 30, 20)

print(t.index(20))
# 1
```

## `count()`

Returns the number of times a value occurs in the tuple.

```python
t = (10, 20, 20, 30, 20)

print(t.count(20))
# 3
```

## `+` Operator

Two tuples can be combined using the `+` operator.

```python
t1 = (10, 20)
t2 = (30, 40)

t3 = t1 + t2

print(t3)
# (10, 20, 30, 40)
```

This creates a **new tuple**; the original tuples remain unchanged.

## `*` Operator

The `*` operator can be used to **repeat** a tuple.

```python
t = (10, 20)

print(t * 3)
# (10, 20, 10, 20, 10, 20)
```

## `in` and `not in`

Used to check whether an item exists in a tuple.

```python
t = (10, 20, 30)

print(20 in t)       # True
print(50 not in t)   # True
```

# Tuple Slicing

Tuples support slicing using:

```text
tuple[start:stop:step]
```

Example:

```python
t = (10, 20, 30, 40, 50)

print(t[1:4])
# (20, 30, 40)

print(t[:3])
# (10, 20, 30)

print(t[::2])
# (10, 30, 50)
```

# Changing Tuple Values

Tuples are **immutable**, so their values cannot be changed directly.

This will cause an error:

```python
t = (10, 20, 30)

t[1] = 50
# TypeError
```

If you need to change, add, or remove an item:

**Tuple → List → Modify → Tuple**

Example:

```python
t = (10, 20, 30)

l = list(t)
l[1] = 50

t = tuple(l)

print(t)
# (10, 50, 30)
```

The same approach can be used to add an item:

```python
t = (10, 20, 30)

l = list(t)
l.append(40)

t = tuple(l)

print(t)
# (10, 20, 30, 40)
```

And to remove an item:

```python
t = (10, 20, 30)

l = list(t)
l.remove(20)

t = tuple(l)

print(t)
# (10, 30)
```

# Deleting a Tuple

Although individual items cannot be removed from a tuple, the **entire tuple can be deleted** using `del`.

```python
t = (10, 20, 30)

del t
```

After this, the variable `t` no longer exists.

# Packing

**Packing** means putting multiple values into a single tuple.

```python
fruits = "apple", "banana", "orange"

print(fruits)
# ('apple', 'banana', 'orange')
```

The values are automatically packed into a tuple.

# Unpacking

**Unpacking** means taking values from a tuple and assigning them to separate variables.

```python
fruits = ("apple", "banana", "orange")

x, y, z = fruits

print(x)  # apple
print(y)  # banana
print(z)  # orange
```

The number of variables should normally match the number of elements.

# Unpacking Using `*`

The `*` operator can be used when the number of variables is less than the number of tuple elements.

The starred variable collects the remaining values into a **list**.

```python
fruits = ("apple", "banana", "orange", "mango")

x, *y = fruits

print(x)
# apple

print(y)
# ['banana', 'orange', 'mango']
```

The starred variable can also appear in the middle:

```python
fruits = ("apple", "banana", "orange", "mango")

x, *y, z = fruits

print(x)
# apple

print(y)
# ['banana', 'orange']

print(z)
# mango
```

# Tuple vs List

|Feature|List|Tuple|
|---|---|---|
|Ordered|Yes|Yes|
|Indexed|Yes|Yes|
|Mutable|Yes|No|
|Allows duplicates|Yes|Yes|
|Brackets|`[]`|`()`|
|Add items|Yes|No|
|Remove items|Yes|No|
|Change items|Yes|No|
|`index()`|Yes|Yes|
|`count()`|Yes|Yes|
|Can concatenate|Yes|Yes|
|Can repeat with `*`|Yes|Yes|

# Quick Summary

|Operation|Syntax|Purpose|
|---|---|---|
|Length|`len(t)`|Find number of items|
|Access|`t[index]`|Access an item|
|Slicing|`t[start:stop:step]`|Extract items|
|Find index|`t.index(x)`|Find first occurrence|
|Count|`t.count(x)`|Count occurrences|
|Membership|`x in t`|Check if item exists|
|Concatenate|`t1 + t2`|Combine tuples|
|Repeat|`t * n`|Repeat tuple|
|Delete|`del t`|Delete entire tuple|
|Pack|`a, b, c = values`|Pack values into tuple|
|Unpack|`a, b, c = t`|Assign tuple values to variables|
|Star unpack|`a, *b = t`|Collect remaining values into a list|
