# Root Filesystem in Linux

## What is the Root Filesystem

The root filesystem is the top-level directory in Linux. It is represented by a single forward slash `/`. Everything in Linux starts from this point. All other directories, files, and devices are organized under it in a tree structure.

Think of it like the trunk of a tree. All branches (directories) grow from it.

## Key Directories Under Root

- **/bin** - Essential command binaries (like ls, cp, mkdir). Available to all users.
- **/boot** - Files needed to boot the system, including the kernel and bootloader configuration.
- **/dev** - Device files representing hardware (like hard drives, keyboards).
- **/etc** - Configuration files for the system and applications.
- **/home** - Personal directories for regular users. Each user gets their own folder here.
- **/init** - Not a standard directory. Usually refers to the initial process or symlink to systemd/init binary.
- **/lib** - Essential shared libraries and kernel modules required by binaries in /bin and /sbin.
- **/lib64** - 64-bit shared libraries for systems running on 64-bit architecture.
- **/lost+found** - Directory for recovered files after a filesystem check (fsck). Usually empty.
- **/media** - Mount point for removable media like USB drives and CDs. Automatically created by the system.
- **/mnt** - Temporary mount point for manually mounting filesystems or network shares.
- **/opt** - Optional application software packages. Third-party or add-on software often installs here.
- **/proc** - Virtual filesystem showing process and system information. Not real files.
- **/root** - Home directory for the root (superuser) account.
- **/run** - Runtime data for processes since last boot. Includes PID files and sockets. Replaces /var/run.
- **/sbin** - System binaries for administrative tasks (like fdisk, ifconfig). Mostly for root user.
- **/snap** - Directory for Snap package manager installations and data. Used in Ubuntu.
- **/srv** - Data for services provided by the system, such as web or FTP server files.
- **/sys** - Virtual filesystem for kernel and device information.
- **/tmp** - Temporary files. Cleared on reboot.
- **/usr** - User programs and data. Contains most installed software.
- **/var** - Variable data like logs, mail, and databases.

## Important Concepts

- The root user has full access to the entire filesystem.
- Regular users have limited access based on permissions.
- The root filesystem must be mounted first during boot.
- Other partitions or drives can be mounted under subdirectories.

---

## Commands Exercise

### 1. View the Root Directory Structure

List all top-level directories:
```bash
ls /
```

List with details (permissions, size, date):
```bash
ls -l /
```

### 2. Navigate the Root Filesystem

Go to root directory:
```bash
cd /
```

Check your current location:
```bash
pwd
```

Go to a specific directory:
```bash
cd /etc
```

Go back to parent directory:
```bash
cd ..
```

### 3. Explore Key Directories

View configuration files:
```bash
ls /etc
```

View log files:
```bash
ls /var/log
```

View user home directories:
```bash
ls /home
```

### 4. Check Disk Usage

See how much space each directory uses:
```bash
du -sh /*
```

See overall disk usage:
```bash
df -h
```

### 5. Find Files in Root Filesystem

Search for a file named "passwd":
```bash
find / -name passwd 2>/dev/null
```

Search for files modified in the last day:
```bash
find / -mtime -1 -type f 2>/dev/null | head -20
```

### 6. View Mounted Filesystems

See what is mounted and where:
```bash
mount
```

Or use:
```bash
df -h
```

### 7. Check Permissions on Root Directories

View permissions of all root-level directories:
```bash
ls -ld /*
```

### 8. Create and Remove Test Files (as root or with sudo)

Create a test file in /tmp:
```bash
sudo touch /tmp/testfile.txt
```

Verify it exists:
```bash
ls -l /tmp/testfile.txt
```

Remove the test file:
```bash
sudo rm /tmp/testfile.txt
```

### 9. View Process Information via /proc

List running processes:
```bash
ls /proc | head -20
```

View system memory info:
```bash
cat /proc/meminfo
```

View CPU info:
```bash
cat /proc/cpuinfo
```

### 10. Understand Filesystem Hierarchy

Read the manual for filesystem hierarchy:
```bash
man hier
```

Press `q` to exit the manual.

