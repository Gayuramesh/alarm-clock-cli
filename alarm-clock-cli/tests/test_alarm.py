import unittest

from alarm_clock.utils import parse_alarm_time


class TestAlarm(unittest.TestCase):

    def test_valid_time(self):
        self.assertIsNotNone(parse_alarm_time("07:30"))

    def test_invalid_time(self):
        self.assertIsNone(parse_alarm_time("25:61"))


if __name__ == "__main__":
    unittest.main()
