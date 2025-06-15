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
    return "Monitor page coming soon"

if __name__ == "__main__":
    app.run(debug=True)