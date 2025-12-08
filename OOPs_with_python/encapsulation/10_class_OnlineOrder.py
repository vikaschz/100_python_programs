"""Make a class OnlineOrder with private __status.
Only allow status changes through approved methods: process, ship, deliver, cancel"""


class OnlineOrder:
    def __init__(self):
        self.__status = "Pending"

    def process(self):
        if self.__status == "Pending":
            self.__status = "Processing"
            print("Order is now Processing.")
        else:
            print("Cannot process order from current state.")

    def ship(self):
        if self.__status == "Processing":
            self.__status = "Shipped"
            print("Order has been Shipped.")
        else:
            print("Cannot ship order from current state.")

    def deliver(self):
        if self.__status == "Shipped":
            self.__status = "Delivered"
            print("Order Delivered.")
        else:
            print("Cannot deliver order from current state.")

    def cancel(self):
        if self.__status in ("Pending", "Processing"):
            self.__status = "Cancelled"
            print("Order Cancelled.")
        else:
            print("Cannot cancel the order from current state.")

    def get_status(self):
        return self.__status

order = OnlineOrder()
order.process()
order.ship()
order.deliver()
print(order.get_status())
