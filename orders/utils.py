import datetime
import calendar

def format_date_time(date_time):
    suffix = "th" if 11 <= date_time.day <= 13 else {1: "st", 2: "nd", 3: "rd"}.get(date_time.day % 10, "th")
    return f"{date_time.strftime('%d{suffix} %b %Y, %A, %I:%M %p')}".format(suffix=suffix)