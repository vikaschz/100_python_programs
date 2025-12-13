"""
9. Menu-Driven Robot Control Panel
Class Robot with private battery & temperature.
Menu:
1. Perform task
2. Cool down
3. Recharge
4. View stats
5. Shutdown robot
Robot stops tasks if battery < 10 or temperature > limit.
"""


class Robot:
    def __init__(self):
        self.__battery = 100  # private
        self.__temperature = 25  # private
        self.__active = True

    @property
    def battery(self):
        return self.__battery

    @property
    def temperature(self):
        return self.__temperature

    @property
    def is_active(self):
        return self.__active

    def __set_battery(self, value):
        self.__battery = max(0, min(100, value))

    def __set_temperature(self, value):
        self.__temperature = max(20, value)

    def __shutdown(self):
        print("❌ SAFETY ALERT! Robot shutting down...")
        self.__active = False

    def perform_task(self):
        if not self.__active:
            print("Robot is inactive. Restart required.")
            return

        if self.__battery < 10:
            print("⚠️ Battery too low for performing tasks!")
            self.__shutdown()
            return

        if self.__temperature > 80:
            print("⚠️ Temperature too high! Task not allowed.")
            self.__shutdown()
            return

        print("🤖 Performing task...")
        self.__set_battery(self.__battery - 15)
        self.__set_temperature(self.__temperature + 12)

        if self.__battery < 10 or self.__temperature > 80:
            self.__shutdown()

    def cool_down(self):
        if not self.__active:
            print("Robot is inactive.")
            return

        self.__set_temperature(self.__temperature - 20)
        print("❄️ Cooling down... Temperature reduced.")

    def recharge(self):
        if not self.__active:
            print("Robot is inactive.")
            return

        self.__set_battery(self.__battery + 30)
        print("🔋 Recharging... Battery increased.")

    def view_stats(self):
        print(f"\n📊 ROBOT STATS")
        print(f"Battery: {self.__battery}%")
        print(f"Temperature: {self.__temperature}°C")
        print(f"Status: {'Active' if self.__active else 'Inactive'}\n")

    def shutdown_robot(self):
        self.__shutdown()


robot = Robot()

while True:
    print("\n---- ROBOT CONTROL PANEL ----")
    print("1. Perform task")
    print("2. Cool down")
    print("3. Recharge")
    print("4. View stats")
    print("5. Shutdown robot")

    choice = input("Enter your choice: ")

    if choice == "1":
        robot.perform_task()

    elif choice == "2":
        robot.cool_down()

    elif choice == "3":
        robot.recharge()

    elif choice == "4":
        robot.view_stats()

    elif choice == "5":
        robot.shutdown_robot()
        break

    else:
        print("Invalid choice! Try again.")
