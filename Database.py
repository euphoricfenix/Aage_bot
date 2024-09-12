# Create the database and the table
import sqlite3 as sq

def init_db():
    conn = sq.connect('app.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS UserLink (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            telegram_user_id INTEGER NOT NULL,
            uuid TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Run this when setting up
init_db()
