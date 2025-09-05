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


---

## ⚙️ Installation & Setup

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/system-health-monitor.git
   cd system-health-monitor
   
2. Install dependencies:

   ```bash
   pip install psutil

3.Run the monitor:

   ```bash
   python system_health.py


