import sqlite3
from datetime import datetime

DB_NAME = "iot_data.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS sensor_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            light INTEGER,
            fan INTEGER,
            ac INTEGER,
            timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
        )
    """)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS control_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device TEXT,
            value INTEGER,
            timestamp TEXT
        )
    """)

    conn.commit()
    conn.close()


def log_control(device, value):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO control_history (device, value, timestamp)
        VALUES (?, ?, ?)
    """, (
        device,
        value,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    ))

    conn.commit()
    conn.close()


def insert_data(light, fan, ac):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO sensor_data (light, fan, ac)
        VALUES (?, ?, ?)
    """, (light, fan, ac))

    conn.commit()
    conn.close()