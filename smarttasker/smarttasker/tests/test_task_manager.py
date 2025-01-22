import unittest
import os
from smarttasker.task_manager import TaskManager
from smarttasker.constants import DATABASE_PATH


class TestTaskManager(unittest.TestCase):
    def setUp(self):
        if os.path.exists(DATABASE_PATH):
            os.remove(DATABASE_PATH)
        self.task_manager = TaskManager(DATABASE_PATH)
    
    def tearDown(self):
         self.task_manager.close()
         if os.path.exists(DATABASE_PATH):
            os.remove(DATABASE_PATH)

    def test_add_task(self):
        task = self.task_manager.add_task("Testowe zadanie pilne na jutro")
        self.assertEqual(task.content, "Testowe zadanie pilne na jutro")
        self.assertEqual(task.priority, "pilne")
    
    def test_add_note(self):
        note = self.task_manager.add_note("Testowa notatka do domu")
        self.assertEqual(note.content, "Testowa notatka do domu")
        self.assertEqual(note.category, "dom")

    def test_get_tasks(self):
        self.task_manager.add_task("Task 1")
        self.task_manager.add_task("Task 2 praca")
        tasks = self.task_manager.get_tasks()
        self.assertEqual(len(tasks), 2)

        tasks_praca = self.task_manager.get_tasks("praca")
        self.assertEqual(len(tasks_praca), 1)
        self.assertEqual(tasks_praca[0].content, "Task 2 praca")

    def test_get_notes(self):
        self.task_manager.add_note("Note 1")
        self.task_manager.add_note("Note 2 dom")
        notes = self.task_manager.get_notes()
        self.assertEqual(len(notes), 2)

        notes_dom = self.task_manager.get_notes("dom")
        self.assertEqual(len(notes_dom), 1)
        self.assertEqual(notes_dom[0].content, "Note 2 dom")

    def test_complete_task(self):
         task = self.task_manager.add_task("Zadanie testowe do zakonczenia")
         self.task_manager.complete_task(0)
         tasks = self.task_manager.get_tasks()
         self.assertTrue(tasks[0].completed)
    
    def test_remove_task(self):
         self.task_manager.add_task("Zadanie 1")
         self.task_manager.add_task("Zadanie 2")
         self.task_manager.remove_task(0)
         tasks = self.task_manager.get_tasks()
         self.assertEqual(len(tasks), 1)
         self.assertEqual(tasks[0].content, "Zadanie 2")

    def test_remove_note(self):
         self.task_manager.add_note("Notatka 1")
         self.task_manager.add_note("Notatka 2")
         self.task_manager.remove_note(0)
         notes = self.task_manager.get_notes()
         self.assertEqual(len(notes), 1)
         self.assertEqual(notes[0].content, "Notatka 2")

if __name__ == '__main__':
    unittest.main()