
# Linux Users and Groups

## Core Concepts

**Users** are identities that can log in and access the system. Each user has a unique ID (UID).

**Groups** are collections of users. They simplify permission management. Each group has a unique ID (GID).

Think of it like this:
- Users = individual employees
- Groups = departments or teams
- Permissions = what each person/team can access


## Types of Users

### 1. Root User (Superuser)
- UID = 0
- Has complete system control
- Can do anything: install software, modify files, manage users
- Dangerous if misused

### 2. System Users
- UID typically 1-999
- Created automatically for services (apache, mysql, etc.)
- Cannot log in normally
- Run background processes

### 3. Regular Users
- UID starts from 1000
- Created for human users
- Limited permissions by default
- Need sudo for administrative tasks


## Key Files

Linux stores user/group info in specific files:

### `/etc/passwd`
Stores user account information.

Format: `username:password_placeholder:UID:GID:description:home_directory:shell`

Example:
```
drishti:x:1001:1001:hbruh:/home/drishti:/bin/bash
```

### `/etc/shadow`
Stores encrypted passwords securely.
- Only readable by root
- Contains password hashes and expiry info

### `/etc/group`
Stores group information.

Format: `group_name:password_placeholder:GID:user_list`

Example:
```
developers:x:1002:hbruh,john,jane
```

## Essential Commands

### Managing Users

**Create a user:**
```bash
sudo adduser user1
```
This creates home directory, sets password, and asks for details.

**Delete a user:**
```bash
sudo deluser user1
```
Add `--remove-home` to delete their home folder too.

**Modify user:**
```bash
sudo usermod -aG developers user1
```
Adds user1 to the "developers" group without removing existing groups.

**Change password:**
```bash
sudo passwd drishti
```

**View current user:**
```bash
whoami
```

**List all users:**
```bash
cat /etc/passwd
```


### Managing Groups

**Create a group:**
```bash
sudo addgroup developers
```

**Delete a group:**
```bash
sudo delgroup developers
```

**Add user to group:**
```bash
sudo usermod -aG developers userx
```

**Remove user from group:**
```bash
sudo gpasswd -d userx developers
```

**View user's groups:**
```bash
groups userx
```

**List all groups:**
```bash
cat /etc/group
```

## Understanding Permissions

Every file has three permission levels:
- **Owner** (user)
- **Group**
- **Others** (everyone else)

Each level can have:
- **r** = read
- **w** = write
- **x** = execute

Example:
```
-rwxr-xr-- 1 userx developers 4096 Oct 8 10:00 script.py
```

Breaking it down:
- Owner (hbruh): read, write, execute
- Group (developers): read, execute
- Others: read only


## Practical Example

Let's say you're setting up a project team:

**Step 1:** Create a group for your team
```bash
sudo addgroup project_alpha
```

**Step 2:** Add team members
```bash
sudo usermod -aG project_alpha hbruh
sudo usermod -aG project_alpha john
sudo usermod -aG project_alpha jane
```

**Step 3:** Create shared directory
```bash
sudo mkdir /opt/project_alpha
sudo chown :project_alpha /opt/project_alpha
sudo chmod 775 /opt/project_alpha
```

Now all team members can read, write, and execute files in that directory.

## Important Notes

- Always use `sudo` for user/group management
- The `-a` flag with `usermod` is crucial—it appends to existing groups instead of replacing them
- Changes to group membership require logout/login to take effect
- Use `newgrp groupname` to switch to a new group in current session
- Never share the root password—use sudo instead

## Quick Reference

| Task | Command |
|------|---------|
| Create user | `sudo adduser username` |
| Delete user | `sudo deluser username` |
| Create group | `sudo addgroup groupname` |
| Add user to group | `sudo usermod -aG groupname username` |
| View groups | `groups username` |
| Change ownership | `sudo chown user:group filename` |
| Change permissions | `chmod 755 filename` |
