"""7. Menu-Driven Online Order Tracker
Class Order with private __status (Pending, Processing, Shipped, Delivered, Cancelled).
Menu:
1. Process order
2. Ship order
3. Deliver order
4. Cancel order
5. View status
6. Exit
Block invalid state transitions."""


class Order:
    VALID_STATES = ["Pending", "Processing", "Shipped", "Delivered", "Cancelled"]

    def __init__(self):
        self.__status = "Pending"

    # Getter
    @property
    def status(self):
        return self.__status

    # Setter
    @status.setter
    def status(self, new_status):
        if new_status not in Order.VALID_STATES:
            print("❌ Invalid Status!")
            return

        if self.__status == "Pending":
            if new_status not in ["Processing", "Cancelled"]:
                print("❌ Can't move from Pending →", new_status)
                return

        elif self.__status == "Processing":
            if new_status not in ["Shipped", "Cancelled"]:
                print("❌ Can't move from Processing →", new_status)
                return

        elif self.__status == "Shipped":
            if new_status != "Delivered":
                print("❌ Can't move from Shipped →", new_status)
                return

        elif self.__status in ["Delivered", "Cancelled"]:
            print(f"❌ Order already {self.__status}. No more updates allowed.")
            return

        self.__status = new_status
        print(f"✔ Status updated to: {self.__status}")

    def process(self):
        self.status = "Processing"

    def ship(self):
        self.status = "Shipped"

    def deliver(self):
        self.status = "Delivered"

    def cancel(self):
        self.status = "Cancelled"

    def view_status(self):
        print(f"📦 Current Status: {self.__status}")


def menu():
    order = Order()

    while True:
        print("\n--- Online Order Tracker ---")
        print("1. Process order")
        print("2. Ship order")
        print("3. Deliver order")
        print("4. Cancel order")
        print("5. View status")
        print("6. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            order.process()
        elif choice == "2":
            order.ship()
        elif choice == "3":
            order.deliver()
        elif choice == "4":
            order.cancel()
        elif choice == "5":
            order.view_status()
        elif choice == "6":
            print("Exiting...")
            break
        else:
            print("❌ Invalid choice! Try again.")


menu()
