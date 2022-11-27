from rich.table import Table
from rich.console import Console
from readMenu import menus

table = Table(title="Menu",)

headers = list(menus[0].keys())

for header in headers:
  table.add_column(header, justify="left", style="cyan")
  
for row in menus:
  table.add_row(row['No'], row['Nama'], row['Harga'], row['Type'])
  
console = Console()
console.print(table)