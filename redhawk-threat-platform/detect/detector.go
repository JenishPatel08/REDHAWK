package main

import (
    "encoding/json"
    "fmt"
    "os"
)

type LogEntry struct {
    Timestamp  string `json:"timestamp"`
    Source     string `json:"source"`
    EventType  string `json:"event_type"`
    Username   string `json:"username"`
    IPAddress  string `json:"ip_address"`
    Severity   string `json:"severity"`
}

type Alert struct {
    Timestamp string `json:"timestamp"`
    IP        string `json:"ip_address"`
    Username  string `json:"username"`
    Reason    string `json:"reason"`
    Severity  string `json:"severity"`
}

func main() {
    data, err := os.ReadFile("./output/normalized_logs.json")
    if err != nil {
        panic(err)
    }

    var logs []LogEntry
    json.Unmarshal(data, &logs)

    bruteCount := make(map[string]int)
    alreadyAlerted := make(map[string]bool)
    alerts := []Alert{}

    for _, log := range logs {
        key := log.IPAddress + "_" + log.Username
        bruteCount[key]++

        if bruteCount[key] >= 5 && !alreadyAlerted[key] {
            alert := Alert{
                Timestamp: log.Timestamp,
                IP:        log.IPAddress,
                Username:  log.Username,
                Reason:    "Multiple failed login attempts",
                Severity:  "high",
            }
            alerts = append(alerts, alert)
            alreadyAlerted[key] = true
        }
    }

    out, _ := json.MarshalIndent(alerts, "", "  ")
    os.WriteFile("C:/Users/jenish/redhawk-threat-platform/output/alerts.json", out, 0644)

    fmt.Println("✅ Threat detection complete. Alerts written to output/alerts.json")
}
