# src/authentication.py
import hashlib
import sqlite3
from rich.prompt import Prompt
from rich.logging import RichHandler
import logging
from database import connect_db

logging.basicConfig(level=logging.INFO, handlers=[RichHandler()])
logger = logging.getLogger("auth")

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def register_user():
    conn = connect_db()
    c = conn.cursor()

    username = Prompt.ask("Enter a username")
    password = Prompt.ask("Enter a password", password=True)
    role = Prompt.ask("Enter role (admin/user)", choices=["admin", "user"])
    hashed_password = hash_password(password)

    try:
        c.execute('INSERT INTO users (username, password, role) VALUES (?, ?, ?)', 
                  (username, hashed_password, role))
        conn.commit()
        logger.info(f"User {username} registered successfully")
    except sqlite3.IntegrityError:
        logger.error("Username already exists!")

    conn.close()

def login_user():
    conn = connect_db()
    c = conn.cursor()

    username = Prompt.ask("Enter your username")
    password = Prompt.ask("Enter your password", password=True)
    hashed_password = hash_password(password)

    c.execute('SELECT role FROM users WHERE username = ? AND password = ?', (username, hashed_password))
    user = c.fetchone()

    conn.close()

    if user:
        logger.info(f"User {username} logged in successfully")
        return username, user[0]
    else:
        logger.error("Invalid username or password")
        return None, None
