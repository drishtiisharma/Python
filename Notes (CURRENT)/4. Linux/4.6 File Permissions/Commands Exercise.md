## Exercise 1: Create files and inspect permissions

Run these commands one by one:

```
mkdir -p ~/projects/permissions-practice
cd ~/projects/permissions-practice
```

Create two files and a directory:

```
touch alpha.txt beta.txt
mkdir reports
```

Add some text:

```
echo "Linux file permissions practice" > alpha.txt
echo "Second practice file" > beta.txt
```

Now inspect the permissions:

```
ls -l
ls -ld reports
stat alpha.txt
```

Your task: Identify the owner, group, and permission string for `alpha.txt`.

## Exercise 2: Practice numeric permissions

First, set the permissions:

```
chmod 644 alpha.txt
ls -l alpha.txt
```

Expected permission string:

```
-rw-r--r--
```

Now try each command and inspect the result after each one:

```
chmod 600 alpha.txt
ls -l alpha.txt
```

```
chmod 640 alpha.txt
ls -l alpha.txt
```

```
chmod 755 alpha.txt
ls -l alpha.txt
```

```
chmod 400 alpha.txt
ls -l alpha.txt
```

Finally, restore the standard practice-file permission:

```
chmod 644 alpha.txt
```

Your task: For each numeric mode, write down what the owner, group, and others can do.

## Exercise 3: Practice symbolic permissions

Start with:

```
chmod 600 alpha.txt
```

Now add read permission for the group:

```
chmod g+r alpha.txt
ls -l alpha.txt
```

Remove the owner's write permission:

```
chmod u-w alpha.txt
ls -l alpha.txt
```

Give everyone read permission:

```
chmod a+r alpha.txt
ls -l alpha.txt
```

Set the owner's permissions exactly to read and write:

```
chmod u=rw alpha.txt
ls -l alpha.txt
```

Your task: Explain the difference between `+`, `-`, and `=` in these commands.

## Exercise 4: Practice directory permissions

Create a directory with a file inside it:

```
mkdir reports/private
echo "Confidential report" > reports/private/report.txt
```

Set permissions:

```
chmod 700 reports
chmod 700 reports/private
chmod 600 reports/private/report.txt
```

Inspect them:

```
ls -ld reports
ls -ld reports/private
ls -l reports/private/report.txt
```

Now test access as your current user:

```
cat reports/private/report.txt
```

It should work because your current user owns the files and directories.

Next, remove execute permission from `reports`:

```
chmod 600 reports
```

Try:

```
ls reports
cat reports/private/report.txt
```

These access attempts should fail because the directory no longer has execute permission for you.

Restore the directory permissions:

```
chmod 700 reports
```

Your task: Explain why the file's own permissions were not enough to guarantee access.

## Exercise 5: Practice owner and group changes

First, check your current identity:

```
whoami
id
groups
```

Create a practice group:

```
sudo groupadd permgroup
```

Assign the group to `alpha.txt`:

```
sudo chgrp permgroup alpha.txt
```

Verify:

```
ls -l alpha.txt
```

Now change the owner and group:

```
sudo chown root:permgroup beta.txt
ls -l beta.txt
```

The owner should now be `root`, and the group should be `permgroup`.

Restore ownership to your user:

```
sudo chown drishti:permgroup beta.txt
```

Replace `drishti` with your actual username if yours differs.

Your task: Explain what changed after each `chgrp` and `chown` command.

## Exercise 6: Create a shared group directory

This exercise builds on the Linux group-management topic you've already studied.

Create a directory and assign the group:

```
mkdir shared
sudo chgrp permgroup shared
chmod 2770 shared
```

Check:

```
ls
```