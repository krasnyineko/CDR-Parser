from .writer import Writer
from .xlsxwriter import XlsxWriter
from .csvwriter import CsvWriter

writers = {
    'xlsx': {
        'ext': 'xlsx',
        'class': XlsxWriter
    },
    'csv': {
        'ext': 'csv',
        'class': CsvWriter
    }
}
