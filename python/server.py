from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

# get latest sensor row
def get_latest():
    conn = sqlite3.connect("database/iot.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT light, fan, ac, timestamp
        FROM sensor_data
        ORDER BY id DESC
        LIMIT 1
    """)

    row = cursor.fetchone()
    conn.close()

    if row:
        return {
            "light": row[0],
            "fan": row[1],
            "ac": row[2],
            "timestamp": row[3]
        }
    else:
        return {
            "light": 0,
            "fan": 0,
            "ac": 0,
            "timestamp": None
        }

@app.route("/data")
def data():
    return jsonify(get_latest())

if __name__ == "__main__":
    app.run(debug=True)