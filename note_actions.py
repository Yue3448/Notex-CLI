from datetime import date
from datetime import datetime

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

def sort_notes(notes, argument):

    sort_status = False

    if argument in ('id', 'completed', 'date', 'time', 'text'):

        sorted_notes = sorted(notes, key=lambda notes: notes[argument])
        sort_status = True

        return [sorted_notes, sort_status]

    else:
        return ['invalid_argument']
    
def get_notes_in_page(notes, current_page, current_sort_argument):

    start = (current_page - 1) * 12
    end = start + 12

    if current_sort_argument:
        sorted_notes = sort_notes(notes, current_sort_argument)[0]

        return sorted_notes[start:end]

    else:
        return notes[start:end]

def search_notes(notes, query):
    pass

def find_note(notes, find_id):
    
    is_valid_id = find_id.isdecimal()

    if not is_valid_id:
        return ('invalid_id', None)

    find_id = int(find_id)
    found = False
    
    for note in notes:
        if find_id == note["id"]:
            found = True
            return ('ok', note)
        
    if not found:
        return ('not_found', None)
    
def add_to_note(notes, text):

    current_date = str(date.today())
    current_time = datetime.now().strftime("%H:%M:%S")

    ids = [note['id'] for note in notes]

    if len(ids) > 0:
        max_id = max(ids)

    if len(notes) == 0:
        notes.append({"id": 1, "text": text, "completed": False, "date": current_date, "time": current_time})

    else:
        new_id = max_id + 1
        notes.append({"id": new_id, "text": text, "completed": False, "date": current_date, "time": current_time})

    return "created"

def complete_task(notes, complete_id):

    argument_flag = False
    
    if complete_id.lower() == 'all':
        complete_all_accept = input('Complete ALL notes? [Y/N](default N): ')

        if complete_all_accept.lower() == 'y':
            argument_flag = True

        elif complete_all_accept.lower() in ('n', ''):
            return 'complete cancelled'

        else:
            return 'Wrong command'

        if argument_flag:
            for note in notes:
                if not note["completed"]:
                    note["completed"] = True

            return "all notes completed"
    
    is_valid_id = complete_id.isdecimal()

    if not is_valid_id:
        return "invalid_id"

    else:
        complete_id = int(complete_id)

        find_flag = False

        for note in notes:
            if note["id"] == complete_id:
                find_flag = True
            
                note["completed"] = True

                return "completed"

        if not find_flag:
            return "not_found"

def delete_note(notes, delete_id):

    argument_flag = False

    if delete_id.lower() == 'all':

        delete_all_accept = input('Are you really want to delete ALL notes? [Y/N](default N): ')

        if delete_all_accept.lower() == 'y':
            argument_flag = True

        elif delete_all_accept.lower() in ('n', ''):
            return 'delete cancelled'

        else:
            return 'Wrong command'

        if argument_flag:
            notes.clear()
            return 'all notes deleted'

    is_valid_id = delete_id.isdecimal()

    if not is_valid_id:
        return 'invalid_id'

    else:
        delete_id = int(delete_id)
        found = False

        for i, note in enumerate(notes):
            if delete_id == note["id"]:
                del notes[i]

                found = True

                return 'deleted'
    
        if not found:
            return 'not_found'

def uncomplete_task(notes, uncomplete_id):

    argument_flag = False
    
    if uncomplete_id.lower() == 'all':
        uncomplete_all_accept = input('Are you really want to delete ALL notes? [Y/N](default N): ')

        if uncomplete_all_accept.lower() == 'y':
            argument_flag = True

        elif uncomplete_all_accept.lower() in ('n', ''):
            return 'uncomplete cancelled'

        else:
            return 'Wrong command'

        if argument_flag:
            for note in notes:
                if note["completed"]:
                    note["completed"] = False

            return "all notes uncompleted"

    is_valid_id = uncomplete_id.isdecimal()

    if not is_valid_id:
        return "invalid_id"

    else:
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
    