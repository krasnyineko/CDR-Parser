import logging
import click

from cdrparser.main import convert_cdr
from cdrparser.writers import writers

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@click.command()
@click.argument('cdr_csv', type=click.Path(exists=True))
@click.option('--output', '-o', default=None)
@click.argument('criteria', nargs=-1)
@click.option('--format', '-f', type=click.Choice(writers.keys()), default='xlsx')
def main(cdr_csv, output, criteria, format):
    if output is None:
        import time
        output = time.strftime(f'%Y-%m-%d_%H%M%S.{writers[format]["ext"]}')

    convert_cdr(cdr_csv, output, writers[format]['class'], criteria)


if __name__ == '__main__':
    main()
