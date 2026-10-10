from note_queries import find_note, search_notes, sort_notes


class TestEditActions:
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

