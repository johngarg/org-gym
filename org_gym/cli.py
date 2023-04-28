import click
from org_gym.parser import parse_gym_file

@click.group()
@click.version_option()
def cli():
    "A tool for working with fitness data in orgmode."


@cli.command(name="parse")
@click.argument(
    "orgfile"
)
@click.option(
    "-o",
    "--output",
    help="Path to output csv file.",
    default="output.csv",
)
def parse(orgfile, output):
    "Parse an orgmode file and output a csv file."
    dataframe = parse_gym_file(orgfile)
    dataframe.to_csv(path_or_buf=output)
    click.echo(f"CSV file written to {output}")
