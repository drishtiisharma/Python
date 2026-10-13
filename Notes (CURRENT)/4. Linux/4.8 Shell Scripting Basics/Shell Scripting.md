# Linux: Shell Scripting Basics

## 1. What is a Shell?

A shell is a command-line interpreter that accepts commands from the user and passes them to the operating system for execution.

Examples of Linux shells:

- Bash (Bourne Again Shell): One of the most commonly used Linux shells.
    
- sh (Bourne Shell): A traditional Unix shell interface.
    
- Zsh (Z Shell): A shell with additional interactive features.
    
- Fish (Friendly Interactive Shell): A shell designed for ease of use.


To check your current shell:

```
echo $SHELL
```

To check the shell you are currently running:

```
ps -p $$
```

Note: Your default shell and your currently running shell may differ. For example, when you use `su` to switch users, you might end up in a different shell.

## 2. What is Shell Scripting?

Shell scripting is the process of writing multiple shell commands in a file so that they can execute together in a specified order.

A shell script is commonly saved with the `.sh` extension.

Examples of what shell scripts can do:

- Create files and directories.
    
- Manage users and file permissions.
    
- Back up important files.
    
- Install or update packages.
    
- Automate repetitive tasks.
    
- Run Python programs or other commands.

Example:

```
#!/bin/bash

echo "Hello, Linux!"
pwd
whoami
```

When executed, this script prints a message, displays the current directory, and shows the current username.

## 3. The Shebang

The shebang is the first line of a script. It specifies which interpreter should execute the script.

Syntax:

```
#!/bin/bash
```

Here:

- `#!` identifies the interpreter directive.
    
- `/bin/bash` is the path to the Bash interpreter.

Another common form is:

```
#!/usr/bin/env bash
```

This searches for Bash using the environment's `PATH`.

> [!NOTE]
> **Why Scripts can run without Shebang too?**
> The shebang makes scripts self-contained and portable. It allows direct execution (`./script.sh`) without typing the interpreter name every time. This is essential for automation, cron jobs, and when other programs call your script, as they rely on the shebang to know which interpreter to use. It also ensures the correct interpreter runs even if the user's default shell is different.

## 4. Creating and Executing a Shell Script

A script can be created using a text editor or a terminal command.

Example:

```
nano hello.sh
```

Write the script, save it, and exit the editor.

There are two common ways to execute it.

Method 1: Run it through Bash

```
bash hello.sh
```

This does not require execute permission on the file, provided Bash can read it.

Method 2: Execute the file directly

```
chmod +x hello.sh
./hello.sh
```

The `chmod +x` command adds execute permission, while `./hello.sh` runs the script from the current directory.

> [!NOTE]
> **What does +x mean?**
> The `chmod +x` adds execute permission to a file for all user categories (owner, group, and others). It makes the file runnable as a program or script. For example, if a file had permissions `644` (read/write for owner, read-only for others), running `chmod +x filename` changes it to `755`, allowing everyone to execute it. This is commonly used for shell scripts or binaries that need to be run directly from the terminal.

## 5. Comments in Shell Scripts

Comments explain the purpose of commands and are ignored by the shell.

A single-line comment starts with `#`.

```
# Display a welcome message
echo "Welcome to Linux"
```

The shebang is also written using `#`, but it has a special purpose when placed at the beginning of a script.

## 6. Displaying Output with `echo`

The `echo` command displays text or variable values.

```
echo "Hello World"
```

You can also display multiple values:

```
echo "Learning Linux Shell Scripting"
echo "Current user:"
whoami
```

## 7. Variables in Shell Scripting

Variables store values that can be reused throughout a script.

Syntax:

```
name="Drishti"
```

To access a variable, place `$` before its name.

```
echo "$name"
```

Example:

```
#!/bin/bash

name="Drishti"
course="CSE-AIML"

echo "Name: $name"
echo "Course: $course"
```

Important rules:

- Do not put spaces around `=` when assigning a value.
    
- Use `$variable_name` to access the value.
    
- Variable names are case-sensitive.
    
- By default, shell variables are treated as strings, although Bash can perform arithmetic operations on numeric values.

Correct:

```
name="Drishti"
```

Incorrect:

```
name = "Drishti"
```

The incorrect form is interpreted as a command named `name` with arguments.

## 8. Taking User Input with `read`

The `read` command accepts input from the user.

Syntax:

```
read variable_name
```

Example:

```
#!/bin/bash

echo "Enter your name:"
read name

echo "Hello, $name"
```

You can also display a prompt directly:

```
read -p "Enter your age: " age
echo "Your age is $age"
```

Here, `-p` displays the prompt before accepting input.

## 9. Arithmetic Operations

Bash supports integer arithmetic using arithmetic expansion.

Syntax:

```
$((expression))
```

Example:

```
a=10
b=5

echo $((a + b))
echo $((a - b))
echo $((a * b))
echo $((a / b))
echo $((a % b))
```

Common arithmetic operators:

|Operator|Meaning|
|---|---|
|`+`|Addition|
|`-`|Subtraction|
|`*`|Multiplication|
|`/`|Integer division|
|`%`|Remainder|
|`**`|Exponentiation|

For example, `10 / 3` produces `3`, not `3.333`, because Bash integer arithmetic truncates the fractional part.

## 10. Conditional Statements: `if`, `else`, and `elif`

Conditional statements allow a script to make decisions based on conditions.

Syntax:

```
if [ condition ]; then
    commands
elif [ another_condition ]; then
    commands
else
    commands
fi
```

Example:

```
#!/bin/bash

read -p "Enter your age: " age

if [ "$age" -ge 18 ]; then
    echo "You are an adult"
else
    echo "You are a minor"
fi
```

Here, `fi` marks the end of the `if` statement.

Common integer comparison operators:

|Operator|Meaning|
|---|---|
|`-eq`|Equal to|
|`-ne`|Not equal to|
|`-gt`|Greater than|
|`-lt`|Less than|
|`-ge`|Greater than or equal to|
|`-le`|Less than or equal to|

For string comparisons, you will commonly use `=` and `!=` inside `[ ... ]`.

Example:

```
if [ "$name" = "Drishti" ]; then
    echo "Name matched"
fi
```

## 11. Loops in Shell Scripting

Loops execute commands repeatedly.

### A. `for` loop

A `for` loop iterates over a sequence of values.

```
for i in 1 2 3 4 5
do
    echo "$i"
done
```

You can also use a numeric range:

```
for i in {1..5}
do
    echo "$i"
done
```

### B. `while` loop

A `while` loop continues as long as its condition is true.

```
i=1

while [ "$i" -le 5 ]
do
    echo "$i"
    i=$((i + 1))
done
```

The variable is incremented during each iteration so the loop eventually stops.

## 12. Functions

A function is a reusable block of commands that performs a particular task.

Syntax:

```
function_name() {
    commands
}
```

Example:

```
greet() {
    echo "Hello, Linux!"
}

greet
```

Here, `greet` defines the function, and calling `greet` executes its commands.

Functions help organize larger scripts and avoid repeating the same code.

## 13. Command-Line Arguments

Command-line arguments allow you to pass values to a script when executing it.

Example script:

```
#!/bin/bash

echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
```

Run it:

```
bash arguments.sh Drishti Linux
```

Special variables:

|Variable|Meaning|
|---|---|
|`$0`|Script name or invocation path|
|`$1`, `$2`, etc.|First, second, and subsequent arguments|
|`$@`|All positional arguments, preserved individually when quoted|
|`$#`|Number of positional arguments|
|`$?`|Exit status of the previous command|

An exit status of `0` usually indicates success; a non-zero status indicates an error or another condition.

## 14. File and Directory Checks

Bash provides operators for checking files and directories.

```
if [ -f "hello.txt" ]; then
    echo "File exists"
fi
```

Common file test operators:

|Operator|Meaning|
|---|---|
|`-e`|Path exists|
|`-f`|Regular file exists|
|`-d`|Directory exists|
|`-r`|Path is readable|
|`-w`|Path is writable|
|`-x`|Path is executable|

Example:

```
if [ -d "projects" ]; then
    echo "Directory exists"
else
    echo "Directory does not exist"
fi
```

## 15. Exit Status and `exit`

Commands return an exit status indicating whether they succeeded.

Check the status of the previous command using:

```
echo $?
```

A script can also return an exit status explicitly:

```
#!/bin/bash

echo "Task completed"
exit 0
```

Use `exit 0` for successful completion and a non-zero value when the script should indicate failure.

## 16. Good Practices for Shell Scripts

- Use meaningful script and variable names.
    
- Add comments where they clarify the purpose of commands.
    
- Quote variables when appropriate, such as `"$name"`, to avoid unwanted word splitting and filename expansion.
    
- Use `bash -n script.sh` to check Bash syntax without executing the script.
    
- Use `bash -x script.sh` to trace commands while debugging.
    
- Avoid using `sudo` unnecessarily.
    
- Test scripts on sample files before using them on important data.
    
- Use `#!/bin/bash` when the script specifically requires Bash syntax.


