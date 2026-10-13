
## Exercise 1 — Bash

### Step 1: Create a practice directory

```
mkdir -p ~/projects/bash_practice
cd ~/projects/bash_practice
pwd
```

Expected directory:

```
/home/drishti/projects/bash_practice
```

Your username or path may differ.

### Step 2: Create your first script

Open a file using Nano:

```
nano hello.sh
```

Enter this content:

```
#!/bin/bash

echo "Hello, Linux!"
echo "Current user:"
whoami

echo "Current directory:"
pwd

echo "Current date and time:"
date
```

Save the file in Nano:

1. Press `Ctrl + O`.
    
2. Press `Enter`.
    
3. Press `Ctrl + X`.
    

### Step 3: Execute the script

First, run it using Bash:

```
bash hello.sh
```

Now grant execute permission:

```
chmod +x hello.sh
```

Execute it directly:

```
./hello.sh
```

Compare the two execution methods.

### Step 4: Create a script with variables and input

Create a new file:

```
nano user_info.sh
```

Enter:

```
#!/bin/bash

read -p "Enter your name: " name
read -p "Enter your age: " age

echo "Name: $name"
echo "Age: $age"
```

Run it:

```
bash user_info.sh
```

Enter your name and age when prompted.

### Step 5: Practice conditions and loops

Create a script:

```
nano practice.sh
```

Enter:

```
#!/bin/bash

read -p "Enter a number: " number

if [ "$number" -gt 10 ]; then
    echo "Greater than 10"
else
    echo "10 or less"
fi

for i in 1 2 3 4 5
do
    echo "$i"
done
```

Execute it:

```
bash practice.sh
```

Try different numbers to see how the condition behaves.

## Exercise 2 — SSH

We'll first practice SSH locally on your Ubuntu WSL environment. This lets you understand SSH without needing a second computer.

### Step 1: Check whether the SSH client exists

```
ssh -V
```

If the command displays an OpenSSH version, the client is installed.

### Step 2: Check the SSH server package

```
dpkg -l openssh-server
```

If it is not installed, install it:

```
sudo apt update
sudo apt install openssh-server
```

### Step 3: Start the SSH server

```
sudo service ssh start
```

Check its status:

```
sudo service ssh status
```

If your WSL environment uses systemd, you can also use:

```
sudo systemctl status ssh
```

### Step 4: Connect to your own machine

First, find your username:

```
whoami
```

Then connect locally:

```
ssh your_username@localhost
```

Replace `your_username` with the username returned by `whoami`.

If prompted to trust the host key, verify that the connection is to your own local machine before accepting it. Enter your Linux account password if requested.

Once connected, run:

```
whoami
pwd
hostname
```

You are now using a remote shell session, even though the SSH connection is to the same computer.

Exit the SSH session:

```
exit
```

If this step fails: WSL service configuration, SSH server installation, or port configuration may need attention. Do not change firewall settings or expose SSH to the internet just to complete this exercise.

### Step 5: Generate an SSH key pair

```
ssh-keygen -t ed25519
```

For a beginner exercise, accept the default file location. You can set a passphrase to protect your private key.

List your SSH files:

```
ls -la ~/.ssh
```

Typically, you will see:

- `id_ed25519` — Private key; keep it secret.
    
- `id_ed25519.pub` — Public key; safe to share with a trusted server administrator when needed.
    

If these files already exist, do not overwrite them unless you intend to replace the existing key pair.

## Exercise 3 — Cron

For this exercise, we'll create a script that records the current date and time in a log file. Then we'll schedule it to run automatically every minute.

### Step 1: Create a cron practice directory

```
mkdir -p ~/projects/cron_practice
cd ~/projects/cron_practice
```

### Step 2: Create the script

```
nano log_time.sh
```

Enter:

```
#!/bin/bash

date >> /home/drishti/projects/cron_practice/time.log
```

If your Linux username is not `drishti`, replace `/home/drishti` with the correct home directory. You can find it with:

```
echo "$HOME"
```

Save the file and grant execute permission:

```
chmod +x ~/projects/cron_practice/log_time.sh
```

Test the script manually:

```
bash ~/projects/cron_practice/log_time.sh
```

View the log:

```
cat ~/projects/cron_practice/time.log
```

You should see a date and time.

### Step 3: Open your crontab

```
crontab -e
```

If asked to choose an editor, select Nano if that option is available.

Add the following line at the bottom, replacing the username in the path if needed:

```
* * * * * /home/drishti/projects/cron_practice/log_time.sh
```

Save and exit.

This schedules the script to run once every minute.

### Step 4: Verify the cron job

List your scheduled jobs:

```
crontab -l
```

Wait one or two minutes, then check the log:

```
cat ~/projects/cron_practice/time.log
```

You should see additional timestamps. Cron executes tasks according to the machine's configured time zone.

If nothing appears, check the service:

```
sudo service cron status
```

On WSL, cron may need to be started manually, depending on your configuration:

```
sudo service cron start
```

### Step 5: Remove the test job

Open the crontab:

```
crontab -e
```

Delete only the line you added, then save and exit. This is preferable to `crontab -r`, which deletes every cron job belonging to your user.

# Final revision

|Topic|What you should be able to do|
|---|---|
|Bash|Write and execute scripts, use variables, take input, apply conditions, and use loops|
|SSH|Understand client/server connections, connect locally, check SSH services, and generate SSH keys|
|Cron|Understand cron expressions, schedule scripts, inspect logs, and manage scheduled jobs|


