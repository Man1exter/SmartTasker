import click
from smarttasker.task_manager import TaskManager
from smarttasker.utils import print_tasks, print_notes
from smarttasker.constants import DATABASE_PATH
from rich.console import Console

console = Console()
task_manager = TaskManager(database_path=DATABASE_PATH)

@click.group()
def cli():
    """SmartTasker - Inteligentny asystent zadań i notatek."""
    pass

@cli.command()
@click.argument('text', type=str)
def add_task(text):
    """Dodaj nowe zadanie."""
    task = task_manager.add_task(text)
    console.print(f"[bold green]Dodano zadanie:[/bold green] {task}")

@cli.command()
@click.argument('text', type=str)
def add_note(text):
    """Dodaj nową notatkę."""
    note = task_manager.add_note(text)
    console.print(f"[bold green]Dodano notatkę:[/bold green] {note}")

@cli.command()
@click.option('--category', '-c', type=str, default=None, help="Filtruj po kategorii")
def show_tasks(category):
    """Pokaż wszystkie zadania (opcjonalnie filtruj po kategorii)."""
    tasks = task_manager.get_tasks(category)
    if tasks:
       print_tasks(tasks, console)
    else:
        console.print("[yellow]Brak zadań[/yellow]")
@cli.command()
@click.option('--category', '-c', type=str, default=None, help="Filtruj po kategorii")
def show_notes(category):
    """Pokaż wszystkie notatki (opcjonalnie filtruj po kategorii)."""
    notes = task_manager.get_notes(category)
    if notes:
        print_notes(notes, console)
    else:
       console.print("[yellow]Brak notatek[/yellow]")

@cli.command()
@click.argument('index', type=int)
def complete_task(index):
    """Oznacz zadanie jako ukończone."""
    task_manager.complete_task(index)
    console.print(f"[bold green]Zadanie o indeksie {index} zostało oznaczone jako ukończone[/bold green]")
    

@cli.command()
@click.argument('index', type=int)
def remove_task(index):
    """Usuń zadanie."""
    task_manager.remove_task(index)
    console.print(f"[bold red]Zadanie o indeksie {index} zostało usunięte[/bold red]")


@cli.command()
@click.argument('index', type=int)
def remove_note(index):
     """Usuń notatkę."""
     task_manager.remove_note(index)
     console.print(f"[bold red]Notatka o indeksie {index} została usunięta[/bold red]")

if __name__ == '__main__':
    cli()