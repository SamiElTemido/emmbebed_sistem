from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def main():
    name ="Pepe"
    return render_template('index.html', person=name)  # or pass a name here

@app.route("/about")
def about():
    return "About page coming soon"

@app.route("/monitor")
def monitor():
    # Sample data - Replace with real data
    measurements = [
        {"timestamp": "2023-06-15 10:00:00", "distance": "150.2", "status": "Normal"},
        {"timestamp": "2023-06-15 10:01:00", "distance": "149.8", "status": "Normal"},
        {"timestamp": "2023-06-15 10:02:00", "distance": "151.0", "status": "Normal"},
    ]
    return render_template('monitor.html', measurements=measurements)

if __name__ == "__main__":
    app.run(debug=True)