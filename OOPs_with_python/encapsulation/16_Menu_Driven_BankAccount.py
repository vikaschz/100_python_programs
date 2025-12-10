"""
1. Menu-Driven BankAccount
Create a class BankAccount with a private __balance.
Menu options:
1. create Account
2. Deposit money
3. Withdraw money
4. Check balance
5. Exit

All balance changes must use encapsulated methods.
"""


class BankAccount:
    def __init__(self, account_no, balance=0):
        self.account_no = account_no
        self.__balance = balance  # private

    def check_balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"✅ Deposited: ₹{amount}")
            print(f"💰 Current Balance: ₹{self.__balance}")
        else:
            print("❌ Negative amount cannot be deposited.")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"✅ Withdrawn: ₹{amount}")
            print(f"💰 Current Balance: ₹{self.__balance}")
        else:
            print("❌ Invalid amount or insufficient balance.")


# ✅ Store multiple accounts in a dictionary
accounts = {}

while True:
    print("\n------ BANKING MENU ------")
    print("1. Create Account")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Check Balance")
    print("5. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("❌ Invalid input, enter a number.")
        continue

    if choice == 1:
        acc_no = input("Enter new account number: ")
        if acc_no in accounts:
            print("⚠️ Account already exists!")
        else:
            accounts[acc_no] = BankAccount(acc_no)
            print(f"✅ Account {acc_no} created successfully!")

    elif choice == 2:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter amount to deposit: ₹"))
            accounts[acc_no].deposit(amount)
        else:
            print("❌ Account not found!")

    elif choice == 3:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            amount = int(input("Enter amount to withdraw: ₹"))
            accounts[acc_no].withdraw(amount)
        else:
            print("❌ Account not found!")

    elif choice == 4:
        acc_no = input("Enter account number: ")
        if acc_no in accounts:
            print(f"💰 Balance: ₹{accounts[acc_no].check_balance()}")
        else:
            print("❌ Account not found!")

    elif choice == 5:
        print("👋 Thank you for using our Bank System. Exiting...")
        break

    else:
        print("❌ Invalid choice, try again.")
