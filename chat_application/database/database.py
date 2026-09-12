import sqlite3
from pathlib import Path

from utils.security import hash_password
from utils.security import hash_password, verify_password

BASE_DIR = Path(__file__).resolve().parent
DATABASE_NAME = BASE_DIR / "chat.db"


def get_connection():
    connection = sqlite3.connect(DATABASE_NAME)
    return connection


def initialize_database():
    connection = get_connection()

    schema_path = BASE_DIR / "schema.sql"

    with open(schema_path, "r") as file:
        schema = file.read()

    connection.executescript(schema)

    connection.commit()
    connection.close()

    print("Database initialized successfully.")

def create_user(username, password):
    connection = get_connection()

    try:
        cursor = connection.cursor()

        password_hash = hash_password(password)

        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (?, ?)
            """,
            (username, password_hash)
        )

        connection.commit()
        return True

    except sqlite3.IntegrityError:
        return False

    finally:
        connection.close()

def get_user(username):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT id, username, password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    return user    

def authenticate_user(username, password):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT password
        FROM users
        WHERE username = ?
        """,
        (username,)
    )

    user = cursor.fetchone()

    connection.close()

    if user is None:
        return False

    stored_password = user[0]

    return verify_password(password, stored_password)    


def save_message(username, room_name, message):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        INSERT INTO messages (username, room_name, message)
        VALUES (?, ?, ?)
        """,
        (username, room_name, message)
    )

    connection.commit()
    connection.close()


def get_room_messages(room_name):
    connection = get_connection()

    cursor = connection.cursor()

    cursor.execute(
        """
        SELECT username, message, sent_at
        FROM messages
        WHERE room_name = ?
        ORDER BY id ASC
        """,
        (room_name,)
    )

    messages = cursor.fetchall()

    connection.close()

    return messages    