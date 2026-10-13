# Part 2: Practical Commands Exercise

We'll perform these exercises in your Ubuntu terminal in WSL. Start with your normal user, `drishti`, rather than root.

## Exercise 1 — Check your shell

Run these commands one by one.

```
echo $SHELL
```

Displays your configured default shell.

```
bash --version
```

Displays the installed Bash version.

```
whoami
```

Displays your current username.

```
pwd
```

Displays your current working directory.

## Exercise 2 — Create your practice directory

Let's keep all our shell scripts in one place.

```
mkdir -p ~/projects/shell-scripting
cd ~/projects/shell-scripting
```

Verify the location:

```
pwd
```

List the files:

```
ls -la
```

The directory should initially be empty except for `.` and `..`.

## Exercise 3 — Create and execute your first script

Create a file:

```
nano hello.sh
```

Write the following inside it:

```
#!/bin/bash

# My first shell script

echo "Hello, Linux!"
echo "I am learning shell scripting."
echo "My username is:"
whoami
```

Save and exit Nano:

- Press `Ctrl + O` to save.
    
- Press `Enter` to confirm the filename.
    
- Press `Ctrl + X` to exit.
    

Run the script:

```
bash hello.sh
```

Now give it execute permission:

```
chmod +x hello.sh
```

Execute it directly:

```
./hello.sh
```

What you learn: Script creation, shebang, comments, `echo`, `whoami`, `chmod`, and script execution.

## Exercise 4 — Work with variables

Create another script:

```
nano variables.sh
```

Write:

```
#!/bin/bash

name="Drishti"
course="CSE-AIML"
year=3

echo "Name: $name"
echo "Course: $course"
echo "Year: $year"
```

Execute it:

```
bash variables.sh
```

Now modify the values and run it again.

Practice task: Add two variables named `college` and `city`, and print their values.

## Exercise 5 — Take user input

Create:

```
nano input.sh
```

Write:

```
#!/bin/bash

read -p "Enter your name: " name
read -p "Enter your course: " course

echo "Hello, $name"
echo "You are studying $course"
```

Run it:

```
bash input.sh
```

Enter your details when prompted.

Practice task: Ask the user for their age and display it.

## Exercise 6 — Perform arithmetic

Create:

```
nano calculator.sh
```

Write:

```
#!/bin/bash

read -p "Enter first number: " a
read -p "Enter second number: " b

echo "Addition: $((a + b))"
echo "Subtraction: $((a - b))"
echo "Multiplication: $((a * b))"
echo "Division: $((a / b))"
```

Run:

```
bash calculator.sh
```

Try `10` and `5` as inputs.

Expected output:

```
Addition: 15
Subtraction: 5
Multiplication: 50
Division: 2
```

Important: This example expects valid integers and a non-zero divisor. Dividing by zero causes an arithmetic error.

## Exercise 7 — Use conditions

Create:

```
nano even-odd.sh
```

Write:

```
#!/bin/bash

read -p "Enter a number: " num

if [ $((num % 2)) -eq 0 ]; then
    echo "Even number"
else
    echo "Odd number"
fi
```

Execute it:

```
bash even-odd.sh
```

Try both an even number and an odd number.

Practice task: Write a script that accepts a number and checks whether it is positive, negative, or zero.

## Exercise 8 — Practise loops

Create:

```
nano loops.sh
```

Write:

```
#!/bin/bash

for i in {1..5}
do
    echo "Number: $i"
done
``
```