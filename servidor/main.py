from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime, timedelta
from collections import deque
import time
import requests

app = Flask(__name__)

# Store the last 100 measurements in memory
MAX_MEASUREMENTS = 100
measurements_buffer = deque(maxlen=MAX_MEASUREMENTS)

SERVER_URL = "http://78.12.70.74:5000/api/submit"

def read_sensor():
    # Replace with your real sensor reading code
    import random
    return random.uniform(10, 800)

@app.route("/")
def main():
    name = "User"
    return render_template('index.html', person=name)

@app.route("/about")
def about():
    return "About page coming soon"

@app.route("/monitor")
def monitor():
    # Use the in-memory buffer
    measurements = list(measurements_buffer)
    return render_template(
        'monitor.html',
        measurements=measurements,
        measurements_json=json.dumps(measurements)
    )

@app.route("/api/measurements")
def api_measurements():
    return jsonify(list(measurements_buffer))

@app.route("/hola_mundo")
def hola_mundo():
    return "¡Hola, mundo!"

@app.route("/api/submit", methods=["POST"])
def api_submit():
    data = request.get_json()
    try:
        distance = float(data["distance"])
    except (KeyError, ValueError, TypeError):
        return jsonify({"status": "error", "message": "Invalid data"}), 400

    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    if distance > 700:
        status = "Error"
    elif distance < 20:
        status = "Warning"
    else:
        status = "Normal"
    measurement = {
        "timestamp": timestamp,
        "distance": distance,
        "status": status
    }
    measurements_buffer.append(measurement)
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

while True:
    value = read_sensor()
    try:
        requests.post(SERVER_URL, json={"distance": value}, timeout=2)
    except Exception as e:
        print("Failed to send:", e)
    time.sleep(1)