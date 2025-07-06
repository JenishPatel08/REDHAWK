# ssh_parser.py
import re
import json

def parse_ssh_log(log_path):
    pattern = r'(?P<timestamp>\w+ \d+ \d+:\d+:\d+) .*sshd.*Failed password for (?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)'

    parsed_logs = []
    with open(log_path, 'r') as f:
        for line in f:
            match = re.search(pattern, line)
            if match:
                log_entry = {
                    "source": "SSH",
                    "event": "Failed login",
                    "timestamp": match.group("timestamp"),
                    "user": match.group("user"),
                    "ip": match.group("ip")
                }
                parsed_logs.append(log_entry)

    return parsed_logs

if __name__ == "__main__":
    logs = parse_ssh_log(r"./logs/auth.log")
  # sample log
    with open("./output/ssh_output.json", "w") as out:
        json.dump(logs, out, indent=4)
    print("✅ SSH logs parsed and saved to output/ssh_output.json")
