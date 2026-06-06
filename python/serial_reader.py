import time
import random
from db import insert_data

# =========================
# MODE SWITCH
# =========================
USE_HARDWARE = False   # 🔁 CHANGE THIS LATER TO True

# =========================
# SERIAL IMPORT ONLY IF NEEDED
# =========================
if USE_HARDWARE:
    import serial

    PORT = "COM3"   # change later
    BAUD = 9600


# =========================
# PARSER (shared logic)
# =========================
def parse_line(line):
    try:
        parts = line.strip().split(",")
        data = {}

        for p in parts:
            key, value = p.split(":")
            data[key] = int(value)

        return data
    except:
        return None


# =========================
# SIMULATION MODE
# =========================
def simulation_loop():
    print("💻 Running in SIMULATION MODE (no hardware)\n")

    while True:
        line = f"LIGHT:{random.randint(0,1)},FAN:{random.randint(0,100)},AC:{random.randint(18,28)}"
        print("RAW:", line)

        data = parse_line(line)

        if data:
            insert_data(
                data["LIGHT"],
                data["FAN"],
                data["AC"]
            )
            print("✔ Stored in DB:", data)

        time.sleep(2)


# =========================
# HARDWARE MODE
# =========================
def hardware_loop():
    print("🔌 Running in HARDWARE MODE (Arduino connected)\n")

    ser = serial.Serial(PORT, BAUD, timeout=1)

    while True:
        line = ser.readline().decode().strip()

        if line:
            print("RAW:", line)

            data = parse_line(line)

            if data:
                insert_data(
                    data.get("LIGHT", 0),
                    data.get("FAN", 0),
                    data.get("AC", 0)
                )

                print("✔ Stored in DB:", data)


# =========================
# STARTER
# =========================
def start_reader():
    if USE_HARDWARE:
        hardware_loop()
    else:
        simulation_loop()