"""4. Menu-Driven Inventory System
Class InventoryItem with private __stock.
Menu:
1. Add stock
2. Remove stock
3. View stock
4. Exit
Stock may never go below zero."""


class InventoryItem:

    def __init__(self, name, stock):
        self.name = name
        self.__stock = stock  # private

    def add_stock(self, amount):
        if amount > 0:
            self.__stock += amount
            print(f"{amount} units added.")
        else:
            print("Invalid amount!")

    def remove_stock(self, amount):
        if amount > 0:
            if amount <= self.__stock:
                self.__stock -= amount
                print(f"{amount} units removed.")
            else:
                print("Not enough stock to remove!")
        else:
            print("Invalid amount!")

    def view_stock(self):
        print(f"Current stock of {self.name}: {self.__stock}")


item = InventoryItem("Laptop", 50)

while True:
    print("\n--- Inventory Menu ---")
    print("1. Add stock")
    print("2. Remove stock")
    print("3. View stock")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        amt = int(input("Enter amount to add: "))
        item.add_stock(amt)

    elif choice == "2":
        amt = int(input("Enter amount to remove: "))
        item.remove_stock(amt)

    elif choice == "3":
        item.view_stock()

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice! Try again.")
