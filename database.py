import sqlite3
from models import Contact

class Database:
    def __init__(self, db_name):
        self.connection = sqlite3.connect(db_name)
        self.create_table()

    def create_table(self):
        with self.connection:
            self.connection.execute(
                '''CREATE TABLE IF NOT EXISTS contacts (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL,
                    email TEXT NOT NULL
                )'''
            )

    def add_contact(self, contact):
        with self.connection:
            self.connection.execute(
                'INSERT INTO contacts (name, phone, email) VALUES (?, ?, ?)',
                (contact.name, contact.phone, contact.email)
            )

    def get_all_contacts(self):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM contacts')
        return cursor.fetchall()

    def get_contact_by_id(self, contact_id):
        cursor = self.connection.cursor()
        cursor.execute('SELECT * FROM contacts WHERE id = ?', (contact_id,))
        return cursor.fetchone()

    def update_contact(self, contact_id, contact):
        with self.connection:
            self.connection.execute(
                '''UPDATE contacts
                   SET name = ?, phone = ?, email = ?
                   WHERE id = ?''',
                (contact.name, contact.phone, contact.email, contact_id)
            )

    def delete_contact(self, contact_id):
        with self.connection:
            self.connection.execute('DELETE FROM contacts WHERE id = ?', (contact_id,))

    def search_contacts(self, search_term):
        cursor = self.connection.cursor()
        cursor.execute('''
            SELECT * FROM contacts
            WHERE name LIKE ?''',
            (f'%{search_term}%',)
        )
        return cursor.fetchall()
