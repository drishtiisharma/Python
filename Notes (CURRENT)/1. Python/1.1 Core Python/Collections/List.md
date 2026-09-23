# List

A **list** is a collection used to store multiple items in a single variable.

### Characteristics of Lists

- **Ordered** – Items maintain their order.
- **Mutable** – Items can be changed after the list is created.
- **Allows duplicates** – The same value can appear multiple times.
- Uses **square brackets `[]`**.
- Items are accessed using **index values**.
- Indexing starts from **`0`**.

Example:

```python
fruits = ["apple", "banana", "orange", "apple"]
```

|Index|0|1|2|3|
|--:|---|---|---|---|
|Value|apple|banana|orange|apple|

```python
print(fruits[0])    # apple
print(fruits[-1])   # apple
```

# List Functions and Operations

|Function / Operation|Description|Example|
|---|---|---|
|`len()`|Returns the number of items in the list|`len(l)`|
|`append()`|Adds an item to the end of the list|`l.append("apple")`|
|`extend()`|Adds multiple items from another iterable|`l.extend([4, 5])`|
|`insert()`|Inserts an item at a specified index|`l.insert(2, "apple")`|
|`remove()`|Removes the first occurrence of a specified value|`l.remove("apple")`|
|`pop()`|Removes and returns the last item|`l.pop()`|
|`pop(x)`|Removes and returns the item at index `x`|`l.pop(2)`|
|`del l[x]`|Deletes the item at index `x`|`del l[2]`|
|`clear()`|Removes all items; the list remains|`l.clear()`|
|`index()`|Returns the index of the first occurrence of a value|`l.index("apple")`|
|`count()`|Returns the number of occurrences of a value|`l.count("apple")`|
|`reverse()`|Reverses the current order of the list|`l.reverse()`|
|`copy()`|Creates a copy of the list|`new = l.copy()`|
|`sort()`|Sorts the list in ascending order by default|`l.sort()`|

## `len()`

Returns the number of items in a list.

```python
l = [10, 20, 30]

print(len(l))
# 3
```

## `append()`

Adds **one item** to the end of the list.

```python
l = [10, 20, 30]

l.append(40)

print(l)
# [10, 20, 30, 40]
```

## `extend()`

Adds multiple items from another iterable to the end of the list.

```python
l = [10, 20]

l.extend([30, 40])

print(l)
# [10, 20, 30, 40]
```

It can also be done using `+`:

```python
l = [10, 20]
l = l + [30, 40]
```

### `append()` vs `extend()`

|`append()`|`extend()`|
|---|---|
|Adds one item|Adds multiple items|
|`l.append([30, 40])`|`l.extend([30, 40])`|
|`[10, 20, [30, 40]]`|`[10, 20, 30, 40]`|

## `insert()`

Inserts an item at a specified index.

```python
l = [10, 20, 30]

l.insert(2, "apple")

print(l)
# [10, 20, "apple", 30]
```

## `remove()`

Removes the **first occurrence** of a specified value.

```python
l = [10, 20, 30, 20]

l.remove(20)

print(l)
# [10, 30, 20]
```

If the value does not exist, `remove()` raises a `ValueError`.

## `pop()`

Removes and returns an item from the list.

Without an index, it removes the **last item**:

```python
l = [10, 20, 30]

x = l.pop()

print(x)  # 30
print(l)  # [10, 20]
```

With an index, `pop(x)` removes and returns the item at that index:

```python
l = [10, 20, 30]

x = l.pop(1)

print(x)  # 20
print(l)  # [10, 30]
```

## `del l[x]`

Deletes an item at a specified index.

```python
l = [10, 20, 30]

del l[1]

print(l)
# [10, 30]
```

Unlike `pop()`, `del` does not return the removed item.

## `clear()`

Removes all items from the list, but the list itself remains.

```python
l = [10, 20, 30]

l.clear()

print(l)
# []
```

## `index()`

Returns the index of the **first occurrence** of a specified value.

```python
l = [10, 20, 30, 20]

print(l.index(20))
# 1
```

## `count()`

Returns the number of times a specified value occurs in the list.

```python
l = [10, 20, 20, 30, 20]

print(l.count(20))
# 3
```

## `reverse()`

Reverses the current order of the list.

It does **not** sort the list.

```python
l = [30, 10, 20]

l.reverse()

print(l)
# [20, 10, 30]
```

## `copy()`

Creates a copy of the list.

```python
l = [10, 20, 30]

new_l = l.copy()

print(new_l)
# [10, 20, 30]
```

Other ways to copy a list:

```python
new_l = list(l)
```

```python
new_l = l[:]
```

## `sort()`

Sorts the list in **ascending order** by default.

```python
l = [30, 10, 20]

l.sort()

print(l)
# [10, 20, 30]
```

For descending order, use `reverse=True`:

```python
l.sort(reverse=True)

print(l)
# [30, 20, 10]
```

By default, uppercase letters are sorted before lowercase letters.

For case-insensitive sorting, use `key=str.lower`:

```python
l = ["banana", "Apple", "cherry"]

l.sort(key=str.lower)

print(l)
# ['Apple', 'banana', 'cherry']
```

# List Comprehension

**List comprehension** is a concise way to create a list, often by looping through another iterable.

Example:

```python
numbers = [1, 2, 3, 4, 5]

squares = [x * x for x in numbers]

print(squares)
# [1, 4, 9, 16, 25]
```

It can also include a condition:

```python
even = [x for x in numbers if x % 2 == 0]

print(even)
# [2, 4]
```

# Quick Summary

|Operation|Syntax|Purpose|
|---|---|---|
|Length|`len(l)`|Find number of items|
|Add one item|`l.append(x)`|Add item at the end|
|Add multiple items|`l.extend(iterable)`|Add multiple items|
|Insert|`l.insert(i, x)`|Add item at a specific index|
|Remove value|`l.remove(x)`|Remove first matching value|
|Remove last|`l.pop()`|Remove and return last item|
|Remove by index|`l.pop(x)`|Remove and return item at index|
|Delete by index|`del l[x]`|Delete item at index|
|Empty list|`l.clear()`|Remove all items|
|Find index|`l.index(x)`|Find first occurrence|
|Count|`l.count(x)`|Count occurrences|
|Reverse|`l.reverse()`|Reverse current order|
|Copy|`l.copy()`|Create a copy|
|Sort|`l.sort()`|Sort the list|
|List comprehension|`[x for x in l]`|Concisely create a list|