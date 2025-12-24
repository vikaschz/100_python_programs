"""
8. Menu-Driven Appliance Controller
Create a class Appliance with operate(). Subclasses: Fan, Light, AC.
Menu options:
1. Choose appliance
2. Operate appliance
3. Exit
"""

from abc import ABC, abstractmethod


# Abstract Base Class
class Appliance(ABC):
    @abstractmethod
    def operate(self):
        """Abstract method to define appliance behavior."""
        pass


class Fan(Appliance):
    def operate(self):
        print("Fan: Blades are spinning. Airflow set to medium.")


class Light(Appliance):
    def operate(self):
        print("Light: LED panel illuminated. Brightness at 100%.")


class AC(Appliance):
    def operate(self):
        print("AC: Compressor started. Cooling room to 22°C.")


selected_appliance = None

while True:
    print("\n--- Smart Home Controller ---")
    print("1. Choose Appliance")
    print("2. Operate Appliance")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nDevices: 1. Fan | 2. Light | 3. AC")
        dev_choice = input("Enter device number: ")

        if dev_choice == "1":
            selected_appliance = Fan()
            print("Fan selected.")
        elif dev_choice == "2":
            selected_appliance = Light()
            print("Light selected.")
        elif dev_choice == "3":
            selected_appliance = AC()
            print("AC selected.")
        else:
            print("Invalid selection.")

    elif choice == "2":
        if selected_appliance:
            selected_appliance.operate()
        else:
            print("Error: No appliance selected. Please choose one first.")

    elif choice == "3":
        print("Turning off controller. Goodbye!")
        break
    else:
        print("Invalid input, please try again.")
