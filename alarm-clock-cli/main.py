from alarm_clock.cli import AlarmCLI
from alarm_clock.scheduler import Scheduler

def print_menu():
    print("\n" + "=" * 50)
    print("         ⏰ PYTHON CLI ALARM CLOCK ⏰")
    print("=" * 50)
    print("1. ➕ Add Alarm")
    print("2. 📋 View Alarms")
    print("3. 🗑 Delete Alarm")
    print("4. 🚪 Exit")
    print("=" * 50)

def main():

    cli = AlarmCLI()

    scheduler = Scheduler(cli.manager.alarms)

    scheduler.start()

    while True:

        print_menu()

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            cli.add_alarm()

        elif choice == "2":
            cli.view_alarms()

        elif choice == "3":
            cli.delete_alarm()

        elif choice == "4":
            scheduler.stop()
            print("\nThank you for using Python CLI Alarm Clock.")
            print("Have a productive day!\n")
            break

        else:
            print("\n❌ Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
