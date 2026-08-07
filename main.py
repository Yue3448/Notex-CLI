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

╭───────────────────────────────╮
│ --------- NOTES CLI --------- │
╰───────────────────────────────╯
USAGE
  └─ <command> [argument]

COMMANDS

> list
  ├─ aliases: ls, l
  ├─ description: display all saved notes
  ├─ usage: list
  └─ examples:
     ├─ notes> list
     └─ notes> ls

> new
  ├─ aliases: new
  ├─ description: create a new note
  ├─ usage: new <text>
  └─ examples:
     ├─ notes> new Learn Python exceptions
     └─ notes> new Buy milk

> done
  ├─ aliases: done
  ├─ description: mark a note as completed
  ├─ usage: done <id>
  └─ examples:
     ├─ notes> done 3
     └─ notes> done 1

> remove
  ├─ aliases: rm, del
  ├─ description: permanently delete a note
  ├─ usage: remove <id>
  └─ examples:
     ├─ notes> remove 3
     ├─ notes> rm 3
     └─ notes> del 3

> edit
  ├─ aliases: edit, ed, e
  ├─ description: edit your note
  ├─ usage: ed <id> <text> 
  └─ examples:
     ├─ notes> edit 1 buy some pizza
     └─ notes> e 67 go to park

> stats
  ├─ aliases: st
  ├─ description: display note statistics
  ├─ usage: st
  └─ examples:
     └─ notes> st

> help
  ├─ aliases: ?, h
  ├─ description: display this command reference
  ├─ usage: h
  └─ examples:
     ├─ notes> h
     └─ notes> ?

> quit
  ├─ aliases: quit, q
  ├─ description: terminate the current session
  ├─ usage: quit
  └─ examples:
     ├─ notes> quit
     └─ notes> q

[ TIP ]
  ├─ Arguments written as <id> must be integer note identifiers.
  ├─ Arguments written as <text> may contain multiple words.
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
        print("✗ No notes found.")


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

    is_valid_id = complete_id.isdecimal()

    if not is_valid_id:
        print("✗ error: note ID must be a positive integer")
        return

    complete_id = int(complete_id)

    find_flag = False

    for note in notes:
        if note['id'] == complete_id:
            find_flag = True

            note['completed'] = True

            print("✓ Note status updated successfully")
            break

    if not find_flag:
        print("✗ Don't find note id")


def edit_note(notes, edit_note_id, new_text):
    
    is_valid_id = edit_note_id.isdecimal()
    
    if not is_valid_id:
        print("✗ error: note ID must be a positive integer")
        return
    
    edit_note_id = int(edit_note_id)

    found_id = False
    
    for note in notes:
        if note['id'] == edit_note_id:
            found_id = True
        
        if found_id is True:
            note['text'] = new_text
            
            print("✓ Note succesfully edited")
            break
        
    if not found_id:
        print("✗ Don't find note id")


def delete_note(notes, delete_id):

    is_valid_id = delete_id.isdecimal()

    if not is_valid_id:
        print("✗ error: note ID must be a positive integer")
        return

    delete_id = int(delete_id)

    found = False

    for i, note in enumerate(notes):
        if delete_id == note['id']:
            del notes[i]

            found = True

            print("✓ Note deleted")
            break

    if not found:
        print("✗ Note not found")

filename = 'notes.json'

notes = load_notes(filename)

logo = """
███╗   ██╗ ██████╗ ████████╗███████╗███████╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝██╔════╝
██╔██╗ ██║██║   ██║   ██║   █████╗  ███████╗
██║╚██╗██║██║   ██║   ██║   ██╔══╝  ╚════██║
██║ ╚████║╚██████╔╝   ██║   ███████╗███████║
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚══════╝
"""

print(logo)
print("CLI · v0.6.1")
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

    user_input = input('notes> ')
    first_parts = user_input.split(maxsplit=1)

    if not first_parts:
        continue

    if len(first_parts) == 2:
        argument = first_parts[1]
    else:
        argument = None

    command = first_parts[0].lower()

    if command == 'list' or command == 'ls' or command == 'l':
        show_note_list(notes)

    elif command == 'new':
        if argument is None:
            print("✗ error: missing note text")
            print('usage: new <text>')
            continue
        
        add_to_note(notes, argument)
        save_notes(filename, notes)

    elif command == 'done':
        if argument is None:
            print("✗ error: missing note id")
            print('usage: done <id>')
            continue
        
        complete_task(notes, argument)
        save_notes(filename, notes)

    elif command == 'remove' or command == 'rm' or command == 'del':
        if argument is None:
            print("✗ error: missing note id")
            print('usage: rm <id>')
            continue
        
        delete_note(notes, argument)
        save_notes(filename, notes)

    elif command == 'e' or command == 'ed' or command == 'edit':
        second_parts = user_input.split(maxsplit=2)
        
        if len(second_parts) == 1:
            print("✗ No id and new text")
            continue
        
        elif len(second_parts) == 2:
            print("✗ No new text")
            continue
        
        else:
           edit_note_id = second_parts[1]  
           new_text = second_parts[2]
        
        edit_note(notes, edit_note_id, new_text)
        save_notes(filename, notes)
         
    elif command == 'stats' or command == 'st':
        show_stats(notes, complete_notes_counter, uncomplete_notes_counter)

    elif command == 'help' or command == '?' or command == 'h':
        help_shell()

    elif command == 'quit' or command == 'q':
        break

    else:
        print(f"✗ error: unavailable command {command}")
        print('type "help" for check available commands')