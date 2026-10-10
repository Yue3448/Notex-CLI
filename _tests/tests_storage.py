from storage import (
    load_notes,
    save_notes,
)


class TestStorage:
    def test_load_notes(self, tmp_path):
        filename = tmp_path / "notes.db"

        result = load_notes(filename)

        assert result == []

    def test_save_and_load_notes(self, tmp_path):
        filename = tmp_path / "notes.db"

        notes = [
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "date": "2026-10-10",
                "time": "09:00:00",
            },
            {
                "id": 2,
                "text": "buy vegetables",
                "completed": True,
                "date": "2026-10-10",
                "time": "12:30:00",
            },
        ]

        load_notes(filename)
        save_notes(filename, notes)
        result = load_notes(filename)

        assert result == notes
        assert result[0]["completed"] is False
        assert result[1]["completed"] is True

    def test_save_empty_notes(self, tmp_path):
        filename = tmp_path / "notes.db"
        notes = [
            {
                "id": 1,
                "text": "meet with friends",
                "completed": False,
                "date": "2026-10-10",
                "time": "09:00:00",
            },
        ]

        load_notes(filename)
        save_notes(filename, notes)
        save_notes(filename, [])

        result = load_notes(filename)

        assert result == []
