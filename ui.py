from rich.console import Console
from rich.table import Table
from rich.theme import Theme
from rich import box
from note_actions import complete_notes_counter, uncomplete_notes_counter, find_note
from note_actions import get_notes_in_page

themes = Theme({
    'error': 'bold red',
    'accent': 'bold white',
    'done': 'bold green',
    'warning': 'bold yellow'
})

console = Console(theme=themes)

def render_interface(notes, error_code, current_page, max_pages, current_sort_argument):
    console.clear()
    show_logo()
    show_table(get_notes_in_page(notes, current_page, current_sort_argument))
    show_stats(notes, complete_notes_counter, uncomplete_notes_counter)
    show_page_info(current_page, max_pages),
    show_error(error_code)

def render_help_shell():
    show_help_logo()
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
        title='[accent]CLI · v0.8.2[/]',
        box=box.ROUNDED,
        header_style='accent',
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
        
        status_icon = "[done]✓[/]" if note["completed"] else "[error]○[/]"

        if status_icon == "[done]✓[/]":
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
Page [accent]{current_page}[/]/[accent]{max_pages}[/]
"""
    console.print(output_string)

def show_error(error_code):
    if error_code in errors:
        console.print(errors[error_code])
        
def show_stats(notes, complete_counter, uncomplete_counter):
    console.print(
        f"Total: [accent]{len(notes)} |[/] Completed: [accent]{complete_counter(notes)} |[/] Remaining: [accent]{uncomplete_counter(notes)}[/]"
    )

def help_shell():
    table_object = Table(
        title='[accent]Help Shell[/]',
        box=box.ROUNDED,
        header_style='accent',
        caption_justify='center',
        show_lines=True
    )

    table_object.add_column('[accent]Command[/]', justify='center')
    table_object.add_column('[accent]Argument[/]', justify='center')
    table_object.add_column('[accent]Action[/]', justify='center')

    table_object.add_row('new/add', '[accent]<text>[/]', 'Add a note')
    table_object.add_row('done/do', '[accent]all[/]', 'Complete All notes')
    table_object.add_row('done/do', '[accent]<id>[/]', 'Complete a note')
    table_object.add_row('del/rm', '[accent]all[/]', 'Delete All notes')
    table_object.add_row('undone/undo', '[accent]<id>[/]', 'Uncomplete a note')
    table_object.add_row('undone/undo', '[accent]all[/]', 'Uncomplete All notes')
    table_object.add_row('del/rm', '[accent]<id>[/]', 'Delete a note')
    table_object.add_row('ed/e', '[accent]<id> <text>[/]', 'Edit a note')
    table_object.add_row('sort', '[accent]<id>/<text>/<date>/<time>[/]', 'Sort notes by argument')
    table_object.add_row('search/search mode', '[accent]-[/]', 'Entry to Search Mode')
    table_object.add_row('next/nx', '[accent]-[/]', 'Switch to next page')
    table_object.add_row('back/bc', '[accent]-[/]', 'Switch to previous page')
    table_object.add_row('help/h/?', '[accent]-[/]', 'Show [accent]HELP[/accent] panel')
    table_object.add_row('quit/q', '[accent]-[/]', 'Exit')

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


def show_help_logo():
    console.print()
    help_logo = """
 ██╗  ██╗███████╗██╗     ██████╗
 ██║  ██║██╔════╝██║     ██╔══██╗
 ███████║█████╗  ██║     ██████╔╝
 ██╔══██║██╔══╝  ██║     ██╔═══╝
 ██║  ██║███████╗███████╗██║
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝
"""
    console.print(help_logo)

def show_search_logo():
    console.print()
    search_logo = """
 ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
 ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
 ███████╗█████╗  ███████║██████╔╝██║     ███████║
 ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
 ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
 ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""
    console.print(search_logo)

help_string = """
[error]ERROR:[/] unavailable command
type "help" for check available commands
"""
errors = {
    1:'[error]ERROR:[/] missing note id',
    2:'[accent]No notes found[/]',
    3:'[error]ERROR:[/] No id and new text',
    4:'[error]ERROR:[/] Invalid id',
    5:'[error]ERROR:[/] No new text',
    6: help_string,
    7:'[error]ERROR:[/] Missing note text',
    8:'[error]ERROR:[/] Wrong command',
    9: "[error]ERROR: [/] Invalid id or can't found note",
    10: '[warning]Action was cancelled[/]',
    11: "[accent]You're at the last page[/]",
    12: "[accent]You're at the first page[/]",
    13: '[error]ERROR:[/] Invalid argument'
    }