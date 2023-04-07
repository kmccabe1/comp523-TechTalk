import click


@click.command()
@click.argument("filename", type=click.Path(exists=True))
def get_fname(filename):
    """Print FILENAME with path removed."""
    click.echo(click.format_filename(filename, shorten=True))


if __name__ == "__main__":
    get_fname()
