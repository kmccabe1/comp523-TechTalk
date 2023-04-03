import click

@click.command()
# Options can be given default values and custom help messages.
@click.option("--count", "-c", default=1, help="Number of goodbyes.")
# Prompt will ask the user for input for the option.
@click.option("--name", prompt="Your name", help="The person to say goodbye to.")
def say_goodbye(count, name):
    # Add a docstring that will be used by the --help option.
    """Say goodbye to the user."""
    for i in range(count):
        click.echo(f"Goodbye {name}.")


if __name__=="__main__":
    say_goodbye()

