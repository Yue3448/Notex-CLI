import json

def load_notes(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as file:
            notes = json.load(file)

        return notes

    except FileNotFoundError:
        return []

def save_notes(filename, notes):
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)


def complete_notes_counter(notes):
    cnt = 0

    for note in notes:
        if note['completed']:
            cnt += 1

    return cnt


def uncomplete_notes_counter(notes):
    cnt = 0

    for note in notes:
        if not note['completed']:
            cnt += 1

    return cnt


def show_stats(notes, complete_counter, uncomplete_counter):
    print(f'Total: {len(notes)} | Completed: {complete_counter(notes)} | Remaining: {uncomplete_counter(notes)}')


def help_shell():
    HELP_TEXT = """
[ NOTES CLI — COMMAND REFERENCE ]
USAGE
  └─ <command> [argument]

COMMANDS
> list
  ├─ aliases: list, ls, l
  ├─ description: display all saved notes
  └─ examples:
     ├─ notes> list
     └─ notes> ls

> add
  ├─ aliases: new
  ├─ description: create a new note
  └─ example:
     └─ notes> add
        Text: Learn Python exceptions

> complete
  ├─ aliases: done
  ├─ description: mark a note as completed
  ├─ usage: complete <id>
  └─ examples:
     ├─ notes> complete 3
     └─ notes> done 3

> delete
  ├─ aliases: remove, rm, del
  ├─ description: permanently delete a note
  ├─ usage: delete <id>
  └─ examples:
     ├─ notes> delete 3
     └─ notes> rm 3
     
> stats
  ├─ aliases: stats, st
  ├─ description: display all your notes statistics
  ├─ usage: stats
  └─ examples:
     ├─ notes> stats
     └─ notes> st 3
     
> help
  ├─ aliases: help, ?, h
  ├─ description: display this command reference
  └─ example:
     └─ notes> help

> exit
  ├─ aliases: quit, q
  ├─ description: terminate the current session
  └─ example:
     └─ notes> exit

[ TIP ]
  ├─ Arguments written as <id> are required.
  └─ Type "help" whenever you need this reference.
    """

    print(HELP_TEXT)


def show_note_list(notes):

    for note in notes:

        if note['completed']:
            print(f"[{note['id']}] [✓] {note['text']}")

        else:
            print(f"[{note['id']}] [ ] {note['text']}")

    if len(notes) == 0:
        print('No notes found.')


def add_to_note(notes, text):

    if len(notes) == 0:

        notes.append(
            {
                'id': 1,
                'text': text,
                'completed': False
            }
        )

    else:
        new_id = notes[-1]['id'] + 1

        notes.append(
            {
                'id': new_id,
                'text': text,
                'completed': False
            }
        )

    print("✓ Note added successfully.")


def complete_task(notes, complete_id):

    complete_id = int(complete_id)

    find_flag = False

    for note in notes:
        if note['id'] == complete_id:
            find_flag = True

            note['completed'] = True

            print('Note status successfully update.')
            break

    if not find_flag:
        print("Don't find note id.")


def delete_note(notes, delete_id):

    delete_id = int(delete_id)

    found = False

    for i, note in enumerate(notes):
        if delete_id == note['id']:
            del notes[i]

            found = True

            print('Note deleted.')
            break

    if not found:
        print('Note not found.')

filename = 'notes.json'

notes = load_notes(filename)

print('╭───────────────────────────────╮')
print('│ --------- NOTES CLI --------- │')
print('╰───────────────────────────────╯')
print('Welcome to NOTES CLI v0.5!')
print('Type "help" for available commands.')
print()
print('[1] List')
print('[2] Add')
print('[3] Complete')
print('[4] Delete')
print('[5] Edit')
print('[6] Stats')
print('[7] Help')
print('[8] Exit')
print()

while True:

    command = input('notes> ').lower()

    buffer_list = command.split(' ', 1)

    if buffer_list[0] == 'list' or buffer_list[0] == 'ls' or buffer_list[0] == 'l':
        show_note_list(notes)

    elif buffer_list[0] == 'new':
        add_to_note(notes, buffer_list[1])
        save_notes(filename, notes)

    elif buffer_list[0] == 'done':
        complete_task(notes, buffer_list[1])
        save_notes(filename, notes)

    elif buffer_list[0] == 'remove' or buffer_list[0] == 'rm' or buffer_list[0] == 'del':
        delete_note(notes, buffer_list[1])
        save_notes(filename, notes)

    elif buffer_list[0] == 'stats' or buffer_list[0] == 'st':
        show_stats(notes, complete_notes_counter, uncomplete_notes_counter)

    elif buffer_list[0] == 'help' or buffer_list[0] == '?' or buffer_list[0] == 'h':
        help_shell()

    elif buffer_list[0] == 'quit' or buffer_list[0] == 'q':
        break
