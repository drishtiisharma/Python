# Strings

A **string** is a sequence of characters used to store text.

- Strings are surrounded by **single (`' '`) or double (`" "`) quotation marks**.
- Strings are arrays/sequences of **Unicode characters**.
- Square brackets `[]` are used to access individual characters of a string.
- `len()` is used to find the length of a string.
- The `in` keyword checks whether a character or word is present in a string.
- The `not in` keyword checks whether a character or word is not present in a string.
- Strings are **immutable**, meaning their individual characters cannot be changed after creation.
## Creating Strings

```python
name = "Python"
language = 'Python'
```

## Accessing Characters

Square brackets are used to access individual characters using their **index**.

```python
text = "Python"

print(text[0])   # P
print(text[1])   # y
print(text[-1])  # n
```

|Index|`0`|`1`|`2`|`3`|`4`|`5`|
|--:|---|---|---|---|---|---|
|Character|`P`|`y`|`t`|`h`|`o`|`n`|

## Length of a String

The `len()` function returns the number of characters in a string.

```python
text = "Python"

print(len(text))  # 6
```

## Checking if a Value Exists

The `in` and `not in` keywords are used to check whether a character or word exists in a string.

```python
text = "Python programming"

print("Python" in text)       # True
print("Java" in text)         # False
print("Java" not in text)     # True
```

## String Slicing

Slicing is used to extract a portion of a string.

### Syntax

```text
string[start:stop:step]
```

|Parameter|Description|
|---|---|
|`start`|Starting index|
|`stop`|Ending index (not included)|
|`step`|Number of positions to move|

Example:

```python
text = "Python"

print(text[0:3])   # Pyt
print(text[2:5])   # tho
print(text[:4])    # Pyth
print(text[2:])    # thon
print(text[::2])   # Pto
```

## String Concatenation

The `+` operator is used to join two or more strings.

```python
first = "Hello"
second = "World"

result = first + " " + second

print(result)
# Hello World
```

## Combining String and Numbers

A string and an integer cannot be directly concatenated using `+`.

The `format()` method can be used to combine different data types.

```python
age = 20

text = "I am {} years old".format(age)

print(text)
# I am 20 years old
```

## Escape Characters

Escape characters are used to insert characters that are otherwise difficult or impossible to type directly inside a string.

|Escape Character|Meaning|Example|
|---|---|---|
|`\'`|Single quote|`'It\'s Python'`|
|`\"`|Double quote|`"He said \"Hello\""`|
|`\\`|Backslash|`"C:\\Python"`|
|`\n`|New line|`"Hello\nWorld"`|
|`\t`|Tab|`"Hello\tWorld"`|

Example:

```python
text = "Hello\nWorld"

print(text)
```

Output:

```text
Hello
World
```

# Main String Methods

|Method|Description|Example|
|---|---|---|
|`capitalize()`|Converts the first character to uppercase|`"python".capitalize()` → `"Python"`|
|`lower()`|Converts the string to lowercase|`"PYTHON".lower()` → `"python"`|
|`upper()`|Converts the string to uppercase|`"python".upper()` → `"PYTHON"`|
|`title()`|Converts the first character of each word to uppercase|`"hello world".title()` → `"Hello World"`|
|`strip()`|Removes leading and trailing whitespace|`" Python ".strip()` → `"Python"`|
|`replace()`|Replaces a specified value with another value|`"Hello".replace("H", "J")` → `"Jello"`|
|`split()`|Splits a string into a list|`"a,b,c".split(",")` → `['a', 'b', 'c']`|
|`join()`|Joins elements of an iterable into a string|`"-".join(["a","b"])` → `"a-b"`|
|`find()`|Returns the position of the first occurrence|`"Python".find("t")` → `2`|
|`count()`|Returns the number of occurrences|`"banana".count("a")` → `3`|
|`startswith()`|Checks whether a string starts with a value|`"Python".startswith("Py")` → `True`|
|`endswith()`|Checks whether a string ends with a value|`"Python".endswith("on")` → `True`|
|`isdigit()`|Checks whether all characters are digits|`"123".isdigit()` → `True`|
|`isalpha()`|Checks whether all characters are alphabetic|`"Python".isalpha()` → `True`|
|`isalnum()`|Checks whether all characters are alphanumeric|`"Python123".isalnum()` → `True`|
|`isspace()`|Checks whether all characters are whitespace|`" ".isspace()` → `True`|

## Quick Summary

|Operation|Syntax / Method|Purpose|
|---|---|---|
|Create string|`"Python"`|Store text|
|Access character|`text[0]`|Access a character|
|Length|`len(text)`|Find number of characters|
|Check presence|`"Py" in text`|Check if value exists|
|Check absence|`"Java" not in text`|Check if value doesn't exist|
|Slicing|`text[start:stop:step]`|Extract part of a string|
|Concatenate|`text1 + text2`|Join strings|
|Uppercase|`text.upper()`|Convert to uppercase|
|Lowercase|`text.lower()`|Convert to lowercase|
|Remove whitespace|`text.strip()`|Remove leading/trailing spaces|
|Replace|`text.replace()`|Replace text|
|Split|`text.split()`|Convert string into a list|
|Join|`separator.join()`|Join values into a string|
|Format|`text.format()`|Insert values into a string|