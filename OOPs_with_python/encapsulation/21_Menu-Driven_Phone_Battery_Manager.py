"""6. Menu-Driven Phone Battery Manager
Class Phone with private __battery_level (0-100).
Menu:
1. Charge phone
2. Use phone
3. Check battery
4. Exit
Prevent overcharging and going below 0."""


class Phone:
    def __init__(self, battery_level=50):
        self.__battery_level = battery_level  # private

    def charge(self, amount):
        if amount <= 0:
            print("Charge amount must be positive!")
            return

        if self.__battery_level + amount > 100:
            self.__battery_level = 100
            print("Phone fully charged! (100%)")
        else:
            self.__battery_level += amount
            print(f"Charged by {amount}%. Current battery: {self.__battery_level}%")

    def use(self, amount):
        if amount <= 0:
            print("Usage amount must be positive!")
            return

        if self.__battery_level - amount < 0:
            print("Not enough battery to use that much! Phone shutting down...")
            self.__battery_level = 0
        else:
            self.__battery_level -= amount
            print(f"Used {amount}%. Current battery: {self.__battery_level}%")

    def check_battery(self):
        print(f"Battery Level: {self.__battery_level}%")


phone = Phone()

while True:
    print("\n=== PHONE BATTERY MANAGER ===")
    print("1. Charge phone")
    print("2. Use phone")
    print("3. Check battery")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = int(input("Enter amount to charge: "))
        phone.charge(amt)

    elif choice == "2":
        amt = int(input("Enter battery usage: "))
        phone.use(amt)

    elif choice == "3":
        phone.check_battery()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
