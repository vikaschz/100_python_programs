"""Design a class Wallet with a private variable __money.
Add deposit and withdraw methods with basic validation."""


class Wallet:

    def __init__(self, money):
        self.__money = money

    def deposit(self, amount):
        if amount > 0:
            self.__money += amount
            print(f"₹{amount} deposited to wallet")
            print(f"Current money in wallet: ₹{self.__money}")
        else:
            print("Negative amount cannot be deposited.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Withdrawal amount should be positive.")
        elif amount <= self.__money:
            self.__money -= amount
            print(f"₹{amount} withdrawn from wallet")
            print(f"Current money in wallet: ₹{self.__money}")
        else:
            print("You can't withdraw more than what's in the wallet.")


w1 = Wallet(5000)
w1.deposit(-500)
w1.deposit(500)
w1.withdraw(6000)
w1.withdraw(1000)
