# Day 7 - IoT System with SQLite Integration (Clean Baseline)

## Objective
This project extends the Day 5 IoT simulation system by introducing a SQLite database layer for persistent sensor data storage, while keeping the original dashboard UI unchanged.

---

## System Architecture

Arduino (Simulated Sensor Data)
        ↓
Python Processor
        ↓
SQLite Database
        ↓
Future: Dashboard Integration

---

## Project Structure

- arduino/ → Simulated sensor data generator
- python/ → Data processing and database insertion logic
- database/ → SQLite database and initialization scripts
- html/ → Day 5 dashboard UI (unchanged for stability)

---

## Features

- Simulated temperature, humidity, and light sensors
- Continuous data generation every 2 seconds
- SQLite database storage with timestamped entries
- Database inspection tool for verifying stored data
- Stable UI preserved from Day 5

---

## Database

Table: sensor_data

Fields:
- id (Primary Key)
- temperature
- humidity
- light
- timestamp

---

## Learning Outcomes

- Understanding IoT data pipelines
- Introduction to relational databases (SQLite)
- Data persistence concepts
- Separation of system layers (device, processing, storage, UI)

---

## Current Limitation

The dashboard is static in this phase and does not yet display live database data. This will be implemented in the next phase.

---

## Next Step

- Connect dashboard to database
- Enable live data visualization
- Introduce controlled real-time updates