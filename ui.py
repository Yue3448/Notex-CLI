help_string = """
ERROR: unavailable command
type "help" for check available commands
"""
errors = {
    1:'ERROR: missing note id',
    2:'No notes found',
    3:'ERROR: No id and new text',
    4:'ERROR: Invalid id',
    5:'ERROR: No new text',
    6: help_string,
    7:'ERROR:  missing note text'
    }

def show_error(error_code):
    if error_code in errors:
        print(errors[error_code])


def show_stats(notes, complete_counter, uncomplete_counter):
    print(
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
│ help/h/?                  Show command reference │
│ quit/q               Exit                   │
╰─────────────────────────────────────────────╯
"""
    print(help_text)

def show_note_list(notes):

    for note in notes:
        if note["completed"]:
            print(f"[{note['id']}] [x] {note['text']}")

        else:
            print(f"[{note['id']}] [ ] {note['text']}")

    if len(notes) == 0:
        print("No notes found.")

def show_logo():
    print()
    logo = """
███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    """

    print(logo.strip())

def show_menu():
    menu = """
CLI · v0.7.3
    """
    print(menu)