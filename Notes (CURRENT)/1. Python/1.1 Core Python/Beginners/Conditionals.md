# Conditional Statements

**Conditional statements** are used to execute different blocks of code based on whether a condition is `True` or `False`.

Python provides:

- `if`
- `elif`
- `else`
- Nested `if`
- Shorthand `if`
- Shorthand `if-else`
- `match` 

# `if`

The `if` statement executes a block of code **only when its condition is `True`**.

### Syntax

```python
if condition:
    # code to execute
```

Example:

```python
age = 20

if age >= 18:
    print("Adult")
```

Output:

```text
Adult
```

# `if...else`

`if...else` is used when there are **two possible conditions/outcomes**.

- If the `if` condition is `True`, the `if` block executes.
- Otherwise, the `else` block executes.

Example:

```python
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")
```

Output:

```text
Minor
```

# `elif`

`elif` means **"else if"**.

It is used when there are **three or more possible conditions**.

Python checks the conditions from top to bottom. Once it finds a condition that is `True`, its block executes and the remaining conditions are skipped.

Example:

```python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Output:

```text
Grade B
```

Since `marks >= 75` is `True`, Python executes that block and does not check the remaining `elif` conditions.

### `if` vs `elif`

Using multiple independent `if` statements:

```python
marks = 95

if marks >= 50:
    print("Pass")

if marks >= 75:
    print("Grade B")

if marks >= 90:
    print("Grade A")
```

All three conditions are checked.

Using `if...elif...else`:

```python
marks = 95

if marks >= 90:
    print("Grade A")
elif marks >= 75:
    print("Grade B")
elif marks >= 50:
    print("Grade C")
else:
    print("Fail")
```

Only the first matching condition is executed.

# `else`

The `else` block catches anything that was **not handled by the preceding conditions**.

It provides a **default action** and must come at the end.

Example:

```python
number = 7

if number > 10:
    print("Greater than 10")
elif number == 10:
    print("Equal to 10")
else:
    print("Less than 10")
```

Output:

```text
Less than 10
```

# Shorthand `if`

When there is only **one statement** to execute, it can be written on the same line as the `if`.

```python
age = 20

if age >= 18: print("Adult")
```

The colon `:` is still required.

# Shorthand `if...else`

A one-line `if...else` statement is called a:

- **Ternary operator**
    
- **Conditional expression**
    

### Syntax

```text
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

status = "Adult" if age >= 18 else "Minor"

print(status)
# Adult
```

Another example:

```python
a = 10
b = 20

result = a if a > b else b

print(result)
# 20
```

# Nested `if`

A **nested `if`** is an `if` statement inside another `if` statement.

The inner `if` executes **only if the outer `if` condition is `True`**.

Example:

```python
age = 20
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
    else:
        print("Needs a license")
else:
    print("Too young to drive")
```

Output:

```text
Can drive
```

### When to Use Nested `if`

Use a nested `if` when the **second condition depends on the first condition being true** and you need checks at multiple levels.

Example:

```python
username = "admin"
password_correct = True

if username == "admin":
    if password_correct:
        print("Login successful")
```

Here, checking the password only makes sense after confirming the username.

# Nested `if` vs Logical Operators

Sometimes nested `if` statements can be replaced with logical operators.

### Nested `if`

```python
age = 25
has_license = True

if age >= 18:
    if has_license:
        print("Can drive")
```

### Using `and`

```python
if age >= 18 and has_license:
    print("Can drive")
```

### When to Use Which?

|Nested `if`|Logical Operators|
|---|---|
|Second condition depends on the first condition|Multiple conditions need to be checked together|
|Useful for multiple levels of decision-making|Useful when conditions are independent|
|Makes hierarchical checks clearer|Makes combined conditions more concise|

# `match` Statement

The `match` statement is used to select **one of several code blocks** based on the value of an expression.

It can be useful when you have many possible values to compare against.

### Syntax

```python
match value:
    case value1:
        # code
    case value2:
        # code
    case _:
        # default code
```

Example:

```python
day = 3

match day:
    case 1:
        print("Monday")
    case 2:
        print("Tuesday")
    case 3:
        print("Wednesday")
    case 4:
        print("Thursday")
    case _:
        print("Invalid day")
```

Output:

```text
Wednesday
```

The `_` case acts as a **default case** when none of the other cases match.

# `if...elif...else` vs `match`

|`if...elif...else`|`match`|
|---|---|
|Checks conditions|Matches values/patterns|
|Can use comparisons such as `>`, `<`, `>=`|Primarily used for matching patterns/values|
|Suitable for ranges and complex conditions|Suitable when choosing based on specific patterns/values|
|Example: `if age >= 18:`|Example: `case 18:`|

# Quick Summary

|Statement|Purpose|Example|
|---|---|---|
|`if`|Executes code when condition is true|`if age >= 18:`|
|`if...else`|Handles two possible outcomes|`if x > 0: ... else:`|
|`elif`|Checks additional conditions|`elif x == 0:`|
|`else`|Default action when previous conditions are false|`else:`|
|Shorthand `if`|One-line `if`|`if x > 0: print(x)`|
|Ternary|One-line `if...else`|`x if condition else y`|
|Nested `if`|`if` inside another `if`|`if x: if y:`|
|`match`|Selects a block based on matching a value/pattern|`match x: case 1:`|
