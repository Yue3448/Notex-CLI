import sqlite3


def load_notes(filename):
    connection = sqlite3.connect(filename)

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS note (
            id INTEGER PRIMARY KEY,
            text TEXT NOT NULL,
            completed INTEGER DEFAULT 0 CHECK (completed IN (0, 1)),
            date TEXT NOT NULL,
            time TEXT NOT NULL
            )
        """)
        connection.commit()

        result = connection.execute("""
            SELECT id, text, completed, date, time FROM note ORDER BY id
        """)

        rows = result.fetchall()

        notes = []

        for row in rows:
            note = {
                "id": row[0],
                "text": row[1],
                "completed": bool(row[2]),
                "date": row[3],
                "time": row[4],
            }
            notes.append(note)
        return notes

    finally:
        connection.close()


def save_notes(filename, notes):
    connection = sqlite3.connect(filename)

    try:
        connection.execute("""DELETE FROM note""")
        for item in notes:
            connection.execute(
                """
                INSERT INTO note (id, text, completed, date, time)
                VALUES (?, ?, ?, ?, ?)
            """,
                (
                    item["id"],
                    item["text"],
                    int(item["completed"]),
                    item["date"],
                    item["time"],
                ),
            )
        connection.commit()

    except Exception:
        connection.rollback()
        raise

    finally:
        connection.close()
