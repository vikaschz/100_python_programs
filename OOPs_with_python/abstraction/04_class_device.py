"""
Create an abstract class Device with turn_on() and turn_off(). Implement TV and Laptop.
"""

from abc import ABC, abstractmethod


class Device(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


class TV(Device):
    def turn_on(self):
        print("TV is turned ON.")

    def turn_off(self):
        print("TV is turned OFF.")


class Laptop(Device):
    def turn_on(self):
        print("Laptop is powering ON.")

    def turn_off(self):
        print("Laptop is shutting DOWN.")


tv = TV()
laptop = Laptop()

tv.turn_on()
tv.turn_off()

laptop.turn_on()
laptop.turn_off()
