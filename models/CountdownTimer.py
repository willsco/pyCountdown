import datetime

class CountdownTimer:
    def __init__(self, target_date_str):
        self.target_date = datetime.datetime.strptime(target_date_str, "%Y-%m-%d %H:%M:%S")

    def get_time_remaining(self):
        current_date = datetime.datetime.now()
        time_left = self.target_date - current_date
        return time_left if time_left.total_seconds() > 0 else datetime.timedelta(0)
