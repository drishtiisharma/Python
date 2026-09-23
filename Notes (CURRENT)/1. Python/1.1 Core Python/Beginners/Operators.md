# Operators

Python has **9 types of operators**:

| No. | Operator Type                  | Description                                              |
| --: | ------------------------------ | -------------------------------------------------------- |
|   1 | Arithmetic Operators           | Perform mathematical operations                          |
|   2 | Assignment Operators           | Assign values to variables                               |
|   3 | Comparison Operators           | Compare two values                                       |
|   4 | Logical Operators              | Combine conditional statements                           |
|   5 | Identity Operators             | Check whether two variables refer to the same object     |
|   6 | Membership Operators           | Check whether a value exists in a sequence               |
|   7 | Bitwise Operators              | Perform operations on binary numbers                     |
|   8 | Conditional (Ternary) Operator | A one-line alternative to `if-else`                      |
|   9 | Walrus Operator                | Assigns a value and uses it immediately in an expression |

## 1. Arithmetic Operators

Used to perform mathematical calculations.

|Operator|Name|Example|
|---|---|---|
|`+`|Addition|`5 + 2 = 7`|
|`-`|Subtraction|`5 - 2 = 3`|
|`*`|Multiplication|`5 * 2 = 10`|
|`/`|Division|`5 / 2 = 2.5`|
|`//`|Floor Division|`5 // 2 = 2`|
|`%`|Modulus|`5 % 2 = 1`|
|`**`|Exponentiation|`5 ** 2 = 25`|

## 2. Assignment Operators

Used to assign or update values in variables.

|Operator|Example|Equivalent To|
|---|---|---|
|`=`|`x = 5`|`x = 5`|
|`+=`|`x += 2`|`x = x + 2`|
|`-=`|`x -= 2`|`x = x - 2`|
|`*=`|`x *= 2`|`x = x * 2`|
|`/=`|`x /= 2`|`x = x / 2`|
|`//=`|`x //= 2`|`x = x // 2`|
|`%=`|`x %= 2`|`x = x % 2`|
|`**=`|`x **= 2`|`x = x ** 2`|
|`&=`, `|=`,` ^=`|Bitwise assignment|

## 3. Comparison Operators

Used to compare two values. They return either `True` or `False`.

|Operator|Meaning|Example|
|---|---|---|
|`==`|Equal to|`5 == 5` → `True`|
|`!=`|Not equal to|`5 != 3` → `True`|
|`>`|Greater than|`5 > 3` → `True`|
|`<`|Less than|`3 < 5` → `True`|
|`>=`|Greater than or equal to|`5 >= 5` → `True`|
|`<=`|Less than or equal to|`3 <= 5` → `True`|

## 4. Logical Operators

Logical operators are used to **combine conditional statements**.

There are 3 logical operators:

- `and`
    
- `or`
    
- `not`

|Operator|Description|Example|Result|
|---|---|---|---|
|`and`|Returns `True` if both conditions are true|`True and True`|`True`|
|`or`|Returns `True` if at least one condition is true|`True or False`|`True`|
|`not`|Reverses the result|`not True`|`False`|

### Precedence of Logical Operators

The precedence order is:

**`not` → `and` → `or`**

For example:

```python
True or False and False
```

`and` is evaluated first:

```python
True or (False and False)
```

Result:

```python
True
```

### Truth Table

|A|B|A `and` B|A `or` B|
|---|---|---|---|
|`True`|`True`|`True`|`True`|
|`True`|`False`|`False`|`True`|
|`False`|`True`|`False`|`True`|
|`False`|`False`|`False`|`False`|

### `not` Truth Table

|A|`not A`|
|---|---|
|`True`|`False`|
|`False`|`True`|

## 5. Identity Operators

Identity operators are used to check whether two variables **refer to the same object in memory**.

There are two identity operators:

|Operator|Meaning|
|---|---|
|`is`|Checks whether both variables refer to the same object|
|`is not`|Checks whether both variables refer to different objects|

### Difference Between `is` and `==`

|`is`|`==`|
|---|---|
|Checks object identity|Checks value equality|
|Determines whether two variables point to the same object in memory|Determines whether the values are equal|
|Example: `a is b`|Example: `a == b`|

Example:

```python
a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)  # True
print(a is b)  # False
```

The values are equal, but they are two different list objects.

## 6. Membership Operators

Membership operators check whether a value exists in a sequence such as a string, list, tuple, or set.

|Operator|Meaning|Example|
|---|---|---|
|`in`|Returns `True` if the value exists|`3 in [1, 2, 3]` → `True`|
|`not in`|Returns `True` if the value does not exist|`5 not in [1, 2, 3]` → `True`|

Example:

```python
name = "Python"

print("P" in name)       # True
print("Java" not in name) # True
```

## 7. Bitwise Operators

Bitwise operators are used to perform operations on **binary numbers**.

|Operator|Name|Description|
|---|---|---|
|`&`|Bitwise AND|Sets a bit to `1` if both bits are `1`|
|`|`|Bitwise OR|
|`^`|Bitwise XOR|Sets a bit to `1` if the bits are different|
|`~`|Bitwise NOT|Inverts the bits|
|`<<`|Left Shift|Shifts bits to the left|
|`>>`|Right Shift|Shifts bits to the right|

Example:

```text
5  = 0101
3  = 0011

5 & 3 = 0001 = 1
5 | 3 = 0111 = 7
5 ^ 3 = 0110 = 6
```

## 8. Conditional (Ternary) Operator

The **ternary operator**, also called a **conditional expression**, is a one-line alternative to a traditional `if-else` statement.

### Syntax

```python
value_if_true if condition else value_if_false
```

Example:

```python
age = 20

result = "Adult" if age >= 18 else "Minor"
```

Here, `"Adult"` is assigned if the condition is `True`; otherwise, `"Minor"` is assigned.

## 9. Walrus Operator (`:=`)

The **walrus operator (`:=`)** allows us to **assign a value to a variable and use that value immediately in the same expression**.

Example:

```python
if (n := len("Python")) > 5:
    print(n)
```

Here, `n` is assigned the value `6`, and that value is immediately used in the condition.

### Normal Assignment vs Walrus Operator

|Normal Assignment|Walrus Operator|
|---|---|
|`n = len("Python")`|`(n := len("Python"))`|
|Assignment is done separately|Assignment and use can happen in the same expression|

# Operator Precedence

Operator precedence determines the **order in which Python evaluates operators**.

A simplified precedence order from **higher to lower** is:

|Priority|Operators|
|--:|---|
|1|`()` — Parentheses|
|2|`**` — Exponentiation|
|3|`+x`, `-x`, `~x` — Unary operators|
|4|`*`, `/`, `//`, `%`|
|5|`+`, `-`|
|6|`<<`, `>>`|
|7|`&`|
|8|`^`|
|9|`|
|10|`<`, `<=`, `>`, `>=`, `==`, `!=`, `is`, `is not`, `in`, `not in`|
|11|`not`|
|12|`and`|
|13|`or`|
|14|Conditional expression (`if ... else`)|
|15|Assignment expressions (`:=`)|

**Tip:** When in doubt, use parentheses `()` to make the intended order explicit.