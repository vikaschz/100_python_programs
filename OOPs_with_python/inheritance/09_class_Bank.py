"""
Create a base class Bank with deposit() and withdraw().
Derive SBI and HDFC classes.
"""


class Bank:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Successfully deposited ${amount}. New balance: ₹{self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(
                f"Successfully withdrew ${amount}. Remaining balance: ₹{self.balance}"
            )
        else:
            print("Insufficient funds or invalid amount.")


class SBI(Bank):
    def withdraw(self, amount):

        limit = 40000
        if amount > limit:
            print(f"SBI Alert: Transaction exceeds the daily limit of ₹{limit}.")
        else:
            print("Processing SBI transaction...")
            super().withdraw(amount)


class HDFC(Bank):
    def deposit(self, amount):
        if amount > 100000:
            bonus = 100
            print(f"HDFC Special: You earned a ₹{bonus} loyalty bonus!")
            amount += bonus
        super().deposit(amount)


sbi_acc = SBI("John Doe", 50000)
hdfc_acc = HDFC("Jane Smith", 10000)

print(f"--- {sbi_acc.account_holder}'s SBI Session ---")
sbi_acc.withdraw(45000)

print(f"\n--- {hdfc_acc.account_holder}'s HDFC Session ---")
hdfc_acc.deposit(150000)
