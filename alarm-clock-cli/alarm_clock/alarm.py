from dataclasses import dataclass
from datetime import datetime


@dataclass
class Alarm:

    alarm_time: datetime

    triggered: bool = False

    @property
    def display_time(self):

        return self.alarm_time.strftime("%H:%M")

    def __str__(self):

        return self.display_time
