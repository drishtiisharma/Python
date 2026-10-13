**What is umask**

umask stands for "user file-creation mode mask." It determines the default permissions for newly created files and directories.

It works by removing permissions from the system's default maximum permissions.

**Default Maximum Permissions**

Files start with 666 (read and write for owner, group, others). Execute permission is not given by default to files.

Directories start with 777 (read, write, and execute for owner, group, others).

**How umask Works**

umask subtracts permissions from these defaults. The formula is:

Final permissions = Default permissions - umask value

**Common umask Values**

umask 022 is the most common default. It removes write permission from group and others.

For files: 666 - 022 = 644 (owner can read/write, group and others can only read)

For directories: 777 - 022 = 755 (owner has full access, group and others can read and execute)

**Checking Your Current umask**

Run this command in terminal:
```
umask
```

It displays the current umask value in octal format.

**Setting a New umask**

To change umask temporarily for your current session:
```
umask 027
```

This removes write permission from group and all permissions from others.

For files: 666 - 027 = 640 (owner read/write, group read, others nothing)

For directories: 777 - 027 = 750 (owner full access, group read/execute, others nothing)

**Making umask Permanent**

Add the umask command to your ~/.bashrc or ~/.profile file:
```
echo "umask 027" >> ~/.bashrc
```

This applies the setting every time you open a new terminal.

**Viewing Permissions After Creation**

Create a test file and check its permissions:
```
touch testfile
ls -l testfile
```

Create a test directory and check its permissions:
```
mkdir testdir
ls -ld testdir
```

The output shows the actual permissions applied based on your current umask.