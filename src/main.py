# src/main.py
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from authentication import register_user, login_user

console = Console()

def show_menu():
    console.clear()
    table = Table(title="SEO Bot Menu")
    table.add_column("Option", justify="center", style="cyan", no_wrap=True)
    table.add_column("Description", style="magenta")

    options = [
        ("1", "Register new user"),
        ("2", "Login"),
        ("3", "Exit")
    ]

    for option, description in options:
        table.add_row(option, description)

    console.print(table)

def main():
    authenticated_user = None
    user_role = None

    while True:
        show_menu()
        choice = Prompt.ask("Enter your choice", choices=["1", "2", "3"])

        if choice == "1":
            register_user()
        elif choice == "2":
            authenticated_user, user_role = login_user()
        elif choice == "3":
            console.print("Exiting...", style="bold red")
            break

if __name__ == "__main__":
    main()
