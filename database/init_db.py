import sqlite3
import os

# ensure folder exists
os.makedirs("database", exist_ok=True)

conn = sqlite3.connect("database/iot.db")
cursor = conn.cursor()

# Clean schema matching your Day 5 dashboard
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

print("Day 7 Database initialized successfully")