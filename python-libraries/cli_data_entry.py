from rich.console import Console
from rich.table import Table
import json
import os

console = Console()

# Show example data
console.print("Here is some example movie data:", style="bold cyan")

table = Table(title="Popular Movies")
table.add_column("Year", style="cyan")
table.add_column("Title", style="magenta")
table.add_column("Box Office", justify="right")

table.add_row("2019", "Avengers Endgame", "$2.7B")
table.add_row("2021", "Spider-Man No Way Home", "$1.9B")
table.add_row("1997", "Titanic", "$2.2B")
table.add_row("2009", "Avatar", "$2.9B")
table.add_row("2018", "Black Panther", "$1.3B")

console.print(table)

console.print("\n[bold cyan]Now enter your own movie data:[/bold cyan]")

movies = []

while True:

    title = console.input("Enter movie title: ")
    year = console.input("Enter release year: ")
    box = console.input("Enter box office earnings: ")

    console.print("\n[bold yellow]You entered:[/bold yellow]")
    console.print(f"Title: {title}")
    console.print(f"Year: {year}")
    console.print(f"Box Office: {box}")

    confirm = console.input("Is this correct? (yes/no): ")

    if confirm.lower() == "yes":
        movie = {
            "title": title,
            "year": year,
            "box_office": box
        }
        movies.append(movie)
        console.print("Data confirmed!", style="green")
    else:
        console.print("Please re-enter the data.", style="red")
        continue

    more = console.input("Do you want to add another movie? (yes/no): ")

    if more.lower() != "yes":
        break

# Save data to file
filename = "movies_data.json"

with open(filename, "w") as file:
    json.dump(movies, file, indent=4)

# Show file path
path = os.path.abspath(filename)

console.print("\n[bold green]Data saved successfully![/bold green]")
console.print(f"The file is saved at: {path}")