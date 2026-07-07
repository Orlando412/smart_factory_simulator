import sqlite3


def initialize_database():

    conn = sqlite3.connect("factory.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS machine_events (

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        timestamp TEXT,

        machine TEXT,

        event_type TEXT,

        details TEXT
    )
    """)

    conn.commit()

    conn.close()