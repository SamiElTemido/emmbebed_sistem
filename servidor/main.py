from flask import Flask, render_template, jsonify
import json
from datetime import datetime, timedelta

app = Flask(__name__)

@app.route("/")
def main():
    name = "User"
    return render_template('index.html', person=name)

@app.route("/about")
def about():
    return "About page coming soon"

@app.route("/monitor")
def monitor():
    # Read the last 50 measurements from the file
    filepath = '../distancias.txt'
    N = 50
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except Exception:
        lines = []

    # Get the last N valid float values
    distances = []
    for line in lines[-N:]:
        try:
            distances.append(float(line.strip()))
        except ValueError:
            continue

    # Generate timestamps (1 second apart, latest is now)
    now = datetime.now()
    measurements = []
    for i, distance in enumerate(reversed(distances)):
        timestamp = (now - timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S')
        # Simple status logic
        if distance > 700:
            status = "Error"
        elif distance < 20:
            status = "Warning"
        else:
            status = "Normal"
        measurements.append({
            "timestamp": timestamp,
            "distance": distance,
            "status": status
        })
    measurements = list(reversed(measurements))  # Oldest first

    return render_template(
        'monitor.html',
        measurements=measurements,
        measurements_json=json.dumps(measurements)
    )

@app.route("/api/measurements")
def api_measurements():
    filepath = '../distancias.txt'
    N = 50
    try:
        with open(filepath, 'r') as f:
            lines = f.readlines()
    except Exception:
        lines = []

    distances = []
    for line in lines[-N:]:
        try:
            distances.append(float(line.strip()))
        except ValueError:
            continue

    now = datetime.now()
    measurements = []
    for i, distance in enumerate(reversed(distances)):
        timestamp = (now - timedelta(seconds=i)).strftime('%Y-%m-%d %H:%M:%S')
        if distance > 700:
            status = "Error"
        elif distance < 20:
            status = "Warning"
        else:
            status = "Normal"
        measurements.append({
            "timestamp": timestamp,
            "distance": distance,
            "status": status
        })
    measurements = list(reversed(measurements))
    return jsonify(measurements)

if __name__ == "__main__":
    app.run(debug=True)