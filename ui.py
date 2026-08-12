from rich.console import *

console = Console()

def render_interface(notes, complete_notes_counter, uncomplete_notes_counter):
    console.clear()
    show_logo()
    show_menu()
    show_stats(notes, complete_notes_counter, uncomplete_notes_counter)
    show_note_list(notes)


help_string = """
[bold red]ERROR:[/bold red] unavailable command
type "help" for check available commands
"""
errors = {
    1:'[bold red]ERROR:[/bold red] missing note id',
    2:'No notes found',
    3:'[bold red]ERROR:[/bold red] No id and new text',
    4:'[bold red]ERROR:[/bold red] Invalid id',
    5:'[bold red]ERROR:[/bold red] No new text',
    6: help_string,
    7:'[bold red]ERROR:[/bold red] missing note text'
    }

def show_error(error_code):
    if error_code in errors:
        console.print(errors[error_code])


def show_stats(notes, complete_counter, uncomplete_counter):
    console.print(
        f"Total: {len(notes)} | Completed: {complete_counter(notes)} | Remaining: {uncomplete_counter(notes)}"
    )

def help_shell():
    help_text = """
╭─────────────────────────────────────────────╮
│ ls/l                 Show all notes         │ 
│ new <text>           Add a note             │
│ done <id>            Complete a note        │
│ del/rm <id>          Delete a note          │
│ ed/e <id> <text>     Edit a note            │
│ st                   Show statistics        │
│ help/h/?             Show command reference │
│ quit/q               Exit                   │
╰─────────────────────────────────────────────╯
"""
    console.print(help_text)

def show_note_list(notes):

    for note in notes:
        if note["completed"]:
            console.print(f"[{note['id']}] [x] {note['text']}")

        else:
            console.print(f"[{note['id']}] [ ] {note['text']}")

    if len(notes) == 0:
        console.print("No notes found.")

def show_logo():
    console.print()
    logo = """
███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    """

    console.print(logo.strip())

def show_menu():
    menu = """
CLI · v0.7.3.1
    """
    console.print(menu)
