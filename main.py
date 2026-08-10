from storage import load_notes, save_notes
from note_actions import (
    complete_notes_counter,
    uncomplete_notes_counter,
    add_to_note,
    complete_task,
    edit_note,
    delete_note,
)
from ui import show_logo, show_stats, help_shell, show_note_list, show_menu

def main():

    filename = "notes.json"

    notes = load_notes(filename)

    show_logo()
    show_menu()

    while True:
        user_input = input("notes> ")
        first_parts = user_input.split(maxsplit=1)

        if not first_parts:
            continue

        if len(first_parts) == 2:
            argument = first_parts[1]
        else:
            argument = None

        command = first_parts[0].lower()

        if command in ("list", "ls", "l"):
            show_note_list(notes)

        elif command == "new":
            if argument is None:
                print("[ERROR]  missing note text")
                print("usage: new <text>")
                continue

            status = add_to_note(notes, argument)

            if status == 'created':
                save_notes(filename, notes)

        elif command == "done":

            if argument is None:
                print("[ERROR]  missing note id")
                print("usage: done <id>")
                continue

            status = complete_task(notes, argument)

            if status == 'not_found':
                print('No notes found')

            elif status == 'invalid_id':
                print('[ERROR] Invalid id')

            elif status == 'completed':
                save_notes(filename, notes)

        elif command in ("remove", "rm", "del"):
            if argument is None:
                print("[ERROR] missing note id")
                print("usage: rm <id>")
                continue

            status = delete_note(notes, argument)

            if status == 'invalid_id':
                print('[ERROR] invalid id')

            elif status == 'not_found':
                print("[ERROR] Don't found id.")

            elif status == 'deleted':
                save_notes(filename, notes)

        elif command in ("e", "ed", "edit"):
            second_parts = user_input.split(maxsplit=2)

            if len(second_parts) == 1:
                print("[ERROR] No id and new text")
                continue

            elif len(second_parts) == 2:
                print("[ERROR] No new text")
                continue

            else:
                edit_note_id = second_parts[1]
                new_text = second_parts[2]

            status = edit_note(notes, edit_note_id, new_text)

            if status == 'not_found':
                print("[ERROR] Don't found id")

            elif status == 'invalid_id':
                print('[ERROR] Invalid id')

            elif status == 'edited':
                save_notes(filename, notes)

        elif command in ("stats", "st"):
            show_stats(notes, complete_notes_counter, uncomplete_notes_counter)

        elif command in ("?", "h", 'help'):
            help_shell()

        elif command in ("quit", "q"):
            break

        else:
            print(f"[ERROR]  unavailable command {command}")
            print('type "help" for check available commands')

if __name__ == "__main__":
    main()