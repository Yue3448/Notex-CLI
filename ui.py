from rich.console import Console
from rich.table import Table
from rich import box
from note_actions import complete_notes_counter, uncomplete_notes_counter

console = Console()

def render_interface(notes, error_code):
    console.clear()
    show_logo()
    show_table(notes)
    show_stats(notes, complete_notes_counter, uncomplete_notes_counter)
    show_error(error_code)

def render_help_shell():
    show_logo()
    help_shell()

def show_table(notes):
    table_object = Table(
        title='CLI · [cyan]v0.7.6[/cyan]',
        box=box.ROUNDED,
        header_style='bold cyan',
        caption_justify='full'
    )    

    table_object.add_column("ID", justify="center")
    table_object.add_column("Status", justify="center")
    table_object.add_column("Note", justify="center")
    table_object.add_column("Date", justify='center')
    
    for note in notes:
        id_info = str(note["id"])
        text_info = str(note["text"])   
        date_info = note.get('date', '-')
          
        status_icon = "[green]✓[/green]" if note["completed"] else "[red]○[/red]"

        if status_icon == "[green]✓[/green]":
            table_object.add_row(id_info, status_icon, text_info, date_info, style='dim')    
        else:
            table_object.add_row(id_info, status_icon, text_info, date_info)
        
    console.print(table_object)

def show_error(error_code):
    if error_code in errors:
        console.print(errors[error_code])
        
def show_stats(notes, complete_counter, uncomplete_counter):
    console.print(
        f"Total: {len(notes)} | Completed: {complete_counter(notes)} | Remaining: {uncomplete_counter(notes)}"
    )

def help_shell():
    console = Console()
    table_object = Table(
        title='[bold]Help Shell[bold]',
        box=box.ROUNDED,
        header_style='bold cyan',
        caption_justify='center'
    )

    table_object.add_column('[bold]Command[bold]', justify='center')
    table_object.add_column('[bold]Action[bold]', justify='center')

    table_object.add_row('new/add [bold]<text>[bold]', 'Add a note')
    table_object.add_row('done/do [bold]<id>[bold]', 'Complete a note')
    table_object.add_row('undone/undo [bold]<id>[bold]', 'Uncomplete a note')
    table_object.add_row('del/rm [bold]<id>[bold]', 'Delete a note')
    table_object.add_row('ed/e [bold]<id>[bold] [bold]<text>[bold]', 'Edit a note')
    table_object.add_row('help/h/?', 'Show [bold]HELP[bold] panel')
    table_object.add_row('quit/q', 'Exit')

    console.print(table_object)

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
    7:'[bold red]ERROR:[/bold red] Missing note text',
    8:'[bold red]ERROR:[/bold red] Wrong command'
    }