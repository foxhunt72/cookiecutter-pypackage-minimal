"""Console script for {{cookiecutter.package_name}}."""

{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
import argparse
{%- endif %}
import sys
{%- if cookiecutter.command_line_interface|lower == 'click' %}

import click
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}

import typer
{%- endif %}

{%- if cookiecutter.command_line_interface|lower == 'click' %}
@click.command()
def main(args=None):
    """Console script for {{cookiecutter.package_name}}."""
    click.echo(
        "Replace this message by putting your code into "
        "{{cookiecutter.package_name}}.cli.main"
    )
    click.echo("See click documentation at https://click.palletsprojects.com/")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'argparse' %}
def main(args_default=None):
    """Console script for {{cookiecutter.package_name}}."""
    parser = argparse.ArgumentParser()
    parser.add_argument('_', nargs='*')
    args = parser.parse_args(args_default)

    print("Arguments: " + str(args._))
    print("Replace this message by putting your code into "
          "{{cookiecutter.package_name}}.cli.main")
    return 0
{%- endif %}
{%- if cookiecutter.command_line_interface|lower == 'typer' %}
main = typer.Typer()

@main.command()
def run(
        args_default: str = typer.Argument(..., help="Extra help")
):
    """Console script for {{cookiecutter.package_name}}."""
    print(
        "Replace this message by putting your code into "
        "{{cookiecutter.package_name}}.cli.ryb"
    )
    typer.secho(f"Some text!", fg = typer.colors.WHITE, bg = typer.colors.RED)

    import time
    with typer.progressbar(["1", "2", "3"]) as progress:
        for test in progress:
             time.sleep(1)
    return 0
{%- endif %}


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover
