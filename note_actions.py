def complete_notes_counter(notes):
    cnt = 0

    for note in notes:
        if note["completed"]:
            cnt += 1

    return cnt

def uncomplete_notes_counter(notes):
    cnt = 0

    for note in notes:
        if not note["completed"]:
            cnt += 1

    return cnt

def add_to_note(notes, text):

    if len(notes) == 0:
        notes.append({"id": 1, "text": text, "completed": False})

    else:
        new_id = notes[-1]["id"] + 1

        notes.append({"id": new_id, "text": text, "completed": False})

    print("[OK] Note added successfully.")

def complete_task(notes, complete_id):

    is_valid_id = complete_id.isdecimal()

    if not is_valid_id:
        print("[ERROR] Note ID must be a positive integer")
        return

    complete_id = int(complete_id)

    find_flag = False

    for note in notes:
        if note["id"] == complete_id:
            find_flag = True

            note["completed"] = True

            print("[OK] Note status updated successfully")
            break

    if not find_flag:
        print("[ERROR] Note ID not found")
    
def edit_note(notes, edit_note_id, new_text):

    is_valid_id = edit_note_id.isdecimal()

    if not is_valid_id:
        print("[ERROR] Note ID must be a positive integer")
        return

    edit_note_id = int(edit_note_id)

    found_id = False

    for note in notes:
        if note["id"] == edit_note_id:
            found_id = True

        if found_id is True:
            note["text"] = new_text

            print("[OK] Note successfully edited")
            break

    if not found_id:
        print("[ERROR] Note ID not found")
    
def delete_note(notes, delete_id):

    is_valid_id = delete_id.isdecimal()

    if not is_valid_id:
        print("[ERROR] Note ID must be a positive integer")
        return

    delete_id = int(delete_id)

    found = False

    for i, note in enumerate(notes):
        if delete_id == note["id"]:
            del notes[i]

            found = True

            print("[OK] Note deleted")
            break

    if not found:
        print("[ERROR] Note not found")
