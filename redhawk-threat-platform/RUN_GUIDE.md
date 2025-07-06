# 🛠️ How to Run RedHawk Threat Detection Pipeline

This guide explains how to run the RedHawk threat detection platform from log creation to alert visualization.

---

## 📁 Project Workflow

1. **Create Sample SSH Logs**
2. **Parse SSH Logs**
3. **Normalize Parsed Logs**
4. **Run Threat Detection (Go)**
5. **Upload Alerts to Elasticsearch**
6. **View on Grafana Dashboard**

---

## 🧪 Step-by-Step Instructions

### 1️⃣ Generate Sample Log File

```bash
python ingest/log_creator.py
Output: logs/auth.log

2️⃣ Parse SSH Logs
python ingest/ssh_parser.py
Output: output/parsed_ssh_logs.json

3️⃣ Normalize Logs to JSON
python normalize/json_normalizer.py
Output: output/normalized_logs.json

4️⃣ Run Threat Detection Engine
go run engine/main.go
Output: output/alerts.json (Brute-force alerts)

5️⃣ Upload Alerts to Elasticsearch
python alerts/upload_elastic.py
Make sure Elasticsearch is running (http://localhost:9200)
Index: alerts

6️⃣ View Alerts in Grafana
Open your browser: http://localhost:3000
Use the RedHawk Threat Dashboard to see visualized alerts
Data source: Elasticsearch → alerts index

✅ Prerequisites
Python 3.x
Go 1.20+
Docker & Docker Compose (for ELK + Grafana)
Elasticsearch (localhost:9200)
Grafana (localhost:3000)

📦 Docker Compose (Optional)
To start ELK + Grafana:
docker-compose up -d





Happy Hunting! 🎯