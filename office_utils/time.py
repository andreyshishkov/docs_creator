from datetime import datetime


def get_time():
    date = datetime.now()
    date = str(date).split('.')[0]
    date = date.replace(':', '_')
    return date
