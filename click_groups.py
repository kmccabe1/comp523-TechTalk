import click

# Group will be the entrypoint to multi commands.
@click.group(chain=True)
# Setting chain to true allows subcommands to be chained together.
@click.option("--count", default=0, help="Count starting from this number.")
# Use this decorator to pass context between commands.
@click.pass_context
def entrypoint(ctx, count):
    # Ensure ctx.obj exists
    ctx.ensure_object(dict)
    ctx.obj["COUNT"] = count
    # Now any command that passes context will have access to COUNT.
    click.echo(f"Count is {count} in entrypoint.")


# Subcommands must use the group function name not click.
@entrypoint.command()
@click.option("--num", default=0)
@click.pass_context
def add(ctx, num):
    """Add num to count."""
    ctx.obj["COUNT"] = ctx.obj["COUNT"] + num
    click.echo("Count is now " + str(ctx.obj["COUNT"]) + " in add.")

@entrypoint.command()
@click.option("--num", default=0)
@click.pass_context
def sub(ctx, num):
    """Subtract num from count."""
    ctx.obj["COUNT"] = ctx.obj["COUNT"] - num
    click.echo("Count is now " + str(ctx.obj["COUNT"]) + " in sub.")

@entrypoint.command()
@click.option("--num", default=0)
@click.pass_context
def multiply(ctx, num):
    """Multiply count by num."""
    ctx.obj["COUNT"] = ctx.obj["COUNT"] * num
    click.echo("Count is now " + str(ctx.obj["COUNT"]) + " in multiply.")
    

if __name__ == "__main__":
    # To pass a program defined context invoke the entrypoint with the specified object
    entrypoint(obj={})
    
