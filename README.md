# Day 7 - Real-Time IoT Data Pipeline (Arduino → Python → SQLite)

## Objective
Build a basic real-time IoT data pipeline where simulated Arduino sensor data is sent via Serial, processed using Python, and stored in an SQLite database.

---

## System Flow

Arduino (Sensor Simulation)
        ↓
Serial Communication
        ↓
Python Backend (Data Reader)
        ↓
SQLite Database Storage

---

## Project Structure

arduino/   → Arduino sensor simulation code  
python/    → Python backend for reading and storing data  
html/      → Future dashboard UI  
database/  → SQLite database file  

---

## Learning Goals

- Understand how IoT devices generate continuous data
- Learn Serial communication between Arduino and Python
- Store real-time data into SQLite database
- Prepare for API + dashboard integration in future steps

---

## Phase 1 (Current Step)

- Arduino generates fake sensor values
- Python will read Serial data
- Data will be stored in SQLite database

---

## Future Upgrades

- REST API for data access
- Live dashboard using HTML + JS
- Device control (fan, light simulation)
- Real IoT hardware integration