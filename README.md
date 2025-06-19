# SensorHub - Remote Sensor Monitoring

This project allows you to remotely monitor sensor data (such as distance measurements) from a Raspberry Pi, sending the data to a Flask server hosted on AWS. The server provides a real-time dashboard with a chart and table of recent sensor readings.

---

## How It Works

- **Raspberry Pi**: Reads sensor values (e.g., from an ultrasonic sensor) and sends them every second to the Flask server using HTTP POST requests.
- **Flask Server (AWS)**: Receives sensor data, stores the latest 100 measurements in memory, and serves a web dashboard.
- **Web Dashboard**: Shows a live-updating chart and table of recent sensor readings, refreshing automatically every 5 seconds.

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd emmbebed_sistem/servidor
```

### 2. Create and Activate a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip3 install flask 
pip3 install requests
```

### 4. Configure and Run the Flask Server (on AWS)

Edit `main.py` if needed, then start the server:

```bash
python main.py
```

The server will listen on port 5000 by default.

### 5. Configure the Raspberry Pi Sensor Script

On your Raspberry Pi, use the following script (replace `<YOUR_AWS_SERVER_IP_OR_DOMAIN>` with your AWS server's public IP or DNS):

```python
import time
import requests

SERVER_URL = "http://<YOUR_AWS_SERVER_IP_OR_DOMAIN>:5000/api/submit"

def read_sensor():
    # Replace with your real sensor reading code
    import random
    return random.uniform(10, 800)

while True:
    value = read_sensor()
    try:
        requests.post(SERVER_URL, json={"distance": value}, timeout=2)
    except Exception as e:
        print("Failed to send:", e)
    time.sleep(1)
```

### 6. Access the Dashboard

Open your browser and go to:

```
http://<YOUR_AWS_SERVER_IP_OR_DOMAIN>:5000/monitor
```

You will see a live chart and table of the latest sensor readings.

---

## Notes

- The server stores only the latest 100 measurements in memory. For persistent storage, consider integrating a database.
- The dashboard updates automatically every 5 seconds.
- data is saved to a `.txt` file
- you must run first the server, then you run measurement code.

---

## Requirements

- Python 3.x
- Flask
- requests

---
