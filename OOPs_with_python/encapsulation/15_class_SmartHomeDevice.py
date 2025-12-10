"""
Design a class SmartHomeDevice with private settings like brightness, volume, and temperature.
Create a central method to update settings only if input falls within safe ranges.
External code cannot modify settings directly."""


class SmartHomeDevice:
    def __init__(self):
        self.__brightness = 50
        self.__volume = 50
        self.__temperature = 22

    def __is_valid(self, setting, value):
        ranges = {
            "brightness": (0, 100),
            "volume": (0, 100),
            "temperature": (16, 30),
        }
        low, high = ranges[setting]
        return low <= value <= high

    def update_setting(self, setting, value):
        if self.__is_valid(setting, value):
            if setting == "brightness":
                self.__brightness = value
            elif setting == "volume":
                self.__volume = value
            elif setting == "temperature":
                self.__temperature = value
            print("Setting updated.")
        else:
            print("Invalid value for setting.")

    def get_settings(self):
        return {
            "brightness": self.__brightness,
            "volume": self.__volume,
            "temperature": self.__temperature,
        }


# Example
device = SmartHomeDevice()
device.update_setting("brightness", 80)
device.update_setting("temperature", 50)
print(device.get_settings())
