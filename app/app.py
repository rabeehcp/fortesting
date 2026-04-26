from flask import Flask, jsonify, request
import os
import socket
import datetime

app = Flask(__name__)

visits = 0

@app.route('/')
def home():
    global visits
    visits += 1
    return jsonify({
        "message": "DevOps Journey App",
        "visits": visits,
        "pod": socket.gethostname(),
        "time": str(datetime.datetime.now()),
        "version": "v1.0"
    })

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
