import psutil
import time
from datetime import datetime

# --- Configuration ---
LOG_FILE = "system_health.log"
CPU_THRESHOLD = 80.0  # in percentage
MEMORY_THRESHOLD = 80.0  # in percentage
DISK_THRESHOLD = 90.0  # in percentage

def log_data(message):
    """Logs a message to the specified log file."""
    with open(LOG_FILE, "a") as f:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"[{timestamp}] {message}\n")

def check_resources():
    """Checks CPU, memory, and disk usage and logs alerts if thresholds are exceeded."""
    
    # Check CPU usage
    cpu_usage = psutil.cpu_percent(interval=1)
    if cpu_usage > CPU_THRESHOLD:
        log_data(f"ALERT: CPU usage is high: {cpu_usage}%")
    
    # Check Memory usage
    memory = psutil.virtual_memory()
    memory_usage = memory.percent
    if memory_usage > MEMORY_THRESHOLD:
        log_data(f"ALERT: Memory usage is high: {memory_usage}%")
    
    # Check Disk usage (for the root partition)
    disk = psutil.disk_usage('/')
    disk_usage = disk.percent
    if disk_usage > DISK_THRESHOLD:
        log_data(f"ALERT: Disk usage is high on '/': {disk_usage}%")

def main():
    print("Starting system health monitor. Press Ctrl+C to exit.")
    log_data("--- System monitor started ---")
    try:
        while True:
            check_resources()
            time.sleep(60)  # wait 60s before checking again
    except KeyboardInterrupt:
        log_data("--- System monitor stopped ---")
        print("Monitor stopped.")

if __name__ == "__main__":
    main()
