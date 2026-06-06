from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)
DB = "iot_data.db"


def get_latest():
    conn = sqlite3.connect(DB)
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
    return {}


@app.route("/latest")
def latest():
    return jsonify(get_latest())


if __name__ == "__main__":
    app.run(debug=True, port=5000)