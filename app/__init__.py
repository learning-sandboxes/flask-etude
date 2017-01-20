from flask import Flask, jsonify
import os

app = Flask(__name__)


@app.route("/ping")
def ping():
    return "pong"


@app.route("/ping_json")
def ping_json():
    return jsonify({'ping': 'pong'})


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port, debug=True)
