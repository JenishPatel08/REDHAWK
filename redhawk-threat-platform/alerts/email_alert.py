import smtplib
from email.mime.text import MIMEText
import json

# === CONFIGURATION ===
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
SENDER_EMAIL = "your_mail@gmail.com"
SENDER_PASSWORD = "password"
RECEIVER_EMAIL = "reciever_mail@gmail.com"

# === FUNCTION ===
def send_email_alert(alert_data):
    subject = "🚨 RedHawk Alert: Threat Detected"
    body = json.dumps(alert_data, indent=4)

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, msg.as_string())
        print("✅ Alert sent via email!")

# === EXAMPLE USAGE ===
if __name__ == "__main__":
    with open("output/alerts.json", "r") as f:
        alerts = json.load(f)

    for alert in alerts:
        send_email_alert(alert)
