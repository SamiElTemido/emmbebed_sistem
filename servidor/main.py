from flask import Flask,render_template

app = Flask(__name__)

@app.route("/")
def main():
    name="Pepe"
    return render_template('main.html',person=name)

@app.route("/health")
def healthcheck():
    x=1+1
    return "<p>server is up and running</p>"   