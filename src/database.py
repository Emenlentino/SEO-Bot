# src/database.py
import sqlite3

def connect_db():
    conn = sqlite3.connect('seo_bot.db')
    return conn

def create_tables():
    conn = connect_db()
    c = conn.cursor()

    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 username TEXT PRIMARY KEY,
                 password TEXT,
                 role TEXT)''')

    c.execute('''CREATE TABLE IF NOT EXISTS job_applications (
                 id INTEGER PRIMARY KEY AUTOINCREMENT,
                 company TEXT,
                 position TEXT,
                 status TEXT)''')

    conn.commit()
    conn.close()

# Run table creation on import
create_tables()
