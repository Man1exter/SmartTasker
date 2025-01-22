from rich.table import Table
from rich import box

def print_tasks(tasks, console):
    table = Table(title="Zadania",show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=4)
    table.add_column("Treść", style="green", width=40)
    table.add_column("Termin", style="cyan", width=20)
    table.add_column("Kategoria", style="blue", width=10)
    table.add_column("Priorytet", style="yellow", width=10)
    table.add_column("Ukończone", style="white", width=10)
    for task in tasks:
        table.add_row(str(task.id), task.content, str(task.due_date), task.category, task.priority, str(task.completed))
    console.print(table)

def print_notes(notes, console):
    table = Table(title="Notatki",show_header=True, header_style="bold magenta", box=box.ROUNDED)
    table.add_column("ID", style="dim", width=4)
    table.add_column("Treść", style="green", width=40)
    table.add_column("Kategoria", style="blue", width=10)
    for note in notes:
        table.add_row(str(note.id), note.content, note.category)
    console.print(table)