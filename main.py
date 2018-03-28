import csv
import logging
from collections import namedtuple

import click

from writers import XlsxWriter

logging.basicConfig()

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

CallRecord = namedtuple('CallRecord', [
    'gcid',
    'calling_party',
    'called_party',
    'reached_party',
    'duration',
    'datetime_connected',
    'datetime_disconnected',
    'datetime_placed'
])


def get_call_records(filename: str, criteria: list):
    """
    Retrieves records matching criteria
    :param filename: path to file
    :param criteria: list of criteria to match
    :return: yields a CallRecord namedtuple
    """

    with open(filename, mode='r', newline='') as file:
        logger.debug(f'Opening file "{filename}"')
        reader = csv.DictReader(file)

        if criteria:
            logger.info(f'Searching for the following ext(s). {criteria}')
        else:
            logger.info('No criteria specified. Parsing all entries')

        for row in reader:

            if criteria:
                if not any(ext in criteria for ext in (
                        row['callingPartyNumber'], row['originalCalledPartyNumber'], row['finalCalledPartyNumber'])):
                    continue

            # noinspection PyShadowingNames
            call_record = CallRecord(
                int(row['globalCallID_callId']),
                row['callingPartyNumber'],
                row['originalCalledPartyNumber'],
                row['finalCalledPartyNumber'],
                int(row['duration']),
                # row['duration'],
                int(row['dateTimeConnect']),
                int(row['dateTimeDisconnect']),
                int(row['dateTimeOrigination']),
            )
            yield call_record


def convert_cdr(cdr_filename: str, output_path: str, writer, criteria: list = None):
    with writer(output_path) as writer:
        for i, call_record in enumerate(get_call_records(cdr_filename, criteria)):
            writer.write(call_record, i)


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

