"""
CRUD methods
"""

import sqlite3
import pyttsx3
import speech_recognition as sr
# pylint: disable=trailing-whitespace disable=C0103

r = sr.Recognizer()

engine = pyttsx3.init()

# Create a connection to the database
conn = sqlite3.connect('data/assistant.sqlite')
    
# Create a cursor object to execute SQL commands
cursor = conn.cursor()

def connect_database():
    """
    Method for connection to database
    """
    
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            content TEXT,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        '''
    )
    conn.commit()

def create_note(title, content):
    """
    Method to create a new note.
    """
    cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
    conn.commit()
    return cursor.lastrowid

def show_note(Ident):
    """
    Show one entry from the table.
    """
    cursor.execute("SELECT * FROM notes WHERE id = ?", (Ident,))
    return cursor.fetchone()

def index_note():
    """
    Show all entries from the table.
    """
    cursor.execute("SELECT * FROM notes")
    return cursor.fetchall()

def update_note(Ident, title, content):
    """
    Update entry form the table.
    """
    cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, Ident))
    conn.commit()

def delete_note(Ident):
    """
    Delete entry from the table.
    """
    cursor.execute("DELETE FROM notes WHERE id = ?", (Ident))
    conn.commit()
