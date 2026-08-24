from rich.console import Console
from rich.table import Table

console = Console()

table = Table(
    title="Мои предметы",
    caption='Total: 0 | Completed: 0 | Remaining: 0'
)

table.add_column("Предмет", style="cyan", no_wrap=True)
table.add_column("Оценка", justify="right", style="green")
table.add_column("Статус", style="magenta")

table.add_row("Python", "5", "Готово")
table.add_row("Алгоритмы", "4", "В процессе")
table.add_row("Английский", "5", "Готово")

console.print(table)