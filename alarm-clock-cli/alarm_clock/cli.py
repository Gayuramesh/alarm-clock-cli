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

            if not 0 <= choice < len(alarms):
                print("\n❌ Invalid alarm number.")
                return

            confirmation = input(
                "Are you sure you want to delete this alarm? (y/n): "
            ).strip().lower()

            if confirmation == "y":
                if self.manager.delete_alarm(choice):
                    print("\n✅ Alarm deleted successfully.")
                else:
                    print("\n❌ Unable to delete alarm.")
            elif confirmation == "n":
                print("\nAlarm deletion cancelled.")
            else:
                print("\n❌ Invalid confirmation. Enter y or n.")

        except ValueError:
            print("\n❌ Please enter a valid alarm number.")

    def update_alarm(self):
        alarms = self.manager.list_alarms()

        if not alarms:
            print("\nNo alarms available to update.")
            return

        self.view_alarms()

        try:
            choice = int(
                input("\nEnter alarm number to update: ")
            ) - 1

            if not 0 <= choice < len(alarms):
                print("\nInvalid alarm number.")
                return

            new_time = input(
                "Enter new alarm time (HH:MM): "
            ).strip()

            success, message = self.manager.update_alarm(
                choice,
                new_time,
            )

            if success:
                print(f"\n{message}")
            else:
                print(f"\nError: {message}")

        except ValueError:
            print("\nPlease enter a valid alarm number.")
