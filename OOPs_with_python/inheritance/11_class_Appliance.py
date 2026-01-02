"""
Create a base class Appliance with turn_on(). Derive Fan, Light, and AC classes.
"""


class Appliance:
    def __init__(self, brand):
        self.brand = brand
        self.is_powered = False

    def turn_on(self):
        self.is_powered = True
        print(f"The {self.brand} appliance is now receiving power.")


class Fan(Appliance):
    def __init__(self, brand, speed_levels=3):
        super().__init__(brand)
        self.speed_levels = speed_levels

    def turn_on(self):
        super().turn_on()
        print(f"Fan blades starting to rotate. Speed set to 1 of {self.speed_levels}.")


class Light(Appliance):
    def __init__(self, brand, color_temp="Warm"):
        super().__init__(brand)
        self.color_temp = color_temp

    def turn_on(self):
        super().turn_on()
        print(f"Light glowing at {self.color_temp} temperature. 💡")


class AC(Appliance):
    def __init__(self, brand, target_temp=24):
        super().__init__(brand)
        self.target_temp = target_temp

    def turn_on(self):
        super().turn_on()
        print(f"Compressor starting... Cooling to {self.target_temp}°C. ❄️")


ceiling_fan = Fan("Usha", 5)
desk_lamp = Light("Philips", "Cool White")
bedroom_ac = AC("Daikin", 22)

devices = [ceiling_fan, desk_lamp, bedroom_ac]

print("--- Smart Home Dashboard ---")
for device in devices:
    device.turn_on()
