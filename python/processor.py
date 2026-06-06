import time
import random
import sqlite3

# connect to database
conn = sqlite3.connect("database/iot.db")
cursor = conn.cursor()

print("IoT system started\n")

while True:
    # simulated Arduino data
    temperature = random.randint(20, 35)
    humidity = random.randint(40, 80)
    light = random.randint(200, 900)

    print("Generated:", temperature, humidity, light)

    # store in database
    cursor.execute("""
        INSERT INTO sensor_data (temperature, humidity, light)
        VALUES (?, ?, ?)
    """, (temperature, humidity, light))

    conn.commit()

    print("Saved to DB ✔")
    print("-" * 30)

    time.sleep(2)