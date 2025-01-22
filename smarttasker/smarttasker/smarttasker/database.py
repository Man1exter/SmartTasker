import sqlite3
from smarttasker.models import Task, Note
from smarttasker.constants import DATABASE_PATH

class DatabaseManager:
    def __init__(self, database_path):
        self.database_path = database_path
        self.conn = sqlite3.connect(database_path)
        self.create_tables()

    def create_tables(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tasks (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                due_date TEXT,
                category TEXT,
                priority TEXT,
                completed INTEGER
            )
        ''')
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS notes (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                content TEXT NOT NULL,
                category TEXT
            )
        ''')
        self.conn.commit()

    def add_task(self, task):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO tasks (content, due_date, category, priority, completed)
            VALUES (?, ?, ?, ?, ?)
        ''', (task.content, task.due_date, task.category, task.priority, int(task.completed)))
        self.conn.commit()
        return Task(cursor.lastrowid, task.content, task.due_date, task.category, task.priority, task.completed)

    def add_note(self, note):
        cursor = self.conn.cursor()
        cursor.execute('''
            INSERT INTO notes (content, category)
            VALUES (?, ?)
        ''', (note.content, note.category))
        self.conn.commit()
        return Note(cursor.lastrowid, note.content, note.category)

    def get_tasks(self, category=None):
        cursor = self.conn.cursor()
        if category:
            cursor.execute('SELECT * FROM tasks WHERE category = ?', (category,))
        else:
            cursor.execute('SELECT * FROM tasks')
        rows = cursor.fetchall()
        tasks = []
        for row in rows:
            tasks.append(Task(row[0], row[1], row[2], row[3], row[4], bool(row[5])))
        return tasks
    
    def get_notes(self, category=None):
        cursor = self.conn.cursor()
        if category:
            cursor.execute('SELECT * FROM notes WHERE category = ?', (category,))
        else:
             cursor.execute('SELECT * FROM notes')
        rows = cursor.fetchall()
        notes = []
        for row in rows:
             notes.append(Note(row[0], row[1], row[2]))
        return notes

    def complete_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('UPDATE tasks SET completed = 1 WHERE id = ?', (task_id,))
        self.conn.commit()

    def remove_task(self, task_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
        self.conn.commit()

    def remove_note(self, note_id):
        cursor = self.conn.cursor()
        cursor.execute('DELETE FROM notes WHERE id = ?', (note_id,))
        self.conn.commit()
    
    def close(self):
        self.conn.close()