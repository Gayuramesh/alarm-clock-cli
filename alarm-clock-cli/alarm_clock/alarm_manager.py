from alarm_clock.alarm import Alarm
from alarm_clock.utils import parse_alarm_time


class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, time_str):

        alarm_time = parse_alarm_time(time_str)

        if alarm_time is None:
            return False, "Invalid time format. Use HH:MM."

        if any(a.display_time == time_str for a in self.alarms):
            return False, "An alarm already exists for this time."

        self.alarms.append(Alarm(alarm_time))

        self.alarms.sort(key=lambda x: x.alarm_time)

        return True, "Alarm added successfully."

    def list_alarms(self):
        return self.alarms

    def delete_alarm(self, index):

        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)
            return True

        return False