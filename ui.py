def show_stats(notes, complete_counter, uncomplete_counter):
    print(
        f"Total: {len(notes)} | Completed: {complete_counter(notes)} | Remaining: {uncomplete_counter(notes)}"
    )


def help_shell():
    help_text = """
╭───────────────────────────────╮
│ --------- NOTES CLI --------- │
╰───────────────────────────────╯
USAGE
  -> <command> [argument]

COMMANDS

> list
  aliases: ls, l
  description: display all saved notes
  usage: list
  examples: notes> list

> new
  description: create a new note
  usage: new <text>
  example: notes> new Buy milk

> done
  description: mark a note as completed
  usage: done <id>
  example: notes> done 3

> remove
  aliases: rm, del
  description: permanently delete a note
  usage: remove <id>
  example: notes> rm 3

> edit
  aliases: ed, e
  description: edit a note
  usage: edit <id> <text>
  example: notes> edit 1 Buy some pizza

> stats
  alias: st
  description: display note statistics

> help
  aliases: ?, h
  description: display this command reference

> quit
  alias: q
  description: terminate the current session

[TIP]
  Arguments written as <id> must be positive integer identifiers.
  Arguments written as <text> may contain multiple words.
"""
    print(help_text)


def show_note_list(notes):

    for note in notes:
        if note["completed"]:
            print(f"[{note['id']}] [[OK]] {note['text']}")

        else:
            print(f"[{note['id']}] [ ] {note['text']}")

    if len(notes) == 0:
        print("[ERROR] No notes found.")


def show_logo():
    print()
    logo = """
███╗   ██╗ ██████╗ ████████╗███████╗███████╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║
██║ ╚████║╚██████╔╝   ██║   ███████╗███████║
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
    """

    print(logo.strip())

def show_menu():
    menu = """ 
CLI · v0.7.0
Type "help" for available commands.

COMMANDS:
╭─────────────────────────────────────────────╮
│ ls, l                Show all notes         │ 
│ new <text>           Add a note             │
│ done <id>            Complete a note        │
│ del/rm <id>          Delete a note          │
│ ed/e <id> <text>     Edit a note            │
│ st                   Show statistics        │
│ h/?                  Show command reference │
│ quit/q               Exit                   │
╰─────────────────────────────────────────────╯
  """
    print(menu)