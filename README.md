# 🛡️ RedHawk: Real-Time Threat Detection Platform

RedHawk is a real-time threat detection and alerting platform built using **Python**, **Go**, and the **ELK Stack (Elasticsearch, Logstash, Kibana/Grafana)**. It parses and analyzes logs (SSH, Suricata, Zeek), detects suspicious activity like brute-force attacks, and visualizes alerts on a dashboard.

---

## 📌 Key Features

- 🔍 SSH/Suricata/Zeek log parsing
- ⚙️ Log normalization to JSON
- 🧠 Go-based rule engine for threat detection
- 📧 Email alert integration
- 📊 Grafana-based alert dashboards
- 📂 Supports simulated or real log files
- 🔄 Easily extendable rules with YAML

---


## 🚀 How It Works

1. 📥 **Ingest logs** → `ingest/ssh_parser.py`
2. 🔄 **Normalize** → `normalize/json_normalizer.py`
3. 🧠 **Detect threats** → `engine/main.go` using rules
4. ⚠️ **Alerts generated** → `output/alerts.json`
5. 📤 **Send to Elasticsearch** → `alerts/upload_elastic.py`
6. 📊 **Visualize in Grafana** → Real-time dashboards

---

## 🔧 Prerequisites

- Python 3.8+
- Go 1.20+
- Docker & Docker Compose (for ELK + Grafana)
- Elasticsearch running on `localhost:9200`
- Grafana running on `localhost:3000`

---

## 🧪 Getting Started

📖 See the [`RUN_GUIDE.md`](./RUN_GUIDE.md) file for full instructions on how to:

- Generate logs
- Detect threats
- Push alerts to Elasticsearch
- Visualize with Grafana

---

## 📫 Contact

Built with 💻 by [Jenish Patel](https://github.com/jenishpatel7)

---

## 📜 License

MIT License – Use it freely for learning and research.
