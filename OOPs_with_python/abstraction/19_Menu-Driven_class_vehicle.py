"""
4. Menu-Driven Vehicle Start System
Create a class Vehicle with start(). Subclasses: Car, Bike, Bus.
Menu options:
1. Choose vehicle
2. Start vehicle
3. Exit
"""

from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass



class Car(Vehicle):
    def start(self):
        print("Car: Ignition turned. Engine purring smoothly.")


class Bike(Vehicle):
    def start(self):
        print("Bike: Ignition on. Engine revving high.")


class Bus(Vehicle):
    def start(self):
        print("Bus: Air brakes released. Diesel engine roaring.")


current_vehicle = None

while True:
    print("\n--- Abstract Vehicle System ---")
    print("1. Choose Vehicle")
    print("2. Start Vehicle")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nAvailable: 1. Car | 2. Bike | 3. Bus")
        v_choice = input("Enter number: ")
        if v_choice == "1":
            current_vehicle = Car()

        elif v_choice == "2":
            current_vehicle = Bike()

        elif v_choice == "3":
            current_vehicle = Bus()

        else:
            print("Invalid choice.")

    elif choice == "2":
        if current_vehicle:
            current_vehicle.start()
        else:
            print("Error: No vehicle selected!")

    elif choice == "3":
        print("Shutting down system...")
        break
    else:
        print("Invalid input.")
