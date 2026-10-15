## Practice Exercises

### Exercise 1: Navigation & File Creation
```bash
# Check current location
pwd

# List all files including hidden ones
ls -la

# Create a directory structure
mkdir -p linux_practice/scripts

# Navigate into it
cd linux_practice

# Create multiple files
touch script1.sh script2.sh notes.txt

# Verify creation
ls -l
```

### Exercise 2: File Operations
```bash
# Copy a file
cp script1.sh script1_backup.sh

# Rename a file
mv notes.txt study_notes.txt

# View file content (create content first)
echo "#!/bin/bash" > script1.sh
echo "echo Hello World" >> script1.sh
cat script1.sh

# Show first 3 lines
head -n 3 script1.sh

# Delete backup
rm script1_backup.sh
```

### Exercise 3: Permissions Practice
```bash
# Check current permissions
ls -l script1.sh

# Make script executable
chmod +x script1.sh

# Set specific permissions (read/write for owner, read for others)
chmod 644 study_notes.txt

# Verify changes
ls -l

# Check default umask
umask

# Temporarily change umask
umask 027
touch test_file.txt
ls -l test_file.txt
```

### Exercise 4: User & Group Management
```bash
# Check your user info
whoami
id

# View passwd file entries
grep drishti /etc/passwd

# View group memberships
groups

# Create a test group (requires sudo)
sudo addgroup testgroup

# Add yourself to the group
sudo usermod -aG testgroup drishti

# Verify
groups drishti

# Clean up
sudo delgroup testgroup
```

### Exercise 5: Package Management
```bash
# Update package lists
sudo apt update

# Search for a package
apt search curl

# Check if package is installed
dpkg -l | grep git

# Install a small utility
sudo apt install tree

# Use it
tree ~/linux_practice

# Remove it
sudo apt remove tree
```

### Exercise 6: Text Processing
```bash
# Create sample data
echo -e "apple\nbanana\napple\ncherry\nbanana" > fruits.txt

# Search for pattern
grep "apple" fruits.txt

# Count occurrences
grep -c "banana" fruits.txt

# Sort and remove duplicates
sort fruits.txt | uniq

# Count total lines
wc -l fruits.txt

# Find all .txt files in home
find ~ -name "*.txt" -type f
```

### Exercise 7: Process Management
```bash
# Start a background process
sleep 100 &

# List background jobs
jobs

# Bring to foreground
fg %1

# Stop it (Ctrl+Z)
# Then kill it
kill %1

# List all processes
ps aux | grep sleep

# Check system resources
top
# Press 'q' to exit
```

### Exercise 8: System Information
```bash
# Check disk usage
df -h

# Check memory
free -h

# System info
uname -a

# Uptime
uptime

# Check logged in users
who
```

### Exercise 9: SSH Basics (Local Testing)
```bash
# Install OpenSSH server
sudo apt install openssh-server

# Start the service
sudo systemctl start ssh

# Check status
sudo systemctl status ssh

# Connect to localhost
ssh drishti@localhost

# Exit SSH session
exit

# Generate SSH key pair
ssh-keygen -t rsa -b 4096

# View public key
cat ~/.ssh/id_rsa.pub
```

### Exercise 10: Cron Job Setup
```bash
# Create a simple script
echo '#!/bin/bash' > ~/backup_script.sh
echo 'echo "Backup ran at $(date)" >> ~/backup_log.txt' >> ~/backup_script.sh
chmod +x ~/backup_script.sh

# Edit crontab
crontab -e

# Add this line to run every day at 2 AM:
# 0 2 * * * /home/drishti/backup_script.sh

# List cron jobs
crontab -l

# Test the script manually
~/backup_script.sh
cat ~/backup_log.txt
```

### Exercise 11: Archives
```bash
# Create archive
tar -czf practice_backup.tar.gz linux_practice/

# List archive contents
tar -tzf practice_backup.tar.gz

# Extract to different location
mkdir extracted
tar -xzf practice_backup.tar.gz -C extracted/

# Verify
ls extracted/linux_practice/
```

### Exercise 12: Help & Discovery
```bash
# Get manual for ls
man ls
# Press 'q' to exit

# Quick help
ls --help

# Find where a command is located
which python3

# Get brief description
whatis chmod

# Search commands by keyword
apropos permission
```

---

## Quick Reference Tips

**File Permission Numbers:**
- 4 = Read (r)
- 2 = Write (w)
- 1 = Execute (x)
- 7 = rwx (4+2+1)
- 6 = rw- (4+2)
- 5 = r-x (4+1)

**Common Flags:**
- `-l` = Long listing format
- `-a` = Show all files (including hidden)
- `-h` = Human-readable sizes
- `-r` = Recursive
- `-v` = Verbose

**Navigation Shortcuts:**
- `~` = Home directory
- `.` = Current directory
- `..` = Parent directory
- `-` = Previous directory (`cd -`)