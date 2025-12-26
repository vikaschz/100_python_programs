"""
Create a base class Vehicle. Derive FourWheeler from Vehicle and Car from FourWheeler.
Demonstrate multilevel inheritance.
"""


class Vehicle:
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type

    def display_vehicle(self):
        print(f"This is a vehicle powered by {self.fuel_type}.")


class FourWheeler(Vehicle):
    def __init__(self, fuel_type, wheel_count=4):

        super().__init__(fuel_type)
        self.wheel_count = wheel_count

    def display_wheels(self):
        print(f"This is a {self.wheel_count}-wheeler.")


class Car(FourWheeler):
    def __init__(self, fuel_type, brand, model):

        super().__init__(fuel_type)
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"Car Details: {self.brand} {self.model}")
        self.display_vehicle()
        self.display_wheels()


my_car = Car("Electric", "Tesla", "Model 3")
my_car.display_info()
