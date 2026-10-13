## 3. Cron (Job Scheduling)

### What is Cron?

Cron is a Linux scheduling service that automatically executes commands or scripts at specified times.

A scheduled task is called a cron job.

Cron is useful for:

- Running scripts automatically.
    
- Creating scheduled backups.
    
- Cleaning temporary files.
    
- Generating reports.
    
- Running maintenance tasks at regular intervals.

For example, you can schedule a script to execute every day at 8:00 AM without manually running it.

### What is crontab?

`crontab` stands for cron table. It contains the scheduled tasks for a user.

Important commands:

| Command           | Meaning                                             |
| ----------------- | --------------------------------------------------- |
| `crontab -l`      | Lists the current user's cron jobs                  |
| `crontab -e`      | Opens the current user's cron table for editing     |
| `crontab -r`      | Removes all cron jobs belonging to the current user |
| `sudo crontab -l` | Lists root's cron jobs                              |
| `sudo crontab -e` | Edits root's cron jobs                              |

Be careful with `crontab -r`: it removes the user's entire crontab, not just one selected job.

### Cron syntax

A cron entry consists of five time fields followed by the command to execute.

```
* * * * * command
```

The five fields represent:

|Field|Allowed values|Meaning|
|---|---|---|
|1|`0–59`|Minute|
|2|`0–23`|Hour|
|3|`1–31`|Day of the month|
|4|`1–12`|Month|
|5|`0–7`|Day of the week (Sunday can be `0` or `7`)|

### Common cron expressions

|Cron expression|Meaning|
|---|---|
|`* * * * *`|Every minute|
|`*/5 * * * *`|Every five minutes|
|`0 * * * *`|At the beginning of every hour|
|`0 8 * * *`|Every day at 8:00 AM|
|`30 18 * * *`|Every day at 6:30 PM|
|`0 9 * * 1`|Every Monday at 9:00 AM|
|`0 0 1 * *`|At midnight on the first day of every month|

Cron uses the machine's configured time zone. Also, day-of-month and day-of-week restrictions have special interaction rules when both are specified.

### Scheduling a Bash script

Suppose your script is located at:

```
/home/drishti/scripts/backup.sh
```

First, make it executable:

```
chmod +x /home/drishti/scripts/backup.sh
```

Open your crontab:

```
crontab -e
```

Add this line to run the script every day at 8:00 AM:

```
0 8 * * * /home/drishti/scripts/backup.sh
```

Use the script's absolute path rather than a relative path because cron jobs may run with a different working directory from your interactive terminal.

### Logging cron output

You can redirect output to a log file:

```
*/5 * * * * /home/drishti/scripts/backup.sh >> /home/drishti/cron.log 2>&1
```

Here:

- `>>` appends output to the log file.
    
- `2>&1` sends error output to the same destination as standard output.
    

This makes it easier to inspect the results of scheduled tasks.

### Cron service commands

On Ubuntu systems using systemd:

```
sudo systemctl status cron
sudo systemctl start cron
sudo systemctl stop cron
sudo systemctl enable cron
```

These commands check, start, stop, and enable the cron service. If cron is not installed, you may need:

```
sudo apt install cron
```

### Cron Job Management Commands

**1. Edit or Create a Cron Job**
```bash
crontab -e
```

**2. List Current Cron Jobs**
```bash
crontab -l
```

**3. Remove All Cron Jobs**
```bash
crontab -r
```

**4. Start the Cron Service**
```bash
sudo service cron start
```

**5. Stop the Cron Service**
```bash
sudo service cron stop
```

**6. Restart the Cron Service**
```bash
sudo service cron restart
```

**7. Check Cron Service Status**
```bash
sudo service cron status
```

**8. View Cron Logs (if available)**
```bash
sudo journalctl -u cron --since "5 minutes ago"
```
or
```bash
sudo grep CRON /var/log/auth.log
```

