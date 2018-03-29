import logging
import click

from cdrparser.main import convert_cdr
from cdrparser.writers import XlsxWriter

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


@click.command()
@click.argument('cdr_csv', type=click.Path(exists=True))
@click.option('--output', '-o', default=None)
@click.argument('criteria', nargs=-1)
def main(cdr_csv, output, criteria):
    if output is None:
        import time
        output = time.strftime('%Y-%m-%d_%H%M%S.xlsx')

    convert_cdr(cdr_csv, output, XlsxWriter, criteria)


if __name__ == '__main__':
    main()
