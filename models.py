class Task:
    def __init__(self, id, content, due_date=None, category='uncategorized', priority='normal', completed = False):
        self.id = id
        self.content = content
        self.due_date = due_date
        self.category = category
        self.priority = priority
        self.completed = completed
    def __str__(self):
       return f"Zadanie(id={self.id}): {self.content}, Termin: {self.due_date}, Kategoria: {self.category}, Priorytet: {self.priority}, Ukończone: {self.completed}"


class Note:
    def __init__(self, id, content, category='uncategorized'):
        self.id = id
        self.content = content
        self.category = category
    def __str__(self):
       return f"Notatka(id={self.id}): {self.content}, Kategoria: {self.category}"