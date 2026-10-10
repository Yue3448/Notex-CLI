from note_actions import (
    add_to_note,
    complete_task,
    delete_note,
    edit_note,
    find_note,
    search_notes,
    sort_notes,
)


class TestEditActions:
    def test_add_to_note(self):
        notes = []

        add_to_note(notes, "buy meat")

        assert len(notes) == 1
        assert notes[0]["text"] == "buy meat"
        assert notes[0]["completed"] is False

    def test_sort_note_by_id(self):
        notes = [
            {"id": 2, "text": "buy vegetables"},
            {"id": 1, "text": "meet with friends"},
        ]

        result = sort_notes(notes, "id")

        assert isinstance(result, list)
        assert result[0] == [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]
        assert result[1] is True

    def test_sort_note_by_status(self):
        notes = [
            {"id": 2, "text": "buy vegetables", "completed": True},
            {"id": 1, "text": "meet with friends", "completed": False},
        ]

        result = sort_notes(notes, "completed")

        assert isinstance(result, list)
        assert result[0] == [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": True},
        ]
        assert result[1] is True

    def test_sort_note_by_date(self):
        notes = [
            {
                "id": 2,
                "text": "buy vegetables",
                "completed": True,
                "date": "2026-10-10",
            },
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "date": "2025-12-31",
            },
        ]

        result = sort_notes(notes, "date")

        assert isinstance(result, list)
        assert result[0] == [
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "date": "2025-12-31",
            },
            {
                "id": 2,
                "text": "buy vegetables",
                "completed": True,
                "date": "2026-10-10",
            },
        ]
        assert result[1] is True

    def test_sort_note_by_time(self):
        notes = [
            {
                "id": 2,
                "text": "buy vegetables",
                "completed": True,
                "time": "18:30:00",
            },
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "time": "09:05:00",
            },
        ]

        result = sort_notes(notes, "time")

        assert isinstance(result, list)
        assert result[0] == [
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "time": "09:05:00",
            },
            {
                "id": 2,
                "text": "buy vegetables",
                "completed": True,
                "time": "18:30:00",
            },
        ]
        assert result[1] is True

    def test_complete_all_tasks(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": False},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "y")
        result = complete_task(notes, "all")

        assert result == "all notes completed"
        assert notes[0]["completed"] is True
        assert notes[1]["completed"] is True

    def test_cancel_complete_all_tasks(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": False},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "n")
        result = complete_task(notes, "all")

        assert result == "complete cancelled"
        assert notes[0]["completed"] is False
        assert notes[1]["completed"] is False

    def test_complete_all_tasks_wrong_command(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": False},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "qwerty")
        result = complete_task(notes, "all")

        assert result == "Wrong command"

    def test_complete_all_tasks_not_found(self):
        notes = [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": False},
        ]

        result = complete_task(notes, "99")

        assert result == "not_found"

    def test_complete_all_tasks_invalid_id(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "qwerty")
        result = complete_task(notes, "qwerty")

        assert result == "invalid_id"

    def test_complete_task(self):
        notes = [
            {"id": 1, "text": "meet with friends", "completed": False},
            {"id": 2, "text": "buy vegetables", "completed": False},
        ]

        result = complete_task(notes, "1")

        assert result == "completed"
        assert notes[0]["completed"] is True

    def test_edit_note(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = edit_note(notes, "1", "stay home")

        assert result == "edited"
        assert notes[0]["text"] == "stay home"

    def test_edit_note_not_found(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = edit_note(notes, "99", "stay home")

        assert result == "not_found"

    def test_edit_note_invalid_id(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = edit_note(notes, "qwerty", "stay home")

        assert result == "invalid_id"


class TestFindActions:
    def test_find_note(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = find_note(notes, "2")

        assert result[0] == "ok"
        assert result[1] == {"id": 2, "text": "buy vegetables"}

    def test_search_notes(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = search_notes(notes, "friend")

        assert result  # ВЕРНУТЬСЯ!


class TestDeleteActions:
    def test_delete_note(self):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        result = delete_note(notes, "1")

        assert result == "deleted"
        assert notes == [{"id": 2, "text": "buy vegetables"}]

    def test_delete_all_notes(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "y")
        result = delete_note(notes, "all")

        assert result == "all notes deleted"
        assert notes == []

    def test_cancel_all_notes_delete(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "n")
        result = delete_note(notes, "all")

        assert result == "delete cancelled"

    def test_wrong_delete_command(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "qwerty")
        result = delete_note(notes, "all")

        assert result == "Wrong command"

    def test_not_found_id_delete(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "99")
        result = delete_note(notes, "99")

        assert result == "not_found"

    def test_invalid_id_delete(self, monkeypatch):
        notes = [
            {"id": 1, "text": "meet with friends"},
            {"id": 2, "text": "buy vegetables"},
        ]

        monkeypatch.setattr("builtins.input", lambda prompt: "qwerty")
        result = delete_note(notes, "qwerty")

        assert result == "invalid_id"
