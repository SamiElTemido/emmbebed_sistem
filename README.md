# Ultrasonic Distance Sensor Project

This project uses a Raspberry Pi to measure distances using an HC-SR04 ultrasonic sensor and logs the measurements to a file.

## Hardware Requirements

- Raspberry Pi
- HC-SR04 Ultrasonic Sensor
- Connecting wires
- GPIO pins used:
  - TRIG: GPIO 23
  - ECHO: GPIO 24

## Software Setup

1. Install required Python packages:
```bash
pip install RPi.GPIO
```

2. Clone this repository:
```bash
git clone https://github.com/SamiElTemido/emmbebed_sistem.git
```

## Usage

Run the sensor measurement script:
```bash
python get_sensor_value.py
```

The script will:
- Take distance measurements every second
- Save measurements to `distancias.txt`
- Display readings in the console
- Stop measuring when you press Ctrl+C

## File Description

- `get_sensor_value.py`: Main script for sensor measurements
- `distancias.txt`: Log file containing recorded distances in centimeters
- `.gitignore`: Git configuration to ignore certain files

## Notes

- Measurements are recorded in centimeters with 2 decimal places
- The sensor reading interval is set to 1 second
- Data is continuously appended to the log file
