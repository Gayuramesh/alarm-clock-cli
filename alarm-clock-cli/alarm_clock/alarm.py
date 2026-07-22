from dataclasses import dataclass


@dataclass
class Alarm:
    """
        Represents a single alarm.
    """

    time: str
    triggered: bool = False