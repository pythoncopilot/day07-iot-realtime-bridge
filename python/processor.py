import time
import random
import sqlite3
import os

print("Day 7 Processor Started...")

# connect to DB
conn = sqlite3.connect("database/iot.db")
cursor = conn.cursor()

while True:
    # simulate Day 5 dashboard values
    light = random.randint(0, 100)
    fan = random.randint(0, 100)
    ac = random.randint(0, 100)

    print(f"Light: {light}% | Fan: {fan}% | AC: {ac}%")

    # insert into database
    cursor.execute("""
        INSERT INTO sensor_data (light, fan, ac)
        VALUES (?, ?, ?)
    """, (light, fan, ac))

    conn.commit()

    # simulate real-time delay
    time.sleep(2)