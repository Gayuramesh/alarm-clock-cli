from alarm_clock.alarm_manager import AlarmManager


class AlarmCLI:

    def __init__(self):
        self.manager = AlarmManager()

    def add_alarm(self):

        alarm = input("\nEnter alarm time (HH:MM): ").strip()

        success, message = self.manager.add_alarm(alarm)

        if success:
            print(f"\n✅ {message}")
            print(f"Alarm scheduled for {alarm}")
        else:
            print(f"\n❌ {message}")

    def view_alarms(self):

        alarms = self.manager.list_alarms()

        if not alarms:
            print("\n⚠ No alarms scheduled.")
            return

        print("\nScheduled Alarms")
        print("-" * 40)

        for index, alarm in enumerate(alarms, start=1):

            status = "✅ Triggered" if alarm.triggered else "⏳ Pending"

            print(
                f"{index}. {alarm.display_time:<10} {status}"
            )

        print("-" * 40)

    def delete_alarm(self):

        alarms = self.manager.list_alarms()

        if not alarms:
            print("\nNo alarms available.")
            return

        self.view_alarms()

        try:

            choice = int(
                input("\nEnter alarm number to delete: ")
            ) - 1

            if self.manager.delete_alarm(choice):
                print("\n✅ Alarm deleted successfully.")
            else:
                print("\n❌ Invalid alarm number.")

        except ValueError:
            print("\n❌ Please enter a valid number.")
