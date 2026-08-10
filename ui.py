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
│ h/?                  Show command reference │
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
        print("[ERROR] No notes found.")


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
CLI · v0.7.1
    """
    print(menu)