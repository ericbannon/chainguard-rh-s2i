from flask import Flask, jsonify, request
import os
import socket

app = Flask(__name__)

@app.route("/")
def index():
    return jsonify({
        "message": "Hello from Chainguard + S2I!",
        "hostname": socket.gethostname(),
        "environment": os.environ.get("APP_ENV", "dev")
    })

@app.route("/echo", methods=["POST"])
def echo():
    data = request.get_json(force=True)
    return jsonify({"you_sent": data})

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
