
from alarm_clock.alarm import Alarm
from alarm_clock.utils import parse_alarm_time


class AlarmManager:

    def __init__(self):
        self.alarms = []

    def add_alarm(self, time_str):
        alarm_time = parse_alarm_time(time_str)

        if alarm_time is None:
            return False, "Invalid time format. Use HH:MM."

        normalized_time = alarm_time.strftime("%H:%M")

        if any(
            alarm.display_time == normalized_time
            for alarm in self.alarms
        ):
            return False, "An alarm already exists for this time."

        self.alarms.append(Alarm(alarm_time))
        self.alarms.sort(key=lambda alarm: alarm.alarm_time)

        return True, "Alarm added successfully."

    def list_alarms(self):
        return self.alarms

    def update_alarm(self, index, new_time_str):
        if not 0 <= index < len(self.alarms):
            return False, "Invalid alarm number."

        new_alarm_time = parse_alarm_time(new_time_str)

        if new_alarm_time is None:
            return False, "Invalid time format. Use HH:MM."

        normalized_time = new_alarm_time.strftime("%H:%M")

        for i, alarm in enumerate(self.alarms):
            if i != index and alarm.display_time == normalized_time:
                return False, "An alarm already exists for this time."

        self.alarms[index] = Alarm(new_alarm_time)
        self.alarms.sort(key=lambda alarm: alarm.alarm_time)

        return True, "Alarm updated successfully."

    def delete_alarm(self, index):
        if 0 <= index < len(self.alarms):
            self.alarms.pop(index)
            return True

        return False
