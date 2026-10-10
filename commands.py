from math import ceil

from prompt_toolkit import PromptSession

from note_actions import (
    add_to_note,
    complete_task,
    delete_note,
    edit_note,
    uncomplete_task,
)
from note_queries import find_note, search_notes, sort_notes
from storage import load_notes, save_notes
from ui import console, render_help_shell, render_interface, render_note


def main():

    filename = "notes.db"

    notes = load_notes(filename)

    session = PromptSession()

    error_code = None

    current_page = 1

    current_sort_argument = None

    current_query = None

    while True:
        visible_notes = None

        if current_query is None:
            max_pages = max(1, ceil(len(notes) / 12))

        else:
            visible_notes = search_notes(notes, current_query)
            max_pages = max(1, ceil(len(visible_notes) / 12))

        current_page = min(current_page, max_pages)

        if visible_notes is None:
            render_interface(
                notes,
                error_code,
                current_page,
                max_pages,
                current_sort_argument,
                current_query,
            )

        else:
            render_interface(
                visible_notes,
                error_code,
                current_page,
                max_pages,
                current_sort_argument,
                current_query,
            )

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

            if status == "created":
                save_notes(filename, notes)

        elif command in ("done", "do"):
            if argument is None:
                error_code = 1
                continue

            status = complete_task(notes, argument)

            if status == "not_found":
                error_code = 2

            elif status == "invalid_id":
                error_code = 4

            elif status == "complete cancelled":
                error_code = 10

            elif status == "Wrong command":
                error_code = 8

            elif status == "completed" or status == "all notes completed":
                save_notes(filename, notes)

        elif command in ("undone", "undo"):
            if argument is None:
                error_code = 1
                continue

            status = uncomplete_task(notes, argument)

            if status == "not_found":
                error_code = 2

            elif status == "invalid_id":
                error_code = 4

            elif status == "uncomplete cancelled":
                error_code = 10

            elif status == "Wrong command":
                error_code = 8

            elif status == "uncompleted" or status == "all notes uncompleted":
                save_notes(filename, notes)

        elif command in ("remove", "rm", "del"):
            if argument is None:
                error_code = 1
                continue

            status = delete_note(notes, argument)

            if status == "invalid_id":
                error_code = 4

            elif status == "not_found":
                error_code = 2

            elif status == "delete cancelled":
                error_code = 10

            elif status == "Wrong command":
                error_code = 8

            elif status == "deleted" or status == "all notes deleted":
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

            if status == "not_found":
                error_code = 2

            elif status == "invalid_id":
                error_code = 4

            elif status == "edited":
                save_notes(filename, notes)

        elif command in ("show", "sh"):
            if argument is None:
                error_code = 1
                continue

            status = find_note(notes, argument)

            if status == ("invalid_id", None):
                error_code = 4

            elif status == ("not_found", None):
                error_code = 2

            elif status == ("Invalid id or can't found note", None):
                error_code = 9

            elif status[0] == "ok":  # pyright: ignore[reportOptionalSubscript]
                with console.screen():
                    render_note(notes, argument)
                    user_action = session.prompt("q: ")

        elif command in ("?", "h", "help"):
            with console.screen():
                render_help_shell()
                user_action = session.prompt("q: ")  # noqa: F841

        elif command in ("search", "find"):
            current_query = argument
            current_page = 1

        elif command in ("next", "nx"):
            if current_page < max_pages:
                current_page += 1
            else:
                error_code = 11

        elif command in ("back", "bc"):
            if current_page > 1:
                current_page -= 1
            else:
                error_code = 12

        elif command == "sort":
            status = sort_notes(notes, argument)

            if len(status) == 1:
                error_code = 13

            else:
                if status[1]:
                    current_sort_argument = argument

        elif command in ("quit", "q"):
            if argument in ("search", "find"):
                current_query = None

            else:
                break

        else:
            error_code = 6
