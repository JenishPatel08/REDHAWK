import json
from datetime import datetime

def normalize_ssh_logs(input_path, output_path):
    with open(input_path, 'r') as infile:
        ssh_logs = json.load(infile)

    normalized = []
    for entry in ssh_logs:
        norm = {
            "timestamp": convert_timestamp(entry["timestamp"]),
            "source": entry["source"],
            "event_type": "authentication_failure",
            "username": entry["user"],
            "ip_address": entry["ip"],
            "severity": "medium"
        }
        normalized.append(norm)

    with open(output_path, 'w') as outfile:
        json.dump(normalized, outfile, indent=4)
    print("✅ Logs normalized and saved to:", output_path)

def convert_timestamp(ts):
    try:
        return datetime.strptime(ts, "%b %d %H:%M:%S").replace(year=2025).strftime("%Y-%m-%d %H:%M:%S")
    except:
        return ts  # fallback if it fails

if __name__ == "__main__":
    normalize_ssh_logs(
        "./output/ssh_output.json",
        "./output/normalized_logs.json"
    )
