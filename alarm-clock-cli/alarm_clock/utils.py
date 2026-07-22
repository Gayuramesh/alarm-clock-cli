from datetime import datetime, timedelta


def parse_alarm_time(time_str: str):
    """
    Parse HH:MM and return the next occurrence of that time.
    """
    try:
        parsed = datetime.strptime(time_str, "%H:%M")

        now = datetime.now()

        alarm_time = now.replace(
            hour=parsed.hour,
            minute=parsed.minute,
            second=0,
            microsecond=0,
        )

        if alarm_time <= now:
            alarm_time += timedelta(days=1)

        return alarm_time

    except ValueError:
        return None
