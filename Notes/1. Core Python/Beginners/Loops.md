# Loops

**Loops** are used to repeatedly execute a block of code until a condition is met or a sequence has been completely iterated over.

Python mainly provides two types of loops:

| Loop    | Purpose                                                   |
| ------- | --------------------------------------------------------- |
| `while` | Executes a block of code as long as a condition is `True` |
| `for`   | Iterates over the items of a sequence or other iterable   |

# `while` Loop

A `while` loop executes a block of code **as long as the given condition is `True`**.

### Syntax

```python
while condition:
    # code to execute
```

Example:

```python
i = 1

while i <= 5:
    print(i)
    i += 1
```

Output:

```text
1
2
3
4
5
```

Here, `i += 1` is important because it changes the value of `i` and eventually makes the condition `i <= 5` become `False`.

### Infinite `while` Loop

If the condition never becomes `False`, the loop will continue forever.

```python
i = 1

while i <= 5:
    print(i)
```

Here, `i` is never increased, so `i <= 5` always remains `True`.

> **Important:** Always make sure that something inside a `while` loop eventually makes its condition `False`, unless an infinite loop is intentional.

# `for` Loop

A `for` loop is used to **iterate over a sequence or iterable**, such as:

- List
- Tuple
- Set
- Dictionary
- String
- Range
### Syntax

```python
for variable in sequence:
    # code to execute
```

Example with a list:

```python
fruits = ["apple", "banana", "orange"]

for fruit in fruits:
    print(fruit)
```

Output:

```text
apple
banana
orange
```

Example with a string:

```python
for character in "Python":
    print(character)
```

Output:

```text
P
y
t
h
o
n
```

# `range()` Function

The `range()` function is commonly used with `for` loops to execute a block of code a specified number of times.

### Syntax

```text
range(start, stop, step)
```

|Parameter|Required?|Description|
|---|---|---|
|`start`|Optional|Starting value; defaults to `0`|
|`stop`|**Required**|Ending value; not included|
|`step`|Optional|Increment/decrement; defaults to `1`|

## `range(stop)`

Only the ending value is specified.

```python
for i in range(5):
    print(i)
```

Output:

```text
0
1
2
3
4
```

The `stop` value `5` is **not included**.

## `range(start, stop)`

Both starting and ending values are specified.

```python
for i in range(2, 6):
    print(i)
```

Output:

```text
2
3
4
5
```

## `range(start, stop, step)`

A third value can be used to specify the increment.

```python
for i in range(1, 10, 2):
    print(i)
```

Output:

```text
1
3
5
7
9
```

The `step` can also be negative:

```python
for i in range(5, 0, -1):
    print(i)
```

Output:

```text
5
4
3
2
1
```

# `else` with Loops

Python allows an `else` block to be used with both `for` and `while` loops.

The `else` block executes **once when the loop finishes normally**.

If the loop is terminated using `break`, the `else` block is **not executed**.

## `else` with `for`

```python
for i in range(5):
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
3
4
Loop completed
```

## `else` with `while`

```python
i = 1

while i <= 3:
    print(i)
    i += 1
else:
    print("Loop completed")
```

Output:

```text
1
2
3
Loop completed
```

## `else` with `break`

If `break` terminates the loop, the `else` block does not execute.

```python
for i in range(5):
    if i == 3:
        break
    print(i)
else:
    print("Loop completed")
```

Output:

```text
0
1
2
```

The `else` block is skipped because the loop was terminated by `break`.

# Loop Control Statements

Python provides three important loop control statements:

|Statement|Purpose|
|---|---|
|`break`|Terminates the entire loop|
|`continue`|Skips the current iteration and continues with the next iteration|
|`pass`|Does nothing; acts as a placeholder|

# `break`

The `break` statement **terminates the entire loop immediately** when its condition is met.

Example:

```python
for i in range(1, 6):
    if i == 4:
        break
    print(i)
```

Output:

```text
1
2
3
```

When `i` becomes `4`, `break` terminates the loop.

# `continue`

The `continue` statement **skips the current iteration** and moves to the next iteration of the loop.

Example:

```python
for i in range(1, 6):
    if i == 3:
        continue
    print(i)
```

Output:

```text
1
2
4
5
```

When `i` is `3`, the `print()` statement is skipped, but the loop continues.

### `break` vs `continue`

|`break`|`continue`|
|---|---|
|Stops the entire loop|Skips only the current iteration|
|Execution continues after the loop|Loop continues with the next iteration|
|Used for early termination|Used to skip specific iterations|

# `pass`

The `pass` statement is a **null operation** — when Python executes it, nothing happens.

It is useful when a statement is syntactically required but you don't want to write any code yet.

Example:

```python
for i in range(5):
    pass
```

The loop executes, but `pass` does nothing.

### `pass` as a Placeholder

It can be useful when you plan to add code later:

```python
def calculate():
    pass
```

Without `pass`, the function body would be empty and Python would produce a syntax error.

`pass` can be used with:

- `if`
- `if-elif-else`
- `for`
- `while`
- Functions
- Classes

Example:

```python
age = 20

if age >= 18:
    pass
else:
    print("Minor")
```

# `pass` vs Comments

|`pass`|Comment|
|---|---|
|Is an actual Python statement|Is ignored by Python|
|Python executes it|Python does not execute it|
|Used when a syntactically valid statement is required|Used to explain or document code|
|Can act as a placeholder|Cannot act as a code placeholder|

Example:

```python
# This is a comment
```

The comment is completely ignored by Python.

```python
pass
```

`pass` is executed, but it performs no operation.

# `for` vs `while`

|`for` Loop|`while` Loop|
|---|---|
|Used to iterate over a sequence/iterable|Used to execute while a condition is true|
|Commonly used when the number of iterations is known|Commonly used when the number of iterations depends on a condition|
|Automatically moves to the next item|You usually need to update the condition manually|
|Can directly iterate over lists, strings, tuples, etc.|Requires a condition|
|`for x in items:`|`while condition:`|

# Complete Example

The following example demonstrates a `for` loop, `range()`, `continue`, and `break` together:

```python
for i in range(1, 11):

    if i == 3:
        continue

    if i == 8:
        break

    print(i)
```

Output:

```text
1
2
4
5
6
7
```

- When `i == 3`, `continue` skips `3`.
- When `i == 8`, `break` terminates the loop.
- Therefore, `8`, `9`, and `10` are never executed.

# Quick Summary

|Concept|Purpose|Example|
|---|---|---|
|`while`|Repeat while condition is `True`|`while x < 5:`|
|`for`|Iterate over an iterable|`for x in list:`|
|`range()`|Generate a sequence of numbers|`range(1, 10, 2)`|
|`else`|Executes when loop finishes normally|`for x in l: ... else:`|
|`break`|Stop the entire loop|`if x == 5: break`|
|`continue`|Skip current iteration|`if x == 5: continue`|
|`pass`|Do nothing / placeholder|`if x: pass`|