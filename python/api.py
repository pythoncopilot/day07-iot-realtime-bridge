from flask import Flask, jsonify, request
from flask_cors import CORS
from db import init_db, log_control

app = Flask(__name__)
CORS(app)

# =========================
# INIT DATABASE
# =========================
init_db()

# =========================
# DEVICE STATE (LIVE MEMORY)
# =========================
device_state = {
    "light": 0,
    "fan": 0,
    "ac": 24,

    "kitchen": 0,
    "bath": 0,
    "tv": 0,
    "garage": 0
}

# =========================
# GET CURRENT STATE
# =========================
@app.route("/latest", methods=["GET"])
def latest():
    return jsonify(device_state)

# =========================
# CONTROL DEVICES + LOG TO DB
# =========================
@app.route("/control", methods=["POST"])
def control():
    global device_state

    data = request.json

    for key in device_state.keys():
        if key in data:
            device_state[key] = data[key]

            # log every change in SQLite
            log_control(key, data[key])

    return jsonify({
        "status": "success",
        "updated_state": device_state
    })

# =========================
# RESET SYSTEM (DEBUG ONLY)
# =========================
@app.route("/reset", methods=["POST"])
def reset():
    global device_state

    device_state = {
        "light": 0,
        "fan": 0,
        "ac": 24,
        "kitchen": 0,
        "bath": 0,
        "tv": 0,
        "garage": 0
    }

    return jsonify({
        "status": "reset_done",
        "state": device_state
    })

# =========================
# HEALTH CHECK
# =========================
@app.route("/")
def home():
    return jsonify({
        "status": "Smart Home IoT API Running",
        "endpoints": ["/latest", "/control", "/reset"]
    })

# =========================
# RUN SERVER
# =========================
if __name__ == "__main__":
    app.run(debug=True, port=5000)