# File Handling
- means using python to create, open, read, write, update, and close files
- allows the program to store and retrieve data files on the computer
## Need?
- saves data even after the program ends
- allows program to read files in all formats like: .txt, .csv and .json
- processed large files without loading everything into memory at once
- useful for: reading config files, saving results, generating reports, etc
- files make it easy to store and transfer data between programs

## Operations
### Opening a File
uses `open()` function, which requires file-path and mode as arguments.
***Syntax***
`file = open('filename.txt','mode)`

**Example**
```
f = open('geek.txt','r')
print(f)
```

**Explanation:** code opens file **geek.txt** in read mode. If the file exists, it returns a file object connected to that file; if the file does not exist, Python raises a FileNotFoundError.

### Closing a File
`file.close()` closes the file and releases the system resources.
If the file was opened in write or append mode, closing ensures that all changes are properly saved.

```
f = open('geek.txt','r')
print(f)
f.close()
print("file closed")
```

### Checking Properties

```
f = open('geek.txt','r')
print("filename: ",f.name)
print("mode: ",f.mode)
print("is closed?", f.closed)
f.close()
print("is closed?",f.closed)
```

**Explanation:**

- **f.name**: Returns the name of the file that was opened (in this case, "geek.txt").
- **f.mode**: Tells us the mode in which the file was opened. Here, it’s 'r' which means read mode.
- **f.closed**: Returns a boolean value- False when file is currently open otherwise True.

### Reading File's Content
Reading a file can be achieved by **file.read()** which reads the entire content of the file. After reading, it’s good practice to close the file to free up system resources.

```
f = open('geek.txt','r')
content = f.read()
print(content)
```

### Writing to a File
Writing to a file is done using the mode "**w**". This creates a new file if it doesn’t exist, or overwrites the existing file if it does. The **write()** method is used to add content. After writing, make sure to close the file.

```
f = open("geek.txt",'w')
f.write(
    """
    something
    good
    is
    going
    to 
    happen
    """
)
f.close()
f = open("geek.txt",'r')
content = f.read()
print(content)
```

or, we can use **with** statement:

```
with open("geeks.txt",'w') as f:
    f.write("""
    hello
    world
    """)

print(open('geeks.txt','r').read())
```

When working with files, we should always use the `with` statement (also called a **context manager**). It automatically closes the file for us when the block of code finishes, even if our script crashes or runs into an error.

### Appending to a File
`"a"` - Append - will append to the end of the file, and will create a file if the specified file does not exist.

```
with open("geeks.txt",'a') as f:
    f.write("Added more content")
with open("geeks.txt",'r') as f:
    print(f.read())
```

### Creating a New File
`"x"` - Create - will create a file, returns an error if the file exists.

```
f = open("new.txt",'x')
```

### Deleting a File
to delete a file, we must import the OS module, and run its `os.remove()` function.

```
import os
os.remove("new.txt")
```

#### Checking if a File Exists (before deleting)

```
import os
if os.path.exists("new.txt"):
    os.remove("new.txt")
else:
    print("file does not exist!")
```

#### Deleting an Entire Folder
To delete an entire folder, use the `os.rmdir()` method:

```
import os
os.rmdir("foldername")
```

but with this we can only remove ***empty*** folders.

[[Converting Files to different formats]] : `.txt` , `.csv`, `.json`
