import json
#from colorama import *

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


#def show_stats(notes, complete_counter, uncomplete_counter):




def show_note_list(notes):

    for note in notes:

        if note['completed']:
            print(f"[{note['id']}] [✓] {note['text']}")

        else:
            print(f"[{note['id']}] [ ] {note['text']}")

    if len(notes) == 0:
        print('No notes found.')


def add_to_note(notes):
    print()

    input_your_note = input('notes>')

    if len(notes) == 0:

        notes.append(
            {
                'id': 1,
                'text': input_your_note,
                'completed': False
            }
        )

    else:
        new_id = notes[-1]['id'] + 1

        notes.append(
            {
                'id': new_id,
                'text': input_your_note,
                'completed': False
            }
        )

    print()

    print("✓ Note added successfully.")


def complete_task(notes):
    print()

    complete_id = int(input('Enter your note id: '))

    find_flag = False

    for note in notes:
        if note['id'] == complete_id:
            find_flag = True

            note['completed'] = True

            print()

            print('Note status successfully update.')
            break

    if not find_flag:
        print("Don't find note id.")


def delete_note(notes):
    print()

    delete_id = int(input('notes>'))

    found = False

    for i, note in enumerate(notes):
        if delete_id == note['id']:
            del notes[i]

            found = True

            print()

            print('Note deleted.')
            break

    if not found:
        print()

        print('Note not found.')

filename = 'notes.json'

notes = load_notes(filename)

print('╭───────────────────────────────╮')
print('│ --------- NOTES CLI --------- │')
print('╰───────────────────────────────╯')
print('Welcome to NOTES CLI v0.1!')
print()
print(f'Total: {len(notes)} | Completed: {complete_notes_counter(notes)} | Remaining: {uncomplete_notes_counter(notes)}')
print()
print('Enter a command:')
print()
print('[1] List')
print('[2] Add')
print('[3] Complete')
print('[4] Delete')
print('[5] Exit')

while True:

    command = input('notes> ').lower()

    if command == 'list' or command == '1':
        show_note_list(notes)

    elif command == 'add' or command == '2':
        add_to_note(notes)
        save_notes(filename, notes)

    elif command == 'complete' or command == '3':
        complete_task(notes)
        save_notes(filename, notes)

    elif command == 'delete' or command == '4':
        delete_note(notes)
        save_notes(filename, notes)

    elif command == 'exit' or command == '5':
        break
