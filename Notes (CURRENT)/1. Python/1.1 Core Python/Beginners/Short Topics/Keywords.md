# Keywords

## What are Keywords?

Keywords are **reserved words** built directly into Python. They form the core vocabulary of the language. Because Python uses them to understand your code, you **cannot use them as regular names** for variables, functions, or classes.

## Why are they used? (Purpose)

1. **To Give Instructions:** They tell the Python interpreter exactly what to do (e.g., `if` means make a decision, `for` means repeat an action).
2. **To Define Structure:** They organize your code blocks (e.g., `def` starts a function, `class` starts a blueprint).
3. **To Establish Rules:** They set logic and boundaries (e.g., `global` changes variable scope, `True`/`False` track state).

## Types of Keywords

Python’s **39 keywords** are broken down into **two main types**:

### Standard Keywords (35 Total)

These are permanently reserved everywhere in your script. Using them as a variable name will immediately crash your program with a `SyntaxError`.

- **Value Indicators:** `True`, `False`, `None`
- **Logical Deciders:** `and`, `or`, `not`, `is`, `in`
- **Flow Controllers:** `if`, `elif`, `else`, `for`, `while`, `break`, `continue`, `pass`
- **Code Builders:** `def`, `return`, `lambda`, `class`
- **Error Handlers:** `try`, `except`, `finally`, `raise`, `assert`
- **Scope Changers:** `global`, `nonlocal`
- **File & Module Tools:** `import`, `from`, `as`, `with`, `del`
- **Speed Boosters (Async):** `async`, `await`

### Soft Keywords (4 Total)

These only act as reserved words when used inside specific features (like structural pattern matching). You can safely use them as normal variable names elsewhere in your code without causing errors.

- `match`
- `case`
- `type`
- `_` (the underscore wildcard)
