import random
from datetime import datetime, timedelta
from pathlib import Path

# Generate 2000 log lines from 4 to 7 July 2025
start_date = datetime(2025, 7, 4, 0, 0, 0)
end_date = datetime(2025, 7, 7, 23, 59, 59)
delta = end_date - start_date

usernames = ['admin', 'jenish', 'root', 'user1', 'guest']
ips = ['212.254.1.' + str(i) for i in range(10, 50)]
log_lines = []

for _ in range(2000):
    random_seconds = random.randint(0, int(delta.total_seconds()))
    log_time = start_date + timedelta(seconds=random_seconds)
    line = log_time.strftime("Jul %d %H:%M:%S") + f" kali sshd[{random.randint(1000,9999)}]: Failed password for {random.choice(usernames)} from {random.choice(ips)} port {random.randint(2000, 65000)} ssh2"
    log_lines.append(line)

# Save to file
output_path = "./logs/auth.log"
with open(output_path, "w") as f:
    f.write("\n".join(log_lines))

output_path  # Return the path for user to download or use
