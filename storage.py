import json

def load_notes(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            notes = json.load(file)

        return notes

    except FileNotFoundError:
        return []
    
def save_notes(filename, notes):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(notes, file, ensure_ascii=False, indent=4)