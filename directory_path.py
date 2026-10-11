from pathlib import Path


def get_database_path():
    data_dir = Path.home() / ".notex"
    data_dir.mkdir(parents=True, exist_ok=True)

    file_db = data_dir / "notes.db"

    return file_db
