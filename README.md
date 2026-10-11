<div align="center">

# NOTEX-CLI
A terminal workspace for capturing notes, tracking tasks, and keeping your next move in sight.

![Version](https://img.shields.io/badge/version-1.0.0-22c55e?style=flat-square)
![Python](https://img.shields.io/badge/built_with-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![SQLite](https://img.shields.io/badge/storage-SQLite-003B57?style=flat-square&logo=sqlite&logoColor=white)
![Local](https://img.shields.io/badge/local-first-f59e0b?style=flat-square)

[Quick start](#quick-start) · [Commands](#command-reference) · [Development](#development)

</div>

## Meet NOTEX

NOTEX-CLI brings notes and tasks into one interactive terminal interface, with short commands, highlighted search results, and a local SQLite database. Once installed, it works offline. Your notes stay on your machine.


```text
 ███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
 ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
 ██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
 ██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
 ██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
 ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝

NOTEX · v1.0.0 · sort: none ────────────────────────────────────────────
    # NOTE                                                  TIME    DATE
▎ ✓ 1 Write the README ···································· 10:24  today
▎ ○ 2 Explore SQLite ······································ 10:27
▎ ○ 3 Capture the next project idea ······················· 10:31
────────────────────────────────────────────────────────────────────────
━━━━━━╸              1/3 done             ‹ 1/1 ›                 ? help

notex>
```

*Example view. In the terminal, active and completed notes have distinct colors, and completed text is dimmed and struck through.*

## What you can do

- **Capture and refine.** Create notes, edit their text, and open the full content of longer entries.
- **Track progress.** Mark tasks as done, reopen them, and see a completion counter and progress bar.
- **Find your focus.** Search by text with case-insensitive matching and highlighted results.
- **Choose your view.** Sort by ID, text, date, time, or completion status. Browse 12 notes per page.
- **Keep it local.** Changes are saved automatically to SQLite after each successful create, edit, status change, or deletion.
- **Move with short commands.** Use aliases such as `add`, `do`, `rm`, and `q`. Open built-in help with `?`.

## Quick start

You need Python 3, pip, and Git. SQLite support comes with Python; the installation below installs the terminal UI dependencies.

```bash
git clone https://github.com/Yue3448/Notex-CLI.git
cd Notex-CLI
python3 -m venv .venv
source .venv/bin/activate
python -m pip install .
notex
```

<details>
<summary>Windows (PowerShell)</summary>

```powershell
git clone https://github.com/Yue3448/Notex-CLI.git
cd Notex-CLI
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install .
notex
```

If your PowerShell configuration blocks activation, run the environment's Python and entry point directly:

```powershell
.\.venv\Scripts\python.exe -m pip install .
.\.venv\Scripts\notex.exe
```

</details>

You can also launch the application from the repository with `python main.py` after installing its dependencies.

## First session

Enter these commands at the application's `notex>` prompt. On a fresh database, the first two notes receive IDs `1` and `2`.

```text
add Write the README
add Explore SQLite
done 1
edit 2 Build a small project with SQLite
search SQLite
q search
sort completed
q
```

Text goes directly after the command; quotes are unnecessary. Use `show 2` to read a note in full. On the note or help screen, press Enter to return to the list.

## Command reference

These are commands inside NOTEX, rather than shell arguments to the `notex` executable. `<id>` is the number shown in the `#` column.

| Command | Aliases | What it does |
| --- | --- | --- |
| `add <text>` | `new` | Create a note with a creation date and time. |
| `edit <id> <text>` | `ed`, `e` | Replace a note's text. |
| `show <id>` | `sh` | Open the full note. |
| `done <id>` | `do` | Mark a note as completed. |
| `undone <id>` | `undo` | Mark a note as not completed. |
| `remove <id>` | `rm`, `del` | Delete a note. |
| `search <text>` | `find` | Filter notes by a substring of their text. |
| `q search` | `quit search`, `q find`, `quit find` | Leave search mode and return to all notes. |
| `sort <field>` | — | Sort the current view in ascending order. |
| `next` | `nx` | Go to the next page. |
| `back` | `bc` | Go to the previous page. |
| `help` | `h`, `?` | Open the command guide. |
| `quit` | `q` | Exit the application. |

**Sorting fields:** `id`, `text`, `date`, `time`, and `completed`. Use `sort completed` to put unfinished notes first. Sorting applies to the current session.

**Search mode:** the filter stays active while you work. The counter and progress bar reflect the matching notes. Run `q search` to clear the filter; running `search` without text also clears it.

**Bulk actions:** `done all`, `undone all`, and `remove all` ask for confirmation. Enter `y` to proceed, or press Enter to cancel. These actions affect every note in the database, including notes outside the current search results. Deleting a single note with `remove <id>` happens immediately.

## Storage

NOTEX creates `notes.db` in the **directory you launch it from**. Start it from the same directory to keep using the same collection; starting elsewhere creates or opens a different database.

Each note stores an ID, text, completion status, and creation date and time. Editing the text preserves the original timestamp. The database is excluded from Git by `.gitignore`.

To back up your collection, exit NOTEX and copy `notes.db`. To restore it, place the copy in the directory you use to launch the application.

## Under the hood

The project separates command handling, note operations, queries, storage, and rendering into small modules.

```text
Notex-CLI/
├── main.py           # Launch from source
├── commands.py       # Interactive loop and command handling
├── note_actions.py   # Create, edit, delete, and change status
├── note_queries.py   # Search, sorting, pagination, and counters
├── storage.py        # SQLite persistence
├── ui.py             # Terminal interface and built-in help
├── config.py         # Interface width setting
├── tests/            # Tests for actions, queries, and storage
└── pyproject.toml    # Package metadata, dependencies, and notex entry point
```

**Python** powers the application, **Rich** renders the interface, **prompt_toolkit** handles interactive input, and **SQLite** stores the notes.

## Development

With the virtual environment activated, install the project in editable mode and add pytest:

```bash
python -m pip install -e .
python -m pip install pytest
python -m pytest -q
```

Editable installation makes source changes available the next time you launch `notex`. The test suite covers note actions, search and sorting, and SQLite persistence; storage tests use temporary databases.

Have an idea or found a bug? [Open an issue](https://github.com/Yue3448/Notex-CLI/issues)

Author - [Yue3448](https://github.com/Yue3448)

This is my first serious educational project. An AI coding assistant helped me with parts of the tests, project packaging, and terminal UI layout. No more than.

## License

This project is licensed under the [MIT License](LICENSE).
