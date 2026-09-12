from storage import load_notes, save_notes
from note_actions import (
    add_to_note,
    complete_task,
    uncomplete_task,
    edit_note,
    delete_note,
    find_note,
)
from ui import (
    render_help_shell,
    render_interface,
    console,
    render_note,
)
from prompt_toolkit import PromptSession

def main():

    filename = "notes.json"

    notes = load_notes(filename)

    session = PromptSession()

    error_code = None

    while True:

        render_interface(notes, error_code)

        user_input = session.prompt("notex> ")
        error_code = None
        
        first_parts = user_input.split(maxsplit=1)

        if not first_parts:
            continue

        if len(first_parts) == 2:
            argument = first_parts[1]
        else:
            argument = None

        command = first_parts[0].lower()

        if command in ("new", "add"):
            if argument is None:
                error_code = 7
                continue

            status = add_to_note(notes, argument)

            if status == 'created':
                save_notes(filename, notes)

        elif command in ("done", 'do'):

            if argument is None:
                error_code = 1
                continue

            status = complete_task(notes, argument)

            if status == 'not_found':
                error_code = 2

            elif status == 'invalid_id':
                error_code = 4

            elif status == 'completed':
                save_notes(filename, notes)

            elif status == 'all notes completed':
                save_notes(filename, notes)

        elif command in ("undone", "undo"):

            if argument is None:
                error_code = 1
                continue

            status = uncomplete_task(notes, argument)

            if status == 'not_found':
                error_code = 2

            elif status == 'invalid_id':
                error_code = 4

            elif status == 'uncompleted':
                save_notes(filename, notes)

            elif status == 'all notes uncompleted':
                save_notes(filename, notes)

        elif command in ("remove", "rm", "del"):
            
            if argument is None:
                error_code = 1
                continue

            status = delete_note(notes, argument)

            if status == 'invalid_id':
                error_code = 4

            elif status == 'not_found':
                error_code = 2

            elif status == 'deleted':
                save_notes(filename, notes)

            elif status == 'all notes deleted':
                save_notes(filename, notes)

        elif command in ("e", "ed", "edit"):
            second_parts = user_input.split(maxsplit=2)

            if len(second_parts) == 1:
                error_code = 3
                continue

            elif len(second_parts) == 2:
                error_code = 5
                continue

            else:
                edit_note_id = second_parts[1]
                new_text = second_parts[2]

            status = edit_note(notes, edit_note_id, new_text)

            if status == 'not_found':
                error_code = 2

            elif status == 'invalid_id':
                error_code = 4

            elif status == 'edited':
                save_notes(filename, notes)


        elif command in ("show", "sh"):

            if argument is None:
                error_code = 1
                continue

            status = find_note(notes, argument)

            if status == ('invalid_id', None):
                error_code = 4

            elif status == ('not_found', None):
                error_code = 2

            elif status == ("Invalid id or can't found note", None):
                error_code = 9

            elif status[0] == 'ok':
                with console.screen():
                    render_note(notes, argument)
                    user_action = session.prompt('type something to quit: ')

        elif command in ("?", "h", 'help'):
            with console.screen():
                render_help_shell()
                user_action = session.prompt('type something to quit: ')
    
        elif command in ("quit", "q"):
            break

        else:
            error_code = 6

if __name__ == "__main__":
    main()