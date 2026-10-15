## Core Command Categories

### 1. File & Directory Navigation
| Command | Description             | Example            |
| ------- | ----------------------- | ------------------ |
| `pwd`   | Print working directory | `pwd`              |
| `ls`    | List directory contents | `ls -la`           |
| `cd`    | Change directory        | `cd /home/drishti` |
| `mkdir` | Create directory        | `mkdir projects`   |
| `rmdir` | Remove empty directory  | `rmdir old_folder` |

### 2. File Operations
| Command | Description            | Example                  |
| ------- | ---------------------- | ------------------------ |
| `touch` | Create empty file      | `touch notes.txt`        |
| `cp`    | Copy files/directories | `cp file1.txt file2.txt` |
| `mv`    | Move/rename files      | `mv old.txt new.txt`     |
| `rm`    | Remove files           | `rm unwanted.txt`        |
| `cat`   | Display file content   | `cat readme.md`          |
| `less`  | View file page by page | `less largefile.log`     |
| `head`  | Show first lines       | `head -n 10 data.csv`    |
| `tail`  | Show last lines        | `tail -n 5 error.log`    |

### 3. File Permissions & Ownership
| Command | Description             | Example                        |
| ------- | ----------------------- | ------------------------------ |
| `chmod` | Change file permissions | `chmod 755 script.sh`          |
| `chown` | Change file owner       | `chown drishti:staff file.txt` |
| `umask` | Set default permissions | `umask 022`                    |

### 4. User & Group Management
| Command    | Description         | Example                    |
| ---------- | ------------------- | -------------------------- |
| `whoami`   | Show current user   | `whoami`                   |
| `id`       | Show user/group IDs | `id drishti`               |
| `adduser`  | Add new user        | `sudo adduser student1`    |
| `deluser`  | Delete user         | `sudo deluser student1`    |
| `addgroup` | Add new group       | `sudo addgroup developers` |
| `delgroup` | Delete group        | `sudo delgroup temp_group` |
| `usermod`  | Modify user account | `usermod -aG sudo drishti` |

### 5. Package Management (Ubuntu/Debian)
| Command       | Description         | Example                |
| ------------- | ------------------- | ---------------------- |
| `apt update`  | Update package list | `sudo apt update`      |
| `apt install` | Install package     | `sudo apt install git` |
| `apt remove`  | Remove package      | `sudo apt remove vim`  |
| `apt search`  | Search packages     | `apt search python3`   |

### 6. System Information & Monitoring
| Command    | Description            | Example    |
| ---------- | ---------------------- | ---------- |
| `uname -a` | System information     | `uname -a` |
| `df -h`    | Disk space usage       | `df -h`    |
| `free -h`  | Memory usage           | `free -h`  |
| `top`      | Process monitor        | `top`      |
| `ps aux`   | List running processes | `ps aux`   |
| `uptime`   | System uptime          | `uptime`   |

### 7. Text Processing & Search
| Command | Description          | Example                   |
| ------- | -------------------- | ------------------------- |
| `grep`  | Search text patterns | `grep "error" log.txt`    |
| `find`  | Find files           | `find /home -name "*.py"` |
| `wc`    | Count lines/words    | `wc -l file.txt`          |
| `sort`  | Sort file content    | `sort names.txt`          |
| `uniq`  | Remove duplicates    | `sort file.txt `\|` uniq` |

### 8. Network & SSH
| Command    | Description             | Example                        |
| ---------- | ----------------------- | ------------------------------ |
| `ssh`      | Secure shell connection | `ssh drishti@server.com`       |
| `scp`      | Secure copy             | `scp file.txt user@host:/path` |
| `ping`     | Test connectivity       | `ping google.com`              |
| `ifconfig` | Network interfaces      | `ifconfig`                     |
| `netstat`  | Network statistics      | `netstat -tuln`                |

### 9. Process Management
| Command | Description | Example |
|---------|-------------|---------|
| `kill` | Terminate process | `kill 1234` |
| `killall` | Kill by name | `killall firefox` |
| `bg` | Resume in background | `bg %1` |
| `fg` | Bring to foreground | `fg %1` |
| `jobs` | List background jobs | `jobs` |

### 10. Archive & Compression
| Command | Description | Example |
|---------|-------------|---------|
| `tar` | Archive files | `tar -czf backup.tar.gz folder/` |
| `gzip` | Compress file | `gzip file.txt` |
| `unzip` | Extract zip | `unzip archive.zip` |

### 11. Cron & Scheduling
| Command      | Description            | Example                           |
| ------------ | ---------------------- | --------------------------------- |
| `crontab -e` | Edit cron jobs         | `crontab -e`                      |
| `crontab -l` | List cron jobs         | `crontab -l`                      |
| `at`         | Schedule one-time task | `echo "cmd" `\|` at now + 1 hour` |

### 12. Help & Documentation
| Command | Description | Example |
|---------|-------------|---------|
| `man` | Manual pages | `man ls` |
| `--help` | Command help | `ls --help` |
| `whatis` | Brief description | `whatis grep` |
| `which` | Find command path | `which python3` |
