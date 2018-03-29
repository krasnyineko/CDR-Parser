from datetime import datetime, timedelta
from xlsxwriter import Workbook

from cdrparser.utils import epoch_date, epoch_time
from .writer import Writer


class XlsxWriter(Writer):
    def __init__(self, filename):
        super().__init__(filename)
        self.workbook = Workbook(filename)
        self.worksheet = self.workbook.add_worksheet()
        _format_header = self.workbook.add_format({'bold': True, 'align': 'center'})
        self._format_date = self.workbook.add_format({'num_format': 'mmm dd yyyy', 'align': 'left'})
        self._format_time = self.workbook.add_format({'num_format': 'hh:mm AM/PM', 'align': 'left'})
        self._format_duration = self.workbook.add_format({'num_format': 'hh:mm:ss', 'align': 'left'})

        self.worksheet.write('A1', 'Date', _format_header)
        self.worksheet.write('B1', 'Time', _format_header)
        self.worksheet.write('C1', 'Calling Number', _format_header)
        self.worksheet.write('D1', 'Called Number', _format_header)
        self.worksheet.write('E1', 'Received Number', _format_header)
        self.worksheet.write('F1', 'Duration', _format_header)
        self.worksheet.write('G1', 'Time Connected', _format_header)
        self.worksheet.write('H1', 'Time Disconnected', _format_header)
        self.worksheet.write('I1', 'Call Type', _format_header)
        self.worksheet.write('J1', 'Call ID', _format_header)
        self.worksheet.set_column(0, 8, 18)

    def close(self):
        self.workbook.close()

    def write(self, item, row):
        self.worksheet.write(row + 1, 0, epoch_date(item.datetime_placed), self._format_date)
        self.worksheet.write(row + 1, 1, epoch_time(item.datetime_placed), self._format_time)

        self.worksheet.write(row + 1, 2, item.calling_party)
        self.worksheet.write(row + 1, 3, item.called_party)
        self.worksheet.write(row + 1, 4, item.reached_party)
        self.worksheet.write(row + 1, 5, timedelta(seconds=item.duration), self._format_duration)

        if item.datetime_connected != 0:
            self.worksheet.write(row + 1, 6, epoch_time(item.datetime_connected), self._format_time)
        else:
            self.worksheet.write(row + 1, 6, 'N/A')

        self.worksheet.write(row + 1, 7, epoch_time(item.datetime_disconnected), self._format_time)

        call_type = 'Simple' if item.called_party == item.reached_party else 'Forward'
        self.worksheet.write(row + 1, 8, call_type)
        self.worksheet.write(row + 1, 9, item.gcid)
