import unittest

from alarm_clock.utils import parse_alarm_time
from alarm_clock.alarm_manager import AlarmManager


class TestAlarm(unittest.TestCase):

    def test_valid_time(self):
        self.assertIsNotNone(parse_alarm_time("07:30"))

    def test_invalid_time(self):
        self.assertIsNone(parse_alarm_time("25:61"))


class TestAlarmManager(unittest.TestCase):

    def setUp(self):
        self.manager = AlarmManager()

    def test_add_alarm(self):
        success, message = self.manager.add_alarm("07:30")
        self.assertTrue(success)
        self.assertEqual(message, "Alarm added successfully.")
        self.assertEqual(len(self.manager.list_alarms()), 1)

    def test_update_alarm(self):
        self.manager.add_alarm("07:30")
        success, message = self.manager.update_alarm(0, "08:30")

        self.assertTrue(success)
        self.assertEqual(message, "Alarm updated successfully.")
        self.assertEqual(
            self.manager.list_alarms()[0].display_time,
            "08:30",
        )

    def test_update_alarm_invalid_time(self):
        self.manager.add_alarm("07:30")
        success, message = self.manager.update_alarm(0, "25:61")

        self.assertFalse(success)
        self.assertEqual(message, "Invalid time format. Use HH:MM.")
        self.assertEqual(
            self.manager.list_alarms()[0].display_time,
            "07:30",
        )

    def test_update_alarm_invalid_index(self):
        success, message = self.manager.update_alarm(0, "08:30")

        self.assertFalse(success)
        self.assertEqual(message, "Invalid alarm number.")

    def test_update_alarm_duplicate_time(self):
        self.manager.add_alarm("07:30")
        self.manager.add_alarm("09:30")
        success, message = self.manager.update_alarm(0, "09:30")

        self.assertFalse(success)
        self.assertEqual(
            message,
            "An alarm already exists for this time.",
        )
        self.assertEqual(
            self.manager.list_alarms()[0].display_time,
            "07:30",
        )

    def test_add_alarm_duplicate_unpadded_time(self):
        success, _ = self.manager.add_alarm("07:30")
        self.assertTrue(success)
    
        success, message = self.manager.add_alarm("7:30")
    
        self.assertFalse(success)
        self.assertEqual(
            message,
            "An alarm already exists for this time.",
        )
        self.assertEqual(len(self.manager.list_alarms()), 1)


if __name__ == "__main__":
    unittest.main()
