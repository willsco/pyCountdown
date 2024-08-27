import datetime


def get_time_remaining(target_date_str):
    target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")
    return target_date
