# SSH (Secure Shell)

- **SSH (Secure Shell)** is a network protocol.
- It allows secure remote access to another computer over an unsecured network.
- It encrypts all data transferred between the client and the server.
- It prevents eavesdropping and connection hijacking.

**Key Components:**
*   **SSH Client:** The software on your local machine that initiates the connection.
*   **SSH Server:** The software on the remote machine that accepts the connection.
*   **Port:** SSH uses port 22 by default.

**Authentication Methods:**
*   **Password Authentication:** You enter the remote user's password.
*   **Key-Based Authentication:** You use a pair of cryptographic keys (public and private). This is more secure and convenient.

### 1. Basic Connection

Connect to a remote server using a username and IP address or hostname.

```bash
ssh username@remote_host_ip
```

Example:
```bash
ssh drishti@192.168.1.100
```

You will be prompted for the password if using password authentication.

### 2. Specifying a Port

If the SSH server runs on a non-default port.

```bash
ssh -p port_number username@remote_host_ip
```

Example:
```bash
ssh -p 2222 drishti@192.168.1.100
```

### 3. Generating SSH Keys

Create a public-private key pair for key-based authentication.

```bash
ssh-keygen -t rsa -b 4096
```

*   `-t rsa`: Specifies the type of key (RSA).
*   `-b 4096`: Specifies the number of bits in the key (4096 is secure).

Follow the prompts to save the key and optionally set a passphrase.

### 4. Copying Public Key to Remote Server

Transfer your public key to the remote server to enable key-based login.

```bash
ssh-copy-id username@remote_host_ip
```

Example:
```bash
ssh-copy-id drishti@192.168.1.100
```

You will need to enter the password once. After this, you can log in without a password if you didn't set a passphrase for the key.

### 5. Executing Remote Commands

Run a command on the remote server without opening an interactive shell.

```bash
ssh username@remote_host_ip "command"
```

Example:
```bash
ssh drishti@192.168.1.100 "ls -l /home/drishti"
```

### 6. Secure File Transfer (SCP)

Copy files securely between local and remote machines.

**Copy from local to remote:**
```bash
scp local_file_path username@remote_host_ip:remote_destination_path
```

Example:
```bash
scp ./report.txt drishti@192.168.1.100:/home/drishti/documents/
```

**Copy from remote to local:**
```bash
scp username@remote_host_ip:remote_file_path local_destination_path
```

Example:
```bash
scp drishti@192.168.1.100:/home/drishti/data.csv ./local_data/
```

### 7. SSH Configuration File

Simplify connections by storing host details in `~/.ssh/config`.

Edit the file:
```bash
nano ~/.ssh/config
```

Add entries like:
```
Host myserver
    HostName 192.168.1.100
    User drishti
    Port 22
    IdentityFile ~/.ssh/id_rsa
```

Now connect using:
```bash
ssh myserver
```

### SSH Management Commands - General Reference

**1. Connect to a Remote Server**
```bash
ssh username@ip_address
```

**2. Connect on a Specific Port**
```bash
ssh -p port_number username@ip_address
```

**3. Generate SSH Key Pair**
```bash
ssh-keygen -t rsa -b 4096
```

**4. Copy Public Key to Remote Server**
```bash
ssh-copy-id username@ip_address
```

**5. Execute a Remote Command Without Logging In**
```bash
ssh username@ip_address "command_to_run"
```

**6. Copy File from Local to Remote (SCP)**
```bash
scp local_file username@ip_address:/remote/path/
```

**7. Copy File from Remote to Local (SCP)**
```bash
scp username@ip_address:/remote/path/file.txt ./local_path/
```

**8. Start the SSH Service (on the server)**
```bash
sudo service ssh start
```

**9. Check SSH Service Status (on the server)**
```bash
sudo service ssh status
```

**10. Edit SSH Configuration (on the server)**
```bash
sudo nano /etc/ssh/sshd_config
```

### SSH Setup and Practice Commands - Local Practice

**1. Install OpenSSH Server**
```bash
sudo apt update
sudo apt install openssh-server
```

**2. Start the SSH Service**
```bash
sudo service ssh start
```

**3. Connect to Yourself (Localhost)**
```bash
ssh drishti@localhost
```

**4. Remote Command Execution**
```bash
ssh drishti@localhost "ls -l /home/drishti"
```

**5. File Transfer via SCP (Secure Copy Protocol)**
```bash
echo "SSH test content" > test_file.txt
scp test_file.txt drishti@localhost:/home/drishti/ssh_backup.txt
```

**6. Key-Based Authentication**
```bash
ssh-keygen -t rsa -b 4096
ssh-copy-id drishti@localhost
```

**7. Deleting Keys from the Local Machine**
```bash
rm ~/.ssh/id_rsa
rm ~/.ssh/id_rsa.pub
ssh-keygen -R localhost
nano ~/.ssh/authorized_keys
```