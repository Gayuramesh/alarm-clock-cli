import threading
import time
from datetime import datetime


class Scheduler:

    def __init__(self, alarms):
        self.alarms = alarms
        self.running = False

    def check_alarms(self):

        while self.running:

            now = datetime.now()

            for alarm in self.alarms:

                if alarm.triggered:
                    continue

                if now >= alarm.alarm_time:

                    print("\n")
                    print("*" * 55)
                    print("🔔🔔🔔 ALARM TRIGGERED 🔔🔔🔔")
                    print(f"Scheduled Time : {alarm.display_time}")
                    print("Time to Wake Up!")
                    print("*" * 55)
                    print()

                    alarm.triggered = True

            time.sleep(1)

    def start(self):

        self.running = True

        threading.Thread(
            target=self.check_alarms,
            daemon=True
        ).start()

    def stop(self):

        self.running = False
