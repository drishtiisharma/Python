# Linux File Permissions

## 1. What are file permissions in Linux?

File permissions determine who can access a file or directory and what actions they can perform.

Linux uses permissions to control whether users can read, modify, execute, or access files and directories.

For example, suppose you have a file named `alpha.txt`. Linux can allow:

- The owner to read and modify the file.
    
- Members of a particular group to read the file.
    
- Other users to have no access to the file.

This helps protect files from unauthorized access or modification.

## 2. The three permission types

Linux has three basic permissions.

| Permission | Symbol | Numeric value | Meaning for a file          | Meaning for a directory                                                          |
| ---------- | ------ | ------------- | --------------------------- | -------------------------------------------------------------------------------- |
| Read       | `r`    | 4             | View file contents          | List directory contents                                                          |
| Write      | `w`    | 2             | Modify file contents        | Create, delete, or rename entries, subject to other restrictions                 |
| Execute    | `x`    | 1             | Run an executable or script | Enter/access the directory and access its contents, subject to other permissions |

Important: Directory permissions work differently from file permissions. For example, reading a directory lets you list its entries, but accessing a file inside it also depends on directory execute permission and the file's own permissions.

## 3. The three permission categories

Permissions are assigned to three categories of users.

|Category|Symbol|Meaning|
|---|---|---|
|Owner (user)|`u`|The user who owns the file|
|Group|`g`|Users belonging to the file's group|
|Others|`o`|Everyone else, excluding the owner and applicable group members|
|All|`a`|Owner, group, and others|

For example, suppose a file belongs to user `drishti` and group `alpha`.

- `drishti` is the owner.
    
- Members of `alpha` are in the group category, except that the owner is evaluated under the owner category.
    
- Other users fall under the others category.

Linux checks the applicable permission category when a user attempts to access a file.

## 4. Understanding Linux file permissions

Run:

```
ls -l
```

Example output:

```
-rwxr-xr-- 1 drishti alpha 120 Oct 12 10:30 alpha.txt
```

Let's break down the permission string.

### Permission string: `-rwxr-xr--`

# `-`

File type

# `rwx`

Owner

# `r-x`

Group

# `r--`

Others


The first character indicates the file type; the next nine characters are divided into three groups of three permissions each.

The first character can indicate:

- `-` — regular file
    
- `d` — directory
    
- `l` — symbolic link
    

In the example:

- Owner (`drishti`) can read, write, and execute.
    
- Group (`alpha`) can read and execute.
    
- Others can only read.


### What does `ls -l` show?

| Position      | Meaning                |
| ------------- | ---------------------- |
| 1             | File type              |
| 2–10          | Permissions            |
| Next field    | Number of hard links   |
| Next field    | Owner                  |
| Next field    | Group                  |
| Next field    | File size in bytes     |
| Date and time | Last modification time |
| Final field   | File or directory name |

To inspect one specific file:

```
ls -l alpha.txt
```

To inspect a directory and its contents:

```
ls -ld projects
ls -l projects
```

The `-d` option makes `ls` display the directory itself rather than listing its contents.

## 5. Changing permissions using `chmod`

The `chmod` command means change mode. It changes file or directory permissions.

There are two common methods:

1. Numeric method — `chmod 640 file.txt`
    
2. Symbolic method — `chmod u+r file.txt`

### A. Numeric method

Each permission has a number:

|Permission|Value|
|---|---|
|Read (`r`)|4|
|Write (`w`)|2|
|Execute (`x`)|1|

Add the values to calculate each category's permission.

|Permission|Calculation|Numeric value|
|---|---|---|
|`---`|0|0|
|`--x`|1|1|
|`-w-`|2|2|
|`-wx`|2 + 1|3|
|`r--`|4|4|
|`r-x`|4 + 1|5|
|`rw-`|4 + 2|6|
|`rwx`|4 + 2 + 1|7|

Three digits represent owner, group, and others, respectively.

For example:

```
chmod 754 alpha.txt
```

This means:

- `7` = owner: `rwx`
    
- `5` = group: `r-x`
    
- `4` = others: `r--`


The resulting permission string is:

```
-rwxr-xr--
```

More common examples:

|Command|Owner|Group|Others|
|---|---|---|---|
|`chmod 777 file.txt`|`rwx`|`rwx`|`rwx`|
|`chmod 755 file.txt`|`rwx`|`r-x`|`r-x`|
|`chmod 700 file.txt`|`rwx`|`---`|`---`|
|`chmod 644 file.txt`|`rw-`|`r--`|`r--`|
|`chmod 640 file.txt`|`rw-`|`r--`|`---`|
|`chmod 600 file.txt`|`rw-`|`---`|`---`|
|`chmod 400 file.txt`|`r--`|`---`|`---`|

Important: `chmod 777` gives everyone read, write, and execute permissions. Avoid using it as a routine fix for permission errors.

### B. Symbolic method

The symbolic method changes selected permissions without requiring you to calculate numeric values.

The syntax is:

```
chmod [who][operator][permission] filename
```

| Operator | Meaning                                            |
| -------- | -------------------------------------------------- |
| `+`      | Add permission                                     |
| `-`      | Remove permission                                  |
| `=`      | Set permissions exactly for the specified category |

Examples:

```
chmod u+x alpha.txt
```

Add execute permission for the owner.

```
chmod g-w alpha.txt
```

Remove write permission from the group.

```
chmod o-r alpha.txt
```

Remove read permission from others.

```
chmod u=rw alpha.txt
```

Set the owner's permissions to read and write only.

```
chmod a+r alpha.txt
```

Add read permission for everyone.

```
chmod u=rwx,g=rx,o=r alpha.txt
```

Set the owner's permissions to `rwx`, the group's to `r-x`, and others' to `r--`.

Difference: `chmod g-w` removes group write permission while preserving the group's other permissions. `chmod g=r` sets the group's permissions to read only, removing its write and execute permissions.

## 6. Changing file ownership using `chown`

The `chown` command changes the owner of a file or directory.

Syntax:

```
sudo chown username filename
```

Example:

```
sudo chown sharma alpha.txt
```

The owner becomes `sharma`.

To change both owner and group:

```
sudo chown sharma:alpha alpha.txt
```

To change only the group using `chown`:

```
sudo chown :alpha alpha.txt
```

Usually, changing ownership requires root privileges or `sudo`.

To check the result:

```
ls -l alpha.txt
```

## 7. Changing group ownership using `chgrp`

The `chgrp` command changes the group associated with a file or directory.

Syntax:

```
sudo chgrp groupname filename
```

Example:

```
sudo chgrp alpha alpha.txt
```

The file's group becomes `alpha`, while its owner remains unchanged.

To verify:

```
ls -l alpha.txt
```

Difference between `chown` and `chgrp`:

- `chown` changes the owner and can also change the group.
    
- `chgrp` changes the group only.
    

## 8. Directory permissions in detail

Directory permissions are particularly important in Linux.

|Permission|What it allows|
|---|---|
|`r`|List directory entries using commands such as `ls`|
|`w`|Create, delete, or rename entries, normally combined with `x`|
|`x`|Traverse the directory and access entries when other permissions permit|

For example:

```
chmod 700 mydir
```

Only the owner has read, write, and execute permissions on the directory.

```
chmod 755 mydir
```

The owner has full permissions; group members and others can list and traverse the directory but cannot modify its entries through directory permissions alone.

```
chmod 750 mydir
```

The owner has full permissions, the group has read and execute permissions, and others have no permissions.

### Important concept: Directory execute permission

Suppose a directory contains `alpha.txt`.

A user may have read permission on `alpha.txt`, but if that user lacks execute permission on the directory, they may still be unable to access the file through that directory.

For a user to access a file by its path, the user generally needs execute permission on each parent directory in the path, along with the appropriate permissions on the file.

## 9. Recursive permissions using `-R`

The `-R` option applies a permission or ownership change recursively to a directory and its contents.

For example:

```
chmod -R 750 mydir
```

This applies mode `750` to the directory and all files and subdirectories beneath it.

Similarly:

```
sudo chown -R drishti:alpha mydir
```

This changes ownership and group ownership throughout the directory tree.

Caution: Recursive `chmod` applies the same permissions to files and directories. This can make ordinary files executable or remove required access. For real projects, use more targeted commands when files and directories need different permissions.

## 10. Default permissions and `umask`

The `umask` command controls which permission bits are removed from the default permissions of newly created files and directories.

Check the current value:

```
umask
```

A common result is:

```
0022
```

With a typical default mode of `666` for files and `777` for directories:

- New files generally become `644` (`rw-r--r--`).
    
- New directories generally become `755` (`rwxr-xr-x`).
    

This assumes the usual creation modes and a `0022` umask. Applications can specify different modes when creating files.

Set the umask for your current shell:

```
umask 027
```

With this value, typical new files receive mode `640`, and new directories receive mode `750`.

Check it again:

```
umask
```

The change usually affects the current shell and processes started from it; it does not automatically change existing files.

## 11. Special permissions: Setuid, Setgid, and Sticky Bit

These are advanced permission bits that modify normal permission behavior.

| Permission | Numeric bit | Main purpose                                                                                                                                |
| ---------- | ----------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| Setuid     | `4000`      | On applicable executable files, run with the file owner's effective user ID                                                                 |
| Setgid     | `2000`      | On applicable executable files, run with the file's effective group ID; on directories, new entries generally inherit the directory's group |
| Sticky bit | `1000`      | On directories, restrict deletion or renaming of entries, typically to the entry owner, directory owner, or root                            |

Examples:

```
chmod 4755 file
chmod 2775 shared_dir
chmod 1777 shared_dir
```

These examples demonstrate the numeric bits; they are not recommendations to apply them indiscriminately.

A familiar example is `/tmp`, which commonly has sticky-bit permissions such as:

```
drwxrwxrwt
```

The final `t` indicates the sticky bit with execute permission for others.

Be especially careful with setuid and setgid on executable files because they can have security implications.

## 12. Useful permission-related commands

|Command|Purpose|
|---|---|
|`ls -l`|View permissions, owner, and group|
|`ls -ld directory`|View a directory's own permissions|
|`stat filename`|View detailed file metadata and permissions|
|`chmod 640 file`|Set numeric permissions|
|`chmod u+x file`|Add owner execute permission|
|`chown user file`|Change the owner|
|`chgrp group file`|Change the group|
|`id`|Display your user ID, group ID, and groups|
|`groups`|Display your group memberships|
|`umask`|Display the current permission mask|
|`namei -l /path/to/file`|Inspect permissions along a file's path|
|`getfacl file`|Display ACL permissions when ACL tools and support are available|
|`setfacl -m u:user:r file`|Add a named user's read permission through an ACL when ACL support is available|

### Bonus: ACL permissions

Linux Access Control Lists (ACLs) allow permissions for specific users or groups beyond the standard owner/group/others model.

For example:

```
setfacl -m u:sharma:r alpha.txt
```

This grants user `sharma` read permission through an ACL, subject to the ACL mask and permissions required on parent directories.

Use `getfacl alpha.txt` to inspect the resulting ACL. ACL tools may need to be installed, and filesystem support is required.


