from storage import load_notes, save_notes
from note_actions import (
    complete_notes_counter,
    uncomplete_notes_counter,
    add_to_note,
    complete_task,
    edit_note,
    delete_note,
)
from ui import (
    show_stats,
    render_help_shell,
    show_error,
    render_interface,
    console
)
from prompt_toolkit import PromptSession

def main():

    filename = "notes.json"

    notes = load_notes(filename)

    session = PromptSession()

    while True:

        render_interface(notes)

        user_input = session.prompt("notex> ")
        first_parts = user_input.split(maxsplit=1)

        if not first_parts:
            continue

        if len(first_parts) == 2:
            argument = first_parts[1]
        else:
            argument = None

        command = first_parts[0].lower()

        if command == "new":
            if argument is None:
                show_error(7)
                continue

            status = add_to_note(notes, argument)

            if status == 'created':
                save_notes(filename, notes)

        elif command == "done":

            if argument is None:
                show_error(1)
                continue

            status = complete_task(notes, argument)

            if status == 'not_found':
                show_error(2)

            elif status == 'invalid_id':
                show_error(4)

            elif status == 'completed':
                save_notes(filename, notes)

        elif command in ("remove", "rm", "del"):
            if argument is None:
                show_error(1)
                continue

            status = delete_note(notes, argument)

            if status == 'invalid_id':
                show_error(4)

            elif status == 'not_found':
                show_error(2)

            elif status == 'deleted':
                save_notes(filename, notes)

        elif command in ("e", "ed", "edit"):
            second_parts = user_input.split(maxsplit=2)

            if len(second_parts) == 1:
                show_error(3)
                continue

            elif len(second_parts) == 2:
                show_error(5)
                continue

            else:
                edit_note_id = second_parts[1]
                new_text = second_parts[2]

            status = edit_note(notes, edit_note_id, new_text)

            if status == 'not_found':
                show_error(2)

            elif status == 'invalid_id':
                show_error(4)

            elif status == 'edited':
                save_notes(filename, notes)

        elif command in ("stats", "st"):
            show_stats(notes, complete_notes_counter, uncomplete_notes_counter)

        elif command in ("?", "h", 'help'):
            with console.screen():
                render_help_shell()
                user_action = session.prompt('press any button to quit: ')
    
        elif command in ("quit", "q"):
            break

        else:
            show_error(6)

if __name__ == "__main__":
    main()