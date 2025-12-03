
from datetime import datetime

def get_weekday(date_string):
    date_format = "%Y-%m-%d"
    date_object = datetime.strptime(date_string, date_format)
    weekday = date_object.strftime("%A")
    return weekday



