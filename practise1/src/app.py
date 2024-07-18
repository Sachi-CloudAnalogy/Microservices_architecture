import socket
from flask import Flask, jsonify, render_template
app = Flask(__name__)

def fetch():
    host_name = socket.gethostname()
    host_ip = socket.gethostbyname(host_name)
    return str(host_name), str(host_ip)

@app.route("/")
def home():
    return "Hello world !!"

@app.route("/health")
def health():
    return jsonify(Status="Active")

@app.route("/new")
def new():
    hostname, ip = fetch()
    return render_template("index.html", hostname=hostname, IP=ip)


if __name__ == "__main__":
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=5000, debug=True)
    