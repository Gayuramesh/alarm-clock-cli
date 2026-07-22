from datetime import datetime


def validate_time(time_str: str) -> bool:
    """
    Validate whether the input is in HH:MM format.
    """
    try:
        datetime.strptime(time_str, "%H:%M")
        return True
    except ValueError:
        return False
