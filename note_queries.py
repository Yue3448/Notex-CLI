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

    if argument in ("id", "completed", "date", "time", "text"):
        sorted_notes = sorted(notes, key=lambda notes: notes[argument])
        sort_status = True

        return [sorted_notes, sort_status]

    else:
        return ["invalid_argument"]


def get_notes_in_page(notes, current_page, current_sort_argument):

    start = (current_page - 1) * 12
    end = start + 12

    if current_sort_argument:
        sorted_notes = sort_notes(notes, current_sort_argument)[0]

        return sorted_notes[start:end]

    else:
        return notes[start:end]


def search_notes(notes, query):
    query = query.lower()

    search_list = []

    for note in notes:
        if query in note["text"].lower():
            search_list.append(note)

    return search_list


def find_note(notes, find_id):

    is_valid_id = find_id.isdecimal()

    if not is_valid_id:
        return ("invalid_id", None)

    find_id = int(find_id)
    found = False

    for note in notes:
        if find_id == note["id"]:
            found = True
            return ("ok", note)

    if not found:
        return ("not_found", None)
