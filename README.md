# 🖥️ System Health Monitor

A lightweight Python script that monitors **CPU, memory, and disk usage** and logs alerts when usage crosses defined thresholds.  
Useful for **basic troubleshooting**, **system monitoring**, and as a learning project for IT/DevOps fundamentals.  

---

## 🚀 Features
- Monitor CPU, memory, and disk usage
- Configurable thresholds for alerts
- Timestamped logs saved to a file
- Runs continuously until stopped
- Simple and portable (only requires Python + psutil)

---

## 🛠️ Tech Stack
- **Language:** Python 3
- **Libraries:** [psutil](https://pypi.org/project/psutil/), datetime, time
- **Output:** Log file (`system_health.log`)

---

## 📂 Project Structure

```bash
system_health_monitor/
├── system_health.py # Main script
├── system_health.log # Log file (created after running)
└── README.md # Project documentation
```



## ⚙️ Installation & Setup

1. Clone the repository:
   ```
   git clone https://github.com/your-username/System-Health-Monitor.git
   cd System-Health-Monitor
   ```
2. Install dependencies:
   ```
   pip install psutil
   ```
3. Run the monitor:
   ```
   python system_health.py
   ```

## 📜 License

This project is licensed under the MIT License.
You are free to use, modify, and distribute this project.

## 📊 Sample Log Output

```
[2025-09-05 14:10:12] --- System monitor started ---
[2025-09-05 14:11:13] ALERT: CPU usage is high: 92.3%
[2025-09-05 14:11:13] ALERT: Memory usage is high: 85.0%
[2025-09-05 14:11:13] ALERT: Disk usage is high on '/': 91.2%
[2025-09-05 14:12:14] --- System monitor stopped ---
```
