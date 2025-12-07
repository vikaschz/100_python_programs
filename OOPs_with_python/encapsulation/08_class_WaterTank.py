"""Create a class WaterTank with private attribute __level (0-100).
Add fill and drain methods that enforce limits."""

class WaterTank:
    def __init__(self):
        self.__level = 0  # 0 to 100

    def fill(self, amount):
        if amount < 0:
            print("Cannot fill negative amount.")
            return

        if self.__level + amount > 100:
            self.__level = 100
            print("Tank is now full (100%).")
        else:
            self.__level += amount
            print(f"Tank level: {self.__level}%")

    def drain(self, amount):
        if amount < 0:
            print("Cannot drain negative amount.")
            return

        if self.__level - amount < 0:
            self.__level = 0
            print("Tank is now empty (0%).")
        else:
            self.__level -= amount
            print(f"Tank level: {self.__level}%")


w = WaterTank()
w.fill(-50)
w.fill(50)
w.fill(55)
w.drain(3)