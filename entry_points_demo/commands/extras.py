__all__ = ["command"]

from typing import Annotated

import typer

command = typer.Typer()

@command.command()
def greet(
        name: Annotated[str, typer.Argument(help="Whom should we greet today?")] = "te ao"
):
    """
    Prints a greeting to the screen.
    """
    print(f"Kia ora {name}!")

if __name__ == "__main__":
    command()
