def show_note_list(notes):
    print()

    for note in notes:

        if note['completed']:
            print(f"{note['id']}. [x] {note['text']}")

        else:
            print(f"{note['id']}. [ ] {note['text']}")

    if len(notes) == 0:
        print('No notes found.')


def add_to_note(notes):
    print()

    input_your_note = input()

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

    print('Success! Note have been added.')


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

    if find_flag is False:
        print("Don't find note id.")


def delete_note(notes):
    print()

    delete_id = int(input('Enter note id: '))

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


notes = [

    {"id": 1, "text": "Изучить словари", "completed": True},
    {"id": 2, "text": "Начать JSON", "completed": False}

]

while True:

    print()
    print('Enter a command:')
    print()
    print('1. list')
    print('2. add')
    print('3. complete')
    print('4. delete')
    print('5. exit')
    print()

    command = input().lower()

    if command == 'list' or command == '1':
        show_note_list(notes)
        print()

    elif command == 'add' or command == '2':
        add_to_note(notes)
        print()

    elif command == 'complete' or command == '3':
        complete_task(notes)
        print()

    elif command == 'delete' or command == '4':
        delete_note(notes)
        print()

    elif command == 'exit' or command == '5':
        break
