from datetime import datetime


def epoch_date(epoch):
    return datetime.fromtimestamp(epoch).date()


def epoch_time(epoch):
    return datetime.fromtimestamp(epoch).time()
