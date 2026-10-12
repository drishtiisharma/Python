## Exercise 1 — Refresh package information

Run:

```
sudo apt update
```

What to observe:

- APT contacts your configured software repositories.
    
- It downloads or refreshes package information.
    
- It may show how many packages can be upgraded.


If it asks for your password, enter your Ubuntu user's password. The characters won't appear while you type; that is normal.

## Exercise 2 — Search for software

Run these commands one at a time:

```
apt search tree
```

```
apt search git
```

```
apt search curl
```

Observe the package names and descriptions. Search results can contain many related packages, not just one exact match.

## Exercise 3 — View package details

Run:

```
apt show tree
```

Then:

```
apt show git
```

Identify the package version, description, dependencies, and download size where those details are available.

## Exercise 4 — Install a package

Let's install `tree`. This is especially useful because you previously encountered an error saying that Ubuntu couldn't locate the package.

Run:

```
sudo apt install tree
```

If prompted to continue, type `Y` and press Enter.

If you still get `Unable to locate package tree`, don't keep retrying the installation. Check the output of `sudo apt update` for repository or network errors first.

After installation, run:

```
tree --version
```

Then:

```
tree ~
```

The first command checks the installed program's version; the second displays your home directory in a tree structure.

## Exercise 5 — Check the installation

Run:

```
dpkg -s tree
```

Then:

```
dpkg -L tree
```

Notice the difference:

- `dpkg -s` shows package status and metadata.
    
- `dpkg -L` lists the files installed by the package.
    

You can also check the executable's location:

```
which tree
```

This usually prints the path of the executable found through your `PATH`.

## Exercise 6 — Check available upgrades

Run:

```
apt list --upgradable
```

If packages are listed, they have upgrades available according to your current package information. If none are listed, that is fine too.

For now, you don't need to run a full upgrade just for this exercise.

## Exercise 7 — Understand dependencies

Run:

```
apt depends tree
```

Then:

```
apt depends git
```

Observe which other packages each package depends on. Some dependencies may already be installed on your system.

## Exercise 8 — Practice removing software

Since `tree` is only a practice package, you can use it to understand removal.

First, remove it:

```
sudo apt remove tree
```

Check whether it is still installed:

```
dpkg -s tree
```

You should now see that the package is no longer installed.

Next, install it again:

```
sudo apt install tree
```

Note: If you want to keep `tree` installed, you can skip this exercise.

## Exercise 9 — Understand `autoremove` and `clean`

Run:

```
sudo apt autoremove
```

Read the proposed changes carefully before confirming. If APT says no packages need to be removed, that's perfectly fine.

Next, run:

```
sudo apt clean
```

This clears downloaded package archives from APT's cache. It does not remove installed software.

## Difference between `apt`, `dpkg` and `snap`:

`apt`, `dpkg`, and `snap` are all used to manage software in Linux, but they work differently. 
- **APT** is a **high-level package manager** that installs software from repositories and automatically handles dependencies. 
- **dpkg** is a **lower-level tool** that installs, removes, and manages individual `.deb` package files, but it does not automatically download and resolve missing dependencies. 
- **Snap** manages applications packaged in the `.snap` format, usually from the **Snap Store**, and normally updates them automatically.

## Difference between `sudo apt update` and `sudo apt upgrade`:

- `sudo apt update` refreshes the package lists from configured repositories to check which software versions are available. It does not upgrade the installed software.

- `sudo apt upgrade` downloads and installs available updates for packages already installed on your system.
