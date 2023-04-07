import click


@click.command()
@click.option("--full_name", nargs=2, default=["John", "Doe"],
        type=str, help="Your first and last name.")
def multi_value_options(full_name):
    first, last = full_name
    click.echo(f"first={first} last={last}")


if __name__=="__main__":
    multi_value_options()
