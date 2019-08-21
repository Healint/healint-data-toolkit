import click


@click.group()
def cli():
    """
        Welcome to Healint Data Toolkit
    """
    pass


@cli.command()
def dev_endpoints():
    """
        A CLI used for development purpose only
    """
    click.echo("Hello world")


if __name__ == "__main__":
    cli()
