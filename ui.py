from rich.console import Console
from rich.table import Table
from rich import box
from note_actions import complete_notes_counter, uncomplete_notes_counter, find_note
from note_actions import get_notes_in_page

console = Console()

def render_interface(notes, error_code, current_page, max_pages):
    console.clear()
    show_logo()
    show_table(get_notes_in_page(notes, current_page))
    show_stats(notes, complete_notes_counter, uncomplete_notes_counter)
    show_page_info(current_page, max_pages),
    show_error(error_code)

def render_help_shell():
    show_logo()
    help_shell()

def note_preview(text, max_note_length=17):

    text = text.strip()

    if len(text) > max_note_length:
        text = text[:max_note_length]
        text += '...'
        return text

    else:
        return text

def show_table(notes_in_page):
    table_object = Table(
        title='[bold white]CLI · v0.7.9[/bold white]',
        box=box.ROUNDED,
        header_style='bold white',
        caption_justify='full'
    )

    table_object.add_column("ID", justify="center")
    table_object.add_column("Status", justify="center")
    table_object.add_column(
        "Note", 
        justify="center",
        max_width=20,
        overflow='ellipsis',
        no_wrap=True
        )
    table_object.add_column("Time", justify="center")
    table_object.add_column("Date", justify="center")

    for note in notes_in_page:
        id_info = str(note["id"])
        text_info = str(note_preview(note["text"], max_note_length=17))
        date_info = note.get('date', '-')
        time_info = str(note["time"])
        
        status_icon = "[green]✓[/green]" if note["completed"] else "[red]○[/red]"

        if status_icon == "[green]✓[/green]":
            table_object.add_row(id_info, status_icon, text_info, time_info, date_info, style='dim')    
        else:
            table_object.add_row(id_info, status_icon, text_info, time_info, date_info)
        
    console.print(table_object)

def render_note(notes, show_id):

    note = find_note(notes, show_id)
    note_text = note[1]['text']
    note_id = note[1]['id']
    note_data = note[1]['date']
    note_time = note[1]['time']

    show_text = f"""
███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝

────────────────
[ID: {note_id}]

{note_text}

────────────────
[DATE] {note_data} {note_time}
"""
    console.print(show_text)

def show_page_info(current_page, max_pages):
    output_string = f"""
Page [bold white]{current_page}[/bold white]/[bold white]{max_pages}[/bold white]
"""
    console.print(output_string)

def show_error(error_code):
    if error_code in errors:
        console.print(errors[error_code])
        
def show_stats(notes, complete_counter, uncomplete_counter):
    console.print(
        f"Total: [bold white]{len(notes)} |[/bold white] Completed: [bold white]{complete_counter(notes)} |[/bold white] Remaining: [bold white]{uncomplete_counter(notes)}[/bold white]"
    )

def help_shell():
    console = Console()
    table_object = Table(
        title='[bold]Help Shell[bold]',
        box=box.ROUNDED,
        header_style='bold white',
        caption_justify='center',
        show_lines=True
    )

    table_object.add_column('[bold]Command[bold]', justify='center')
    table_object.add_column('[bold]Argument[bold]', justify='center')
    table_object.add_column('[bold]Action[bold]', justify='center')

    table_object.add_row('new/add', '[bold white]<text>[/bold white]', 'Add a note')
    table_object.add_row('new/add', '[bold white]all[/bold white]', 'Complete All notes')
    table_object.add_row('done/do', '[bold white]<id>[/bold white]', 'Complete a note')
    table_object.add_row('done/do', '[bold white]<all>[/bold white]', 'Delete All notes')
    table_object.add_row('undone/undo', '[bold white]<id>[/bold white]', 'Uncomplete a note')
    table_object.add_row('done/do', '[bold white]<all>[/bold white]', 'Uncomplete All notes')
    table_object.add_row('del/rm', '[bold white]<id>[/bold white]', 'Delete a note')
    table_object.add_row('ed/e', '[bold white]<id> <text>[/bold white]', 'Edit a note')
    table_object.add_row('next/nx', '[bold white]-[/bold white]', 'Switch to next page')
    table_object.add_row('back/bc', '[bold white]-[/bold white]', 'Switch to previous page')
    table_object.add_row('help/h/?', '[bold white]-[/bold white]', 'Show [bold white]HELP[/bold white] panel')
    table_object.add_row('quit/q', '[bold white]-[/bold white]', 'Exit')

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

    console.print(logo)

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
    8:'[bold red]ERROR:[/bold red] Wrong command',
    9: "[bold red]EROR: [/bold red] Invalid id or can't found note",
    10: 'Action was cancelled',
    11: "You're at the last page",
    12: "You're at the first page"
    }