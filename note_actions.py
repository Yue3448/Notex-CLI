from datetime import date

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

    current_date = str(date.today())

    if len(notes) == 0:
        notes.append({"id": 1, "text": text, "completed": False, "date": current_date})

    else:
        new_id = notes[-1]["id"] + 1
        notes.append({"id": new_id, "text": text, "completed": False, "date": current_date})

    return "created"

def complete_task(notes, complete_id):

    is_valid_id = complete_id.isdecimal()

    if not is_valid_id:
        return "invalid_id"

    complete_id = int(complete_id)

    find_flag = False

    for note in notes:
        if note["id"] == complete_id:
            find_flag = True

            note["completed"] = True

            return "completed"

    if not find_flag:
        return "not_found"

def uncomplete_task(notes, uncomplete_id):

    is_valid_id = uncomplete_id.isdecimal()

    if not is_valid_id:
        return "invalid_id"

    uncomplete_id = int(uncomplete_id)

    find_flag = False

    for note in notes:
        if note["id"] == uncomplete_id:
            find_flag = True

            note["completed"] = False

            return "uncompleted"

    if not find_flag:
        return "not_found"

def edit_note(notes, edit_note_id, new_text):

    is_valid_id = edit_note_id.isdecimal()

    if not is_valid_id:
        return 'invalid_id'

    edit_note_id = int(edit_note_id)

    found_id = False

    for note in notes:
        if note["id"] == edit_note_id:
            found_id = True

        if found_id is True:
            note["text"] = new_text

            return 'edited'

    if not found_id:
        return 'not_found'
    
def delete_note(notes, delete_id):

    is_valid_id = delete_id.isdecimal()

    if not is_valid_id:
        return 'invalid_id'

    delete_id = int(delete_id)

    found = False

    for i, note in enumerate(notes):
        if delete_id == note["id"]:
            del notes[i]

            found = True

            return 'deleted'

    if not found:
        return 'not_found'
