# Dictionary

A **dictionary** is a collection used to store data in **key-value pairs**.

### Characteristics of Dictionaries

- **Ordered** – Dictionaries preserve insertion order in modern Python.
- **Mutable** – Items can be added, changed, or removed.
- **Keys must be unique** – Duplicate keys are not allowed.
- **Values can be duplicated**.
- Data is stored as **`key: value` pairs**.
- Uses **curly brackets `{}`**.
- Values are accessed using their **keys**, not indexes.

Example:

```python
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}
```

### Dictionary Structure

|Key|Value|
|---|---|
|`"name"`|`"John"`|
|`"age"`|`20`|
|`"course"`|`"Python"`|

> **Note:** Dictionaries were unordered in Python versions before 3.7. Since Python 3.7, insertion order is guaranteed.

# Dictionary Operations

|Operation|Description|Example|
|---|---|---|
|Access `[]`|Access a value using its key|`d["name"]`|
|`get()`|Access a value without raising an error if the key is missing|`d.get("name")`|
|`keys()`|Returns a view containing all keys|`d.keys()`|
|`values()`|Returns a view containing all values|`d.values()`|
|`items()`|Returns a view containing all key-value pairs|`d.items()`|
|`update()`|Updates existing keys or adds new key-value pairs|`d.update({"age": 21})`|
|`pop()`|Removes a specified key and returns its value|`d.pop("age")`|
|`popitem()`|Removes and returns the last inserted key-value pair|`d.popitem()`|
|`del`|Deletes a specified key-value pair|`del d["age"]`|
|`clear()`|Removes all items; dictionary remains|`d.clear()`|
|`copy()`|Creates a copy of the dictionary|`new = d.copy()`|

## Accessing Dictionary Values

Values can be accessed by referring to their key.

```python
student = {
    "name": "John",
    "age": 20
}

print(student["name"])
# John
```

If the specified key does not exist, using `[]` raises a `KeyError`.

```python
print(student["email"])
# KeyError
```

## `get()`

The `get()` method can also be used to access values.

```python
print(student.get("name"))
# John
```

If the key does not exist, `get()` returns `None` by default instead of raising an error.

```python
print(student.get("email"))
# None
```

A default value can also be provided:

```python
print(student.get("email", "Not Available"))
# Not Available
```

### `[]` vs `get()`

|`d["key"]`|`d.get("key")`|
|---|---|
|Accesses the value|Accesses the value|
|Raises `KeyError` if key doesn't exist|Returns `None` if key doesn't exist|
|Can be used to access and assign values|Mainly used for safe access|

# `keys()`

Returns a **view containing all keys** in the dictionary.

```python
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

print(student.keys())
```

You can convert it to a list:

```python
print(list(student.keys()))
# ['name', 'age', 'course']
```

# `values()`

Returns a **view containing all values** in the dictionary.

```python
print(student.values())
```

Convert it to a list:

```python
print(list(student.values()))
# ['John', 20, 'Python']
```

# `items()`

Returns a **view containing all key-value pairs** as tuples.

```python
print(student.items())
```

Convert it to a list:

```python
print(list(student.items()))
# [('name', 'John'), ('age', 20), ('course', 'Python')]
```

It is commonly used with loops:

```python
for key, value in student.items():
    print(key, value)
```

# `update()`

The `update()` method can:

- Update an existing key's value.
- Add a new key-value pair.

### Updating an Existing Key

```python
student = {
    "name": "John",
    "age": 20
}

student.update({"age": 21})

print(student)
# {'name': 'John', 'age': 21}
```

### Adding a New Key

```python
student.update({"course": "Python"})

print(student)
# {'name': 'John', 'age': 21, 'course': 'Python'}
```

# `pop()`

Removes a specified key and **returns its value**.

```python
student = {
    "name": "John",
    "age": 20
}

age = student.pop("age")

print(age)
# 20

print(student)
# {'name': 'John'}
```

If the key does not exist, `pop()` raises a `KeyError` unless a default value is provided.

```python
student.pop("email", "Not Found")
# Not Found
```

# `popitem()`

Removes and returns the **last inserted key-value pair**.

```python
student = {
    "name": "John",
    "age": 20,
    "course": "Python"
}

item = student.popitem()

print(item)
# ('course', 'Python')
```

# `del`

The `del` statement removes a specified key-value pair.

```python
student = {
    "name": "John",
    "age": 20
}

del student["age"]

print(student)
# {'name': 'John'}
```

Unlike `pop()`, `del` does **not return the removed value**.

### `pop()` vs `del`

|`pop()`|`del`|
|---|---|
|Removes a specified key|Removes a specified key|
|Returns the removed value|Does not return the removed value|
|`value = d.pop("key")`|`del d["key"]`|
|Can provide a default value|No default value option|

# `clear()`

Removes all items from the dictionary, but the dictionary itself remains.

```python
student = {
    "name": "John",
    "age": 20
}

student.clear()

print(student)
# {}
```

# `copy()`

Creates a copy of the dictionary.

```python
student = {
    "name": "John",
    "age": 20
}

new_student = student.copy()

print(new_student)
# {'name': 'John', 'age': 20}
```

Another way to create a copy:

```python
new_student = dict(student)
```

# Adding Items

A new key-value pair can be added directly using a key.

```python
student = {
    "name": "John"
}

student["age"] = 20

print(student)
# {'name': 'John', 'age': 20}
```

# Changing Values

Existing values can also be changed using their keys.

```python
student = {
    "name": "John",
    "age": 20
}

student["age"] = 21

print(student)
# {'name': 'John', 'age': 21}
```

# Quick Summary

|Operation|Syntax|Purpose|
|---|---|---|
|Access|`d["key"]`|Access value using key|
|Safe access|`d.get("key")`|Access value without `KeyError`|
|Get keys|`d.keys()`|Get all keys|
|Get values|`d.values()`|Get all values|
|Get pairs|`d.items()`|Get all key-value pairs|
|Update|`d.update({...})`|Update or add key-value pairs|
|Add|`d["key"] = value`|Add a new key-value pair|
|Change|`d["key"] = new_value`|Change an existing value|
|Remove|`d.pop("key")`|Remove key and return its value|
|Remove last|`d.popitem()`|Remove last inserted pair|
|Delete|`del d["key"]`|Delete specified key|
|Empty|`d.clear()`|Remove all items|
|Copy|`d.copy()`|Create a copy|
