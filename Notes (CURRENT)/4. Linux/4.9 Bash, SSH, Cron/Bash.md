# Bash (Bourne Again Shell)

### What is Bash?

Bash is a command-line shell used in Linux to interact with the operating system. It reads commands entered by the user, executes them, and displays the output.

Bash can also execute a collection of commands written in a file called a Bash script.

### Basic Bash commands

|Command|Meaning|
|---|---|
|`pwd`|Displays the current working directory|
|`ls`|Lists files and directories|
|`cd`|Changes the current directory|
|`mkdir`|Creates a directory|
|`touch`|Creates an empty file|
|`cp`|Copies files or directories|
|`mv`|Moves or renames files|
|`rm`|Removes files|
|`cat`|Displays file contents|
|`echo`|Prints text|
|`whoami`|Displays the current username|
|`date`|Displays the current date and time|
|`history`|Displays previously executed commands|

### What is a Bash script?

A Bash script is a text file containing multiple shell commands that can be executed together.

Bash scripts usually use the `.sh` extension.

Example:

```
#!/bin/bash

echo "Hello, Linux!"
whoami
pwd
date
```

Explanation:

- `#!/bin/bash` — The shebang specifies the interpreter used to execute the script.
    
- `echo` — Prints a message.
    
- `whoami` — Displays the current username.
    
- `pwd` — Displays the current directory.
    
- `date` — Displays the date and time.

### How to execute a Bash script

There are two common methods:

Method 1: Execute using Bash

```
bash test.sh
```

This runs the script using Bash without requiring the file to have execute permission.

Method 2: Execute directly

```
chmod +x test.sh
./test.sh
```

Here, `chmod +x` adds execute permission, and `./test.sh` executes the script from the current directory.

### Bash variables

Variables store values that can be used later in a script.

```
name="Drishti"
age=21

echo "$name"
echo "$age"
```

Important rules:

- Do not put spaces around `=` when assigning a variable.
    
- Use `$` to access a variable's value.
    
- Double quotes help preserve spaces in variable values.
    

### Taking user input

The `read` command accepts input from the user.

```
echo "Enter your name:"
read name

echo "Hello, $name"
```

### Conditional statements

The `if` statement executes commands depending on whether a condition is true.

```
#!/bin/bash

read -p "Enter a number: " number

if [ "$number" -gt 10 ]; then
    echo "Number is greater than 10"
else
    echo "Number is 10 or less"
fi
```

Common numeric comparison operators:

|Operator|Meaning|
|---|---|
|`-eq`|Equal to|
|`-ne`|Not equal to|
|`-gt`|Greater than|
|`-lt`|Less than|
|`-ge`|Greater than or equal to|
|`-le`|Less than or equal to|

### Loops in Bash

A loop repeats a set of commands.

Example using a `for` loop:

```
for number in 1 2 3 4 5
do
    echo "$number"
done
```

Example using a `while` loop:

```
number=1

while [ "$number" -le 5 ]
do
    echo "$number"
    number=$((number + 1))
done
```

### Exit status

Every command returns an exit status indicating whether it succeeded.

- `0` — Success.
    
- Non-zero — An error or another unsuccessful outcome.
    

```
ls
echo $?
```

`$?` contains the exit status of the most recently executed command.

