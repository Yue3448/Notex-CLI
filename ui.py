from datetime import date, timedelta

from rich.align import Align
from rich.console import Console, Group
from rich.constrain import Constrain
from rich.progress_bar import ProgressBar
from rich.rule import Rule
from rich.table import Table
from rich.text import Text
from rich.theme import Theme

from config import MAX_WIDTH
from note_queries import complete_notes_counter, find_note, get_notes_in_page

themes = Theme(
    {
        "error": "bold red",
        "accent": "bold white",
        "done": "bold green",
        "warning": "bold yellow",
        "muted": "bright_black",
    }
)

console = Console(theme=themes)


def render_interface(
    notes, error_code, current_page, max_pages, current_sort_argument, current_query
):
    console.clear()

    if current_query:
        show_search_logo()
    else:
        show_logo()

    width = min(console.width, MAX_WIDTH)
    notes_in_page = get_notes_in_page(notes, current_page, current_sort_argument)

    console.print(
        Constrain(
            Group(
                show_header(current_sort_argument, current_query),
                show_notes_list(notes_in_page, width, current_query),
                show_footer(notes, current_page, max_pages),
            ),
            width,
        )
    )

    show_error(error_code)


def render_help_shell():
    show_help_logo()
    help_shell()


def show_header(current_sort_argument, current_query):
    if current_query:
        mode_info = f'search: "{current_query}"'
    else:
        mode_info = f"sort: {current_sort_argument or 'none'}"

    title = f"[accent]NOTEX · v0.9.9[/] [muted]·[/] {mode_info}"

    return Rule(title, align="left", style="muted")


def format_date(note_date):
    if note_date == str(date.today()):
        return "today"

    if note_date == str(date.today() - timedelta(days=1)):
        return "yday"

    _year, month, day = note_date.split("-")
    return f"{day}.{month}"


def note_line(note, text_width, current_query):
    text_style = "dim strike" if note["completed"] else "accent"

    text = Text(note["text"].strip(), style=text_style)

    if current_query:
        text.highlight_words([current_query], style="reverse", case_sensitive=False)

    text.truncate(text_width, overflow="ellipsis")

    dots_count = text_width - text.cell_len - 1

    if dots_count > 1:
        text.append(" " + "·" * dots_count, style="muted")

    return text


def show_notes_list(notes_in_page, width, current_query):
    if not notes_in_page:
        empty_text = "Nothing found" if current_query else "No notes yet — add <text>"
        return Align.center(Text(f"\n{empty_text}\n", style="muted"))

    id_width = max(len(str(note["id"])) for note in notes_in_page)
    time_width = 5
    date_width = 6

    text_width = width - (1 + 1 + id_width + time_width + date_width + 5)

    table_object = Table.grid(padding=(0, 1))
    table_object.show_header = True
    table_object.header_style = "muted"

    table_object.add_column("", width=1)
    table_object.add_column("", width=1)
    table_object.add_column("#", width=id_width, justify="right")
    table_object.add_column("NOTE", width=text_width, no_wrap=True)
    table_object.add_column("TIME", width=time_width)
    table_object.add_column("DATE", width=date_width, justify="right")

    previous_date = None

    for note in notes_in_page:
        note_date = note.get("date", "-")

        if note_date == previous_date:
            date_info = ""
        elif note_date == "-":
            date_info = "-"
        else:
            date_info = format_date(note_date)

        previous_date = note_date

        if note["completed"]:
            bar = "[dim green]▎[/]"
            status_icon = "[dim green]✓[/]"
            info_style = "dim"
        else:
            bar = "[yellow]▎[/]"
            status_icon = "[warning]○[/]"
            info_style = "muted"

        if date_info == "today":
            date_info = "[accent]today[/]"

        table_object.add_row(
            bar,
            status_icon,
            f"[{info_style}]{note['id']}[/]",
            note_line(note, text_width, current_query),
            f"[{info_style}]{str(note['time'])[:5]}[/]",
            f"[{info_style}]{date_info}[/]",
        )

    return table_object


def render_note(notes, show_id):

    note = find_note(notes, show_id)
    note_text = note[1]["text"]
    note_id = note[1]["id"]
    note_data = note[1]["date"]
    note_time = note[1]["time"]

    show_text = f"""
███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝

────────────────
[ID: {note_id}]

{note_text}

────────────────
[DATE] {note_data} {note_time}
"""
    console.print(show_text)


def show_error(error_code):
    if error_code in errors:
        console.print(errors[error_code])


def show_footer(notes, current_page, max_pages):
    total = len(notes)
    completed = complete_notes_counter(notes)

    progress = ProgressBar(
        total=max(total, 1),
        completed=completed,
        width=20,
        style="muted",
        complete_style="green",
        finished_style="green",
    )

    footer_grid = Table.grid(padding=(0, 1), expand=True)
    footer_grid.add_column(width=20)
    footer_grid.add_column(ratio=1)
    footer_grid.add_column(ratio=1, justify="center")
    footer_grid.add_column(ratio=1, justify="right")

    footer_grid.add_row(
        progress,
        f"[accent]{completed}[/][muted]/{total} done[/]",
        f"[muted]‹[/] [accent]{current_page}[/][muted]/{max_pages} ›[/]",
        "[muted]? help[/]",
    )

    return Group(Rule(style="muted"), footer_grid)


def help_shell():
    help_shell_string = """
 usage: <command> <argument>

 [accent]Notes[/]
   add, new      <text>          Create a new note
   edit, ed, e   <id> <text>     Change note text
   del, rm       <id> | all      Delete note(s)
   show, sh      <id>            Open full note

 [accent]Status[/]
   done, do      <id> | all      Mark as completed
   undone, undo  <id> | all      Mark as not completed

 [accent]View[/]
   sort           <field>        Sort by id, text, date, time or completed
   search, find   <text>         Find notes by text
   quit, q        search         Quit search mode
   next, nx                      Next page
   back, bc                      Previous page

 [accent]Other[/]
   help, h, ?                    Show this help
   quit, q                       Exit
"""
    console.print(help_shell_string)


def show_logo():
    console.print()
    logo = """
 ███╗   ██╗ ██████╗ ████████╗███████╗██╗  ██╗
 ████╗  ██║██╔═══██╗╚══██╔══╝██╔════╝╚██╗██╔╝
 ██╔██╗ ██║██║   ██║   ██║   █████╗   ╚███╔╝
 ██║╚██╗██║██║   ██║   ██║   ██╔══╝   ██╔██╗
 ██║ ╚████║╚██████╔╝   ██║   ███████╗██╔╝ ██╗
 ╚═╝  ╚═══╝ ╚═════╝    ╚═╝   ╚══════╝╚═╝  ╚═╝
    """

    console.print(logo)


def show_help_logo():
    console.print()
    help_logo = """
 ██╗  ██╗███████╗██╗     ██████╗
 ██║  ██║██╔════╝██║     ██╔══██╗
 ███████║█████╗  ██║     ██████╔╝
 ██╔══██║██╔══╝  ██║     ██╔═══╝
 ██║  ██║███████╗███████╗██║
 ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝
"""
    console.print(help_logo)


def show_search_logo():
    console.print()
    search_logo = """
 ███████╗███████╗ █████╗ ██████╗  ██████╗██╗  ██╗
 ██╔════╝██╔════╝██╔══██╗██╔══██╗██╔════╝██║  ██║
 ███████╗█████╗  ███████║██████╔╝██║     ███████║
 ╚════██║██╔══╝  ██╔══██║██╔══██╗██║     ██╔══██║
 ███████║███████╗██║  ██║██║  ██║╚██████╗██║  ██║
 ╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝╚═╝  ╚═╝
"""
    console.print(search_logo)


help_string = """
[error]ERROR:[/] unavailable command
type "help" for check available commands
"""
errors = {
    1: "[error]ERROR:[/] missing note id",
    2: "[accent]No notes found[/]",
    3: "[error]ERROR:[/] No id and new text",
    4: "[error]ERROR:[/] Invalid id",
    5: "[error]ERROR:[/] No new text",
    6: help_string,
    7: "[error]ERROR:[/] Missing note text",
    8: "[error]ERROR:[/] Wrong command",
    9: "[error]ERROR: [/] Invalid id or can't found note",
    10: "[warning]Action was cancelled[/]",
    11: "[accent]You're at the last page[/]",
    12: "[accent]You're at the first page[/]",
    13: "[error]ERROR:[/] Invalid argument",
}
