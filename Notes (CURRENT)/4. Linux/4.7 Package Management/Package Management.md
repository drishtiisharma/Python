## 1. What is package management in Linux?

Package management is the process of installing, updating, removing, and managing software on a Linux system.

In Linux, software is commonly distributed as packages. A package contains the files and information needed to install a software application, such as its executable files, configuration files, and metadata.

Examples of software you might install:

- `tree` — displays directories in a tree structure.
    
- `git` — version control system.
    
- `curl` — transfers data from URLs.
    
- `python3-pip` — installs Python packages using pip.

Instead of manually downloading and installing every application, we can use a package manager to handle the process.

## 2. What is a package manager?

A package manager is a tool that installs, updates, removes, and manages software packages.

Different Linux distributions use different package managers.

|Linux distribution|Package manager|Package format|
|---|---|---|
|Ubuntu|APT / `apt`|`.deb`|
|Debian|APT / `apt`|`.deb`|
|Fedora|DNF / `dnf`|`.rpm`|
|Arch Linux|Pacman / `pacman`|`.pkg.tar.zst`|

Since you're using Ubuntu, we'll primarily use `apt`.

## 3. What is APT?

APT (Advanced Package Tool) is a package management system used by Ubuntu and Debian-based Linux distributions.

It helps us:

- Install software.
    
- Remove installed software.
    
- Update available package information.
    
- Upgrade installed software.
    
- Search for packages.
    
- View package details.
    
- Manage software dependencies.

Example:

```
sudo apt install git
```

This command installs Git using APT.

### Understanding `sudo apt install git`

- `sudo` — runs the command with administrator privileges.
    
- `apt` — invokes the package management tool.
    
- `install` — tells APT to install a package.
    
- `git` — specifies the package to install.

Administrator privileges are generally required for system-wide package changes.

## 4. What is a software repository?

A software repository is a source from which your Linux system obtains packages and package information.

Ubuntu maintains repositories containing software packages that APT can install.

When you run:

```
sudo apt update
```

APT refreshes its local information about the packages available from your configured repositories.

Important: `apt update` does not normally upgrade the software already installed on your system. It updates the package lists.

Think of these as two different operations:

- `apt update` — refresh information about available packages.
    
- `apt upgrade` — install newer versions of eligible installed packages.


## 5. What is a package index?

A package index is local information about packages available through your configured repositories. It includes details such as package names, versions, and dependencies.

APT uses this information to determine which packages are available and which versions can be installed.

After a fresh Ubuntu installation, or when the package information is outdated, run:

```
sudo apt update
```

This refreshes the package index.

## 6. Installing packages

To install a package:

```
sudo apt install package_name
```

Example:

```
sudo apt install tree
```

APT finds the package in your configured repositories, resolves its dependencies, and installs it.

To install multiple packages in one command:

```
sudo apt install git curl tree
```

APT can install all three packages in the same operation.

## 7. Searching for packages

To search for a package by name or description:

```
apt search keyword
```

Example:

```
apt search tree
```

This displays matching packages from the available package information.

To search for an exact package name or check whether it is available, you can also use:

```
apt-cache policy tree
```

This shows the installed version, if any, and candidate version information when available.

## 8. Viewing package information

To display detailed information about a package:

```
apt show package_name
```

Example:

```
apt show git
```

The output may include:

- Package name
    
- Version
    
- Package size
    
- Dependencies
    
- Description
    
- Package maintainer
    

This is useful when you want to understand what a package does before installing it.

## 9. Updating and upgrading software

These two commands have different purposes.

Update package lists:

```
sudo apt update
```

Refreshes information about available package versions from configured repositories.

Upgrade installed packages:

```
sudo apt upgrade
```

Installs available upgrades for eligible packages already installed on your system.

You can run them one after another:

```
sudo apt update
sudo apt upgrade
```

Review the packages and changes APT proposes before confirming an upgrade.

## 10. Removing packages

To remove an installed package:

```
sudo apt remove package_name
```

Example:

```
sudo apt remove tree
```

This removes the package's installed software files but generally preserves system-wide configuration files managed by the package.

To remove the package along with its system-wide configuration files:

```
sudo apt purge package_name
```

Example:

```
sudo apt purge tree
```

Difference:

- `remove` — removes the installed package but generally keeps system-wide configuration files.
    
- `purge` — removes the package and its package-managed system-wide configuration files.


Neither command necessarily deletes every file that an application might have created in your home directory.

## 11. Removing unnecessary packages

Sometimes APT installs additional packages because the software you requested depends on them. Those packages may become unnecessary after the original software is removed.

To remove packages that APT identifies as no longer needed:

```
sudo apt autoremove
```

Review the proposed removal list before confirming. Avoid automatically accepting removals without checking what will be deleted.

## 12. Checking installed packages

To list packages installed on your system:

```
apt list --installed
```

The output may be lengthy because Ubuntu includes many packages.

To check whether a particular package is installed:

```
dpkg -s package_name
```

Example:

```
dpkg -s git
```

If the package is installed, the output includes its status and other details.

If you only want a quick check of a package's installation state, you can use:

```
dpkg -l git
```

`dpkg` is a lower-level package management tool that works with Debian packages. APT uses it as part of its package management process.

## 13. Checking package dependencies

A dependency is another package or software component required by a package to work correctly.

For example, a program may need a shared library before it can run.

APT automatically resolves and installs the dependencies required by packages you install through it.

To view a package's dependencies:

```
apt depends package_name
```

Example:

```
apt depends git
```

This displays the package dependencies declared for Git.

## 14. Understanding `.deb` packages

Ubuntu uses the `.deb` package format.

A `.deb` file is a package file containing software and package metadata used during installation.

You can install a local `.deb` file using:

```
sudo apt install ./package_name.deb
```

The `./` indicates that the file is in your current directory. APT can also resolve dependencies from configured repositories.

Another tool is `dpkg`:

```
sudo dpkg -i package_name.deb
```

This installs a local Debian package, but `dpkg` does not automatically resolve and download missing dependencies in the same way APT does.

For beginners, prefer APT when possible.

## 15. Checking which files a package installed

Sometimes you may want to see the files installed by a particular package.

Use:

```
dpkg -L package_name
```

Example:

```
dpkg -L git
```

This lists files recorded as belonging to the installed Git package.

To find which installed package owns a particular file:

```
dpkg -S /path/to/file
```

For example, if a file belongs to an installed package, `dpkg -S` can help identify that package.

## 16. Checking available upgrades

To list installed packages for which upgrades are available:

```
apt list --upgradable
```

Run `sudo apt update` first so the available-version information is refreshed.

## 17. Understanding the APT cache

APT maintains downloaded package files and package information in its cache directories.

To remove downloaded package files that are no longer needed from the cache:

```
sudo apt clean
```

This cleans the downloaded package archive cache. It does not uninstall your installed applications.

## 18. Common package management commands — quick revision

|Command|Purpose|
|---|---|
|`sudo apt update`|Refresh package lists|
|`sudo apt upgrade`|Upgrade installed packages|
|`sudo apt install git`|Install Git|
|`sudo apt remove git`|Remove Git|
|`sudo apt purge git`|Remove Git and package-managed system configuration|
|`sudo apt autoremove`|Remove automatically installed packages no longer needed|
|`apt search git`|Search for packages|
|`apt show git`|View package details|
|`apt list --installed`|List installed packages|
|`apt list --upgradable`|List packages with available upgrades|
|`apt depends git`|View package dependencies|
|`dpkg -s git`|View installed package status|
|`dpkg -L git`|List files belonging to an installed package|
|`sudo apt clean`|Clear the downloaded package archive cache|

These commands are the core of package management on Ubuntu. You don't need to memorize everything immediately; focus first on updating, installing, searching, checking, upgrading, and removing packages.

