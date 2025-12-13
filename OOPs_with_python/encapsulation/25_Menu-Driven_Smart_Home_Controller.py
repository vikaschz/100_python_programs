"""
10. Menu-Driven Smart Home Controller
Class SmartDevice with private settings: brightness, volume, temperature.
Menu:
1. Change brightness
2. Change volume
3. Change temperature
4. Show settings
5. Exit
Input must always stay within allowed safe ranges.
"""


class SmartDevice:

    def __init__(self):
        self.__brightness = 50  # private
        self.__volume = 50  # private
        self.__temperature = 22  # private

    @property
    def brightness(self):
        return self.__brightness

    @property
    def volume(self):
        return self.__volume

    @property
    def temperature(self):
        return self.__temperature

    def __set_brightness(self, value):
        if 0 <= value <= 100:
            self.__brightness = value
            print("✔ Brightness updated.")
        else:
            print("❌ Invalid brightness! Must be 0–100.")

    def __set_volume(self, value):
        if 0 <= value <= 100:
            self.__volume = value
            print("✔ Volume updated.")
        else:
            print("❌ Invalid volume! Must be 0–100.")

    def __set_temperature(self, value):
        if 16 <= value <= 30:
            self.__temperature = value
            print("✔ Temperature updated.")
        else:
            print("❌ Invalid temperature! Must be 16–30°C.")

    def update_setting(self, setting, value):
        if setting == "brightness":
            self.__set_brightness(value)

        elif setting == "volume":
            self.__set_volume(value)

        elif setting == "temperature":
            self.__set_temperature(value)

        else:
            print("❌ Unknown setting.")

    def show_settings(self):
        print("\n📟 SMART DEVICE SETTINGS")
        print(f"Brightness:  {self.__brightness}%")
        print(f"Volume:      {self.__volume}%")
        print(f"Temperature: {self.__temperature}°C\n")


device = SmartDevice()

while True:
    print("\n----- SMART HOME CONTROLLER -----")
    print("1. Change brightness")
    print("2. Change volume")
    print("3. Change temperature")
    print("4. Show settings")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        value = int(input("Enter brightness (0-100): "))
        device.update_setting("brightness", value)

    elif choice == "2":
        value = int(input("Enter volume (0-100): "))
        device.update_setting("volume", value)

    elif choice == "3":
        value = int(input("Enter temperature (16-30): "))
        device.update_setting("temperature", value)

    elif choice == "4":
        device.show_settings()

    elif choice == "5":
        print("Exiting Smart Home Controller...")
        break

    else:
        print("❌ Invalid choice! Try again.")
