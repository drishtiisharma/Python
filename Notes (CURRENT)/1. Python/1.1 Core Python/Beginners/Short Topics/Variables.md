# Variables

## What it is
- Anything that can change, vary, and is not fixed/constant.
- In Computer Science, it’s a storage location in memory that holds a value which.your program can change later.
- Python has no commands for declaring it.
- Can get the data type of a variable with the type() function.
- Strings can be declared using single/double quotes.

## Rules
Rules for Variable names:
- Must start with letter or  underscore(\_).
- Cannot start with number.
- Can only contain alphanumeric characters.
- Case sensitive.
- Cannot be any of the keywords.

## Different Cases
Different types of typing cases:
- Camel case: myVariableName
- Pascal case: MyVariableName
- Snake case: my\_variable\_name

## Types based on Scope

| Variable Category | Definition (In Short)                             | Short Code Example                                 |
| ----------------- | ------------------------------------------------- | -------------------------------------------------- |
| **Local**         | Created **inside** a function. Trapped there.     | `def run():`  <br>    `x = 10 # Local`             |
| **Global**        | Created **outside** everything. Used anywhere.    | `x = 5 # Global`  <br>`def run(): print(x)`        |
| **Instance**      | Tied to a **specific object**. Each gets its own. | `def __init__(self):`  <br>    `self.name = "Bob"` |
| **Class**         | Tied to the **entire blueprint**. Shared by all.  | `class Game:`  <br>    `speed = 2 # Class var`     |
