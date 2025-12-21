"""1. Menu-Driven Payment System
Create a class Payment with subclasses UPI, Card, Wallet.
Menu options:
1. Choose payment method
2. Pay amount
3. View last transaction
4. Exit
"""

from abc import ABC, abstractmethod


class Payment(ABC):

    @abstractmethod
    def pay_amount(self, amount):
        pass


class UPI(Payment):
    def pay_amount(self, amount):
        return f"Paid ₹{amount} using UPI."


class Card(Payment):
    def pay_amount(self, amount):
        return f"Paid ₹{amount} using Card."


class Wallet(Payment):
    def pay_amount(self, amount):
        return f"Paid ₹{amount} using Wallet."


payment_method = None
last_transaction = "No transaction yet."

while True:
    print("\n---- PAYMENT MENU ----")
    print("1. Choose payment method")
    print("2. Pay amount")
    print("3. View last transaction")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        print("\nChoose Payment Method:")
        print("1. UPI")
        print("2. Card")
        print("3. Wallet")

        method = input("Enter option: ")

        if method == "1":
            payment_method = UPI()
            print("UPI selected.")
        elif method == "2":
            payment_method = Card()
            print("Card selected.")
        elif method == "3":
            payment_method = Wallet()
            print("Wallet selected.")
        else:
            print("Invalid payment option.")

    elif choice == "2":
        if payment_method is None:
            print("Please choose a payment method first.")
        else:
            amount = float(input("Enter amount to pay: "))
            last_transaction = payment_method.pay_amount(amount)
            print(last_transaction)

    elif choice == "3":
        print("Last Transaction:", last_transaction)

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice")
