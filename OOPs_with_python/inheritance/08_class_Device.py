"""
Create a base class Device with power_on(). Derive Mobile and Laptop classes.
"""
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        self.is_on = False

    def power_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now powered ON.")

class Mobile(Device):
    def __init__(self, brand, model, screen_type):
        
        super().__init__(brand, model)
        self.screen_type = screen_type

    def power_on(self):
        super().power_on()
        print(f"Showing {self.screen_type} splash screen... Signal searching...")

class Laptop(Device):
    def __init__(self, brand, model, ram_gb):
        super().__init__(brand, model)
        self.ram_gb = ram_gb

    def power_on(self):
        super().power_on()
        print(f"Loading OS... {self.ram_gb}GB RAM initialized.")

my_phone = Mobile("Apple", "iPhone 15", "OLED")
my_laptop = Laptop("Dell", "XPS 15", 32)

print("--- Activating Devices ---")
my_phone.power_on()
my_laptop.power_on()