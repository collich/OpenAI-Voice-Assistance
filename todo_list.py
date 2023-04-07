"""
CRUD methods
"""

import sqlite3
import pyttsx3
import speech_recognition as sr
# pylint: disable=trailing-whitespace

r = sr.Recognizer()

engine = pyttsx3.init()

def connect_database():
    """
    Method for connection to database
    """
    
    # Create a connection to the database
    conn = sqlite3.connect('data/assistant.sqlite')
    
    # Create a cursor object to execute SQL commands
    cursor = conn.cursor()
    
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