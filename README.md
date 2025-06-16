# Ultrasonic Distance Sensor Project

This project lets you measure distances with a Raspberry Pi and an HC-SR04 ultrasonic sensor. The measurements are saved to a file and can be viewed in real time on a web dashboard.

## Project Structure

- `get_sensor_value.py`: Script that reads the sensor and saves distances to `distancias.txt`.
- `distancias.txt`: File where all distance measurements are stored (in centimeters).
- `servidor/`: Web server (Flask) to visualize the measurements.
  - `main.py`: Flask app with routes for the dashboard and API.
  - `static/`: CSS styles.
  - `templates/`: HTML templates for the web pages.

## How It Works

1. The sensor script (`get_sensor_value.py`) runs on your Raspberry Pi.
2. Every second, it measures the distance and appends the value to `distancias.txt`.
3. The Flask server (`servidor/main.py`) reads the latest measurements and shows them on a web dashboard at `/monitor`.
4. You can see a live chart and table of recent measurements in your browser.

## Hardware Needed

- Raspberry Pi
- HC-SR04 Ultrasonic Sensor
- Jumper wires
- GPIO pins used:
  - TRIG: GPIO 23
  - ECHO: GPIO 24

## Setup

1. Install Python and Flask on your Raspberry Pi.
2. Install the GPIO library:
    ```bash
    pip install RPi.GPIO
    ```
3. (Optional) Install Flask if not already installed:
    ```bash
    pip install flask
    ```
4. Clone this repository:
    ```bash
    git clone https://github.com/SamiElTemido/emmbebed_sistem.git
    cd emmbebed_sistem
    ```

## Usage

1. **Start the sensor script** (this will keep running and saving data):
    ```bash
    python get_sensor_value.py
    ```
2. **Start the web server** in another terminal:
    ```bash
    cd servidor
    flask --app main run
    ```
3. **Open your browser** and go to [http://localhost:5000/monitor](http://localhost:5000/monitor) to see the dashboard.

## Notes

- Measurements are in centimeters, with 3 decimal places.
- The dashboard updates automatically every 2 seconds.
- Only the latest 50 measurements are shown on the dashboard.
- To stop the sensor script, press `Ctrl+C`.

---
If you have any issues, check your wiring and make sure the sensor is connected to the correct GPIO
