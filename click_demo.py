import click

@click.command()
def say_goodbye():
    click.echo("Goodbye")


if __name__=="__main__":
    say_goodbye()
