from smarttasker.database import DatabaseManager
from smarttasker.models import Task, Note
from smarttasker.nlp_utils import extract_date, extract_category, extract_priority
class TaskManager:
    def __init__(self, database_path):
        self.db_manager = DatabaseManager(database_path)

    def add_task(self, text):
        due_date = extract_date(text)
        category = extract_category(text)
        priority = extract_priority(text)
        task = Task(None, text, due_date, category, priority)
        return self.db_manager.add_task(task)

    def add_note(self, text):
        category = extract_category(text)
        note = Note(None, text, category)
        return self.db_manager.add_note(note)

    def get_tasks(self, category=None):
       return self.db_manager.get_tasks(category)
    
    def get_notes(self, category=None):
       return self.db_manager.get_notes(category)
    
    def complete_task(self, task_index):
         tasks = self.db_manager.get_tasks()
         if 0 <= task_index < len(tasks):
             task_id = tasks[task_index].id
             self.db_manager.complete_task(task_id)
    
    def remove_task(self, task_index):
        tasks = self.db_manager.get_tasks()
        if 0 <= task_index < len(tasks):
             task_id = tasks[task_index].id
             self.db_manager.remove_task(task_id)

    def remove_note(self, note_index):
        notes = self.db_manager.get_notes()
        if 0 <= note_index < len(notes):
            note_id = notes[note_index].id
            self.db_manager.remove_note(note_id)

    def close(self):
        self.db_manager.close()