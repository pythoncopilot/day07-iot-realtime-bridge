import sqlite3

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