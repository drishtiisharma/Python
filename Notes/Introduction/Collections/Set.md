# Sets

A **set** is a collection used to store multiple **unique values**.

### Characteristics of Sets

- **Unordered** – Items do not have a fixed order.
- **Unindexed** – Items cannot be accessed using index values.
- **Mutable** – Items can be added or removed.
- **Duplicates are not allowed**.
- Uses **curly brackets `{}`**.
- Values can be added and removed, but individual elements cannot be changed directly.
- A set cannot contain duplicate values.
- `True` is treated as `1` and `False` is treated as `0` in sets.

Example:

```python
s = {10, 20, 30, 20}

print(s)
# {10, 20, 30}
```

### `True`, `1`, `False`, and `0` in Sets

`True` and `1` are considered equal, and `False` and `0` are considered equal.

```python
s = {True, 1, False, 0, 10}

print(s)
# {False, True, 10}
```

Only one value from each equivalent pair is retained.

### Accessing Set Items

Since sets are unordered and unindexed, items cannot be accessed using indexes.

```python
s = {10, 20, 30}

# s[0]  # TypeError
```

You can check for a value using `in` or `not in`:

```python
print(20 in s)       # True
print(50 not in s)   # True
```

You can also use a loop:

```python
for x in s:
    print(x)
```

# Set Operations

|Operation|Description|Example|
|---|---|---|
|`add()`|Adds one item to the set|`s.add(40)`|
|`update()`|Adds multiple items from another iterable|`s.update({40, 50})`|
|`remove()`|Removes a specified item; raises error if not found|`s.remove(20)`|
|`discard()`|Removes a specified item; no error if not found|`s.discard(20)`|
|`pop()`|Removes and returns an arbitrary item|`s.pop()`|
|`clear()`|Removes all items; set remains|`s.clear()`|
|`del`|Deletes the entire set|`del s`|

## `add()`

Adds a single item to the set.

```python
s = {10, 20, 30}

s.add(40)

print(s)
# {10, 20, 30, 40}
```

> Since sets are unordered, you should not rely on where the new item appears when printed.

## `update()`

Adds multiple items from another set or iterable.

```python
s = {10, 20}

s.update({30, 40})

print(s)
# {10, 20, 30, 40}
```

It can also accept other iterables:

```python
s.update([50, 60])
s.update((70, 80))
```

## `remove()`

Removes a specified item.

```python
s = {10, 20, 30}

s.remove(20)

print(s)
# {10, 30}
```

If the item does not exist, `remove()` raises a `KeyError`.

## `discard()`

Removes a specified item.

```python
s = {10, 20, 30}

s.discard(20)

print(s)
# {10, 30}
```

Unlike `remove()`, `discard()` does **not** raise an error if the item does not exist.

### `remove()` vs `discard()`

|`remove()`|`discard()`|
|---|---|
|Removes specified item|Removes specified item|
|Raises `KeyError` if item doesn't exist|Does not raise an error|
|`s.remove(50)` → Error|`s.discard(50)` → No error|

## `pop()`

Removes and returns an **arbitrary item** from the set.

Because sets are unordered, we cannot predict which item will be removed.

```python
s = {10, 20, 30}

x = s.pop()

print(x)
print(s)
```

## `clear()`

Removes all items from the set, but the set itself remains.

```python
s = {10, 20, 30}

s.clear()

print(s)
# set()
```

## `del`

Deletes the entire set.

```python
s = {10, 20, 30}

del s
```

After `del s`, the variable `s` no longer exists.

# Joining / Combining Sets

Python provides several operations for combining or comparing sets.

Consider:

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

|Operation|Method|Operator|Result|
|---|---|---|---|
|Union|`A.union(B)`|`A \| B`|`{1, 2, 3, 4, 5, 6}`|
|Intersection|`A.intersection(B)`|`A & B`|`{3, 4}`|
|Difference|`A.difference(B)`|`A - B`|`{1, 2}`|
|Symmetric Difference|`A.symmetric_difference(B)`|`A ^ B`|`{1, 2, 5, 6}`|

## Union — `union()` / `|`

Combines the elements of both sets and returns a **new set**.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.union(B)

print(C)
# {1, 2, 3, 4, 5, 6}
```

The original sets remain unchanged.

The `|` operator can also be used:

```python
C = A | B
```

## `update()`

Adds elements from another set to the **original set**.

```python
A = {1, 2, 3}
B = {3, 4, 5}

A.update(B)

print(A)
# {1, 2, 3, 4, 5}
```

Only `A` is modified.

> `union()` returns a new set, while `update()` modifies the existing set.

## Intersection — `intersection()` / `&`

Returns only the elements that are **common to both sets**.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.intersection(B)

print(C)
# {3, 4}
```

Using `&`:

```python
C = A & B
```

The original sets remain unchanged.

## `intersection_update()`

Keeps only the common elements in the **original set**.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.intersection_update(B)

print(A)
# {3, 4}
```

Only `A` is modified.

## Difference — `difference()` / `-`

Returns a **new set** containing elements that are in the first set but not in the second set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.difference(B)

print(C)
# {1, 2}
```

Using `-`:

```python
C = A - B
```

The original sets remain unchanged.

## `difference_update()`

Removes elements from the original set that are also present in the other set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.difference_update(B)

print(A)
# {1, 2}
```

Only `A` is modified.

## Symmetric Difference — `symmetric_difference()` / `^`

Returns a **new set** containing elements that are unique to either set.

In other words, common elements are excluded.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A.symmetric_difference(B)

print(C)
# {1, 2, 5, 6}
```

Using `^`:

```python
C = A ^ B
```

The original sets remain unchanged.

## `symmetric_difference_update()`

Updates the original set so that it contains only the elements that are unique to either set.

```python
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

A.symmetric_difference_update(B)

print(A)
# {1, 2, 5, 6}
```

Only `A` is modified.

# Set Operations: Quick Comparison

|Operation|Meaning|New Set|Original Set Modified|Operator|
|---|---|:-:|:-:|---|
|`union()`|All elements from both sets|Yes|No|`\|`|
|`update()`|Add elements of another set|No|Yes|—|
|`intersection()`|Common elements|Yes|No|`&`|
|`intersection_update()`|Keep common elements|No|Yes|—|
|`difference()`|Elements only in first set|Yes|No|`-`|
|`difference_update()`|Keep elements only in first set|No|Yes|—|
|`symmetric_difference()`|Unique elements from both sets|Yes|No|`^`|
|`symmetric_difference_update()`|Keep unique elements from both sets|No|Yes|—|

# Frozenset

A **frozenset** is an **immutable version of a set**.

### Characteristics of Frozensets

- **Unordered**
- **Unindexed**
- **Immutable / unchangeable**
- Does not allow duplicate values
- Cannot add or remove items
- Supports set operations such as union, intersection, difference, and symmetric difference
- Can be used where an immutable set is required
- A frozenset can be copied to create another frozenset

Example:

```python
s = frozenset([10, 20, 30])

print(s)
# frozenset({10, 20, 30})
```

The following operations are not available for frozensets:

```python
s.add(40)       # Error
s.remove(20)    # Error
s.clear()       # Error
```

However, set operations can be performed:

```python
A = frozenset({1, 2, 3})
B = frozenset({3, 4, 5})

print(A | B)
# frozenset({1, 2, 3, 4, 5})

print(A & B)
# frozenset({3})

print(A - B)
# frozenset({1, 2})

print(A ^ B)
# frozenset({1, 2, 4, 5})
```

# Set vs Frozenset

|Feature|Set|Frozenset|
|---|---|---|
|Ordered|No|No|
|Indexed|No|No|
|Mutable|Yes|No|
|Add items|Yes|No|
|Remove items|Yes|No|
|Duplicates|Not allowed|Not allowed|
|Set operations|Yes|Yes|
|Example|`{1, 2, 3}`|`frozenset({1, 2, 3})`|

# Quick Summary

|Operation|Syntax|Purpose|
|---|---|---|
|Add|`s.add(x)`|Add one item|
|Update|`s.update(iterable)`|Add multiple items|
|Remove|`s.remove(x)`|Remove item; error if absent|
|Discard|`s.discard(x)`|Remove item; no error if absent|
|Pop|`s.pop()`|Remove arbitrary item|
|Clear|`s.clear()`|Remove all items|
|Delete|`del s`|Delete entire set|
|Union|`A \| B`|All unique elements|
|Intersection|`A & B`|Common elements|
|Difference|`A - B`|Elements only in first set|
|Symmetric Difference|`A ^ B`|Elements unique to either set|