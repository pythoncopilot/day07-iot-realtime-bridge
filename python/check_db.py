import sqlite3

conn = sqlite3.connect("../database/iot.db")
cursor = conn.cursor()

cursor.execute("""
SELECT * FROM sensor_data
ORDER BY id DESC
LIMIT 5
""")

rows = cursor.fetchall()

for row in rows:
    print(row)

conn.close()