import time
import random
import sqlite3

conn = sqlite3.connect("../database/iot.db")
cursor = conn.cursor()

print("Day 7 system running...")

while True:
    temperature = random.randint(20, 35)
    humidity = random.randint(40, 80)
    light = random.randint(200, 900)

    print(f"Generated -> T:{temperature}, H:{humidity}, L:{light}")

    cursor.execute("""
        INSERT INTO sensor_data (temperature, humidity, light)
        VALUES (?, ?, ?)
    """, (temperature, humidity, light))

    conn.commit()

    time.sleep(2)