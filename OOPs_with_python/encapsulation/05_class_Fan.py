"""Write a class Fan with private speed (1-5).
Add methods to increase/decrease speed within the range."""

class Fan:
    def __init__(self, speed=1):
        self.__speed = speed

    def increase_speed(self):
        if self.__speed < 5:
            self.__speed += 1
            print(f"Fan speed increased to {self.__speed}")
        else:
            print("Speed is already at maximum (5).")

    def decrease_speed(self):
        if self.__speed > 1:
            self.__speed -= 1
            print(f"Fan speed decreased to {self.__speed}")
        else:
            print("Speed is already at minimum (1).")

    def get_speed(self):
        return self.__speed


f = Fan()
f.increase_speed()
f.increase_speed()
f.decrease_speed()
print("Current speed:", f.get_speed())
