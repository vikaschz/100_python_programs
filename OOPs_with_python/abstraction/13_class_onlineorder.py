"""
Create an abstract class OnlineOrder with process, ship, deliver, cancel.
Enforce valid transitions.
"""

from abc import ABC, abstractmethod


class OnlineOrder(ABC):

    def __init__(self):
        self.status = "Pending"

    @abstractmethod
    def process(self):
        pass

    @abstractmethod
    def ship(self):
        pass

    @abstractmethod
    def deliver(self):
        pass

    @abstractmethod
    def cancel(self):
        pass


class Order(OnlineOrder):

    def process(self):
        if self.status == "Pending":
            self.status = "Processing"
            print("Order is now Processing.")
        else:
            print("Cannot process from current state.")

    def ship(self):
        if self.status == "Processing":
            self.status = "Shipped"
            print("Order has been Shipped.")
        else:
            print("Cannot ship from current state.")

    def deliver(self):
        if self.status == "Shipped":
            self.status = "Delivered"
            print("Order has been Delivered.")
        else:
            print("Cannot deliver from current state.")

    def cancel(self):
        if self.status in ["Pending", "Processing"]:
            self.status = "Cancelled"
            print("Order has been Cancelled.")
        else:
            print("Cannot cancel from current state.")


order = Order()

order.process()
order.ship()
order.deliver()
order.cancel()
