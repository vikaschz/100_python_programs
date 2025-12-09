"""Build a class Robot with private battery and temperature variables.
Add methods to perform tasks that drain the battery and increase temperature.
Shut down operations automatically when safety limits are crossed."""


class Robot:
    def __init__(self):
        self.__battery = 100
        self.__temperature = 25
        self.__active = True

    def __check_safety(self):
        if self.__battery < 10 or self.__temperature > 80:
            print("Safety limits exceeded. Robot shutting down.")
            self.__active = False

    def perform_task(self):
        if not self.__active:
            print("Robot is inactive.")
            return

        print("Performing task...")
        self.__battery -= 15
        self.__temperature += 10
        self.__check_safety()

    def cool_down(self):
        if self.__active:
            self.__temperature = max(25, self.__temperature - 20)
            print("Cooling down...")

    def recharge(self):
        if self.__active:
            self.__battery = min(100, self.__battery + 30)
            print("Recharging...")

    def status(self):
        return f"Battery: {self.__battery}, Temp: {self.__temperature}, Active: {self.__active}"


r = Robot()
r.perform_task()
r.perform_task()
print(r.status())