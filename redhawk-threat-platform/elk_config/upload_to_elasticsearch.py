import json
import requests
from datetime import datetime

ES_URL = "http://localhost:9200/alerts/_doc"

def load_and_upload(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)

    for entry in data:
        # Fix the timestamp format
        try:
            # If already in correct format, skip this
            if 'T' not in entry['timestamp']:
                # Convert from "YYYY-MM-DD HH:MM:SS" to "YYYY-MM-DDTHH:MM:SSZ"
                dt = datetime.strptime(entry['timestamp'], "%Y-%m-%d %H:%M:%S")
                entry['timestamp'] = dt.isoformat() + "Z"
        except Exception as e:
            print(f"Timestamp format issue: {entry['timestamp']} - {e}")
            continue

        # Upload to Elasticsearch
        res = requests.post(ES_URL, json=entry)
        if res.status_code not in [200, 201]:
            print(f"❌ Failed to upload: {res.text}")
        else:
            print(f"✅ Uploaded alert: {entry['ip_address']} at {entry['timestamp']}")

if __name__ == "__main__":
    load_and_upload("output/alerts.json")
