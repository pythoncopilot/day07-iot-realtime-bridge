from db import init_db
from serial_reader import start_reader

if __name__ == "__main__":
    init_db()
    start_reader()