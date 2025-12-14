"""
Create an abstract class Vehicle with an abstract method start(). Implement Car and Bike.
"""

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car starts with a key ignition.")


class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")


car = Car()
bike = Bike()

car.start()
bike.start()
