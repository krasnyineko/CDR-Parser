from csv import DictWriter
from datetime import timedelta

from cdrparser.utils import epoch_date, epoch_time
from cdrparser.writers import Writer


class CsvWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)
        fieldname = [
            'Date',
            'Time',
            'Calling Number',
            'Called Number',
            'Received Number',
            'Duration',
            'Time Connected',
            'Time Disconnected',
            'Cally Type',
            'Call ID'
        ]
        self.file = open(filename, 'w')
        self.writer = DictWriter(self.file, fieldname)
        self.writer.writeheader()

    def write(self, item, row):

        call_type = 'Simple' if item.reached_party == item.called_party else 'Forward'
        self.writer.writerow({
            'Date': epoch_date(item.datetime_placed),
            'Time': epoch_time(item.datetime_placed),
            'Calling Number': item.calling_party,
            'Called Number': item.called_party,
            'Received Number': item.reached_party,
            'Duration': timedelta(seconds=item.duration),
            'Time Connected': epoch_time(item.datetime_connected),
            'Time Disconnected': epoch_time(item.datetime_disconnected),
            'Cally Type': call_type,
            'Call ID': item.gcid
        })

    def close(self):
        self.file.close()