"""
CRUD methods
"""

import sqlite3
import pyttsx3
import speech_recognition as sr
# pylint: disable=trailing-whitespace disable=C0103

class DB:
    def __init__(self):
        self.r = sr.Recognizer()
        self.engine = pyttsx3.init()
        self.conn = sqlite3.connect('data/assistant.sqlite')
        self.__first_initialise = True
        self.cursor = self.conn.cursor()
        while self.__first_initialise == True:
            """
            Loop for first_initialisation
            """
            self.cursor.execute(
                '''
                CREATE TABLE IF NOT EXISTS notes (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    title TEXT,
                    content TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                    )
                    '''
            )
            self.conn.commit()
            self.__first_initialise = False
    
    def show_note(self, Ident):
        """
        Show one entry from the table.
        """
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (Ident,))
        return self.cursor.fetchone()

    def create_note(self, title, content):
        """
         Method to create a new note.
        """
        self.cursor.execute("INSERT INTO notes (title, content) VALUES (?, ?)", (title, content))
        self.conn.commit()
        item = self.show_note(self.cursor.lastrowid)
        return item

    def show_note(self, Ident):
        """
        Show one entry from the table.
        """
        self.cursor.execute("SELECT * FROM notes WHERE id = ?", (Ident,))
        return self.cursor.fetchone()

    def index_note(self):
        """
        Show all entries from the table.
        """
        self.cursor.execute("SELECT title, content FROM notes")
        return self.cursor.fetchall()

    def update_note(self, Ident, title, content):
        """
        Update entry form the table.
        """
        self.cursor.execute("UPDATE notes SET title = ?, content = ? WHERE id = ?", (title, content, Ident))
        self.commit()

    def delete_note(self, Ident):
        """
        Delete entry from the table.
        """
        self.cursor.execute("DELETE FROM notes WHERE id = ?", (Ident))
        self.commit()
