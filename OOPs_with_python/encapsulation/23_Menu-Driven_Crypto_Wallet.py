"""8. Menu-Driven Crypto Wallet
Class CryptoWallet with private __balance.
Menu:
1. Deposit
2. Withdraw
3. Transfer (simulate signature verification)
4. View balance
5. Exit
Reject transactions without a valid "signature" (fake simulation)."""


class CryptoWallet:

    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # private variable

    @property
    def balance(self):
        return self.__balance

    def __set_balance(self, new_balance):
        self.__balance = new_balance

    def verify_signature(self, signature):
        return signature == "VALID"

    def deposit(self, amount, signature):
        if not self.verify_signature(signature):
            print("❌ Invalid digital signature! Transaction rejected.")
            return

        if amount > 0:
            self.__set_balance(self.__balance + amount)
            print(f"✅ Deposited ₹{amount}")
        else:
            print("❌ Deposit amount must be positive.")

    def withdraw(self, amount, signature):
        if not self.verify_signature(signature):
            print("❌ Invalid digital signature! Transaction rejected.")
            return

        if amount <= 0:
            print("❌ Invalid withdrawal amount.")
        elif amount > self.__balance:
            print("❌ Insufficient balance.")
        else:
            self.__set_balance(self.__balance - amount)
            print(f"✅ Withdrawn ₹{amount}")

    def transfer(self, other_wallet, amount, signature):
        if not self.verify_signature(signature):
            print("❌ Invalid digital signature! Transfer rejected.")
            return

        if amount <= 0:
            print("❌ Transfer amount must be positive.")
        elif amount > self.__balance:
            print("❌ Insufficient funds.")
        else:
            self.__set_balance(self.__balance - amount)
            other_wallet._CryptoWallet__set_balance(other_wallet.balance + amount)
            print(f"✅ Transferred ₹{amount} to {other_wallet.owner}")

    def show_balance(self):
        print(f"Current Balance for {self.owner}: ₹{self.__balance}")


w1 = CryptoWallet("Vikas", 1000)
w2 = CryptoWallet("Alice", 500)

while True:
    print("\n--- Crypto Wallet Menu ---")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Transfer")
    print("4. View Balance")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        amt = float(input("Enter amount to deposit: "))
        sig = input("Enter signature (type VALID to accept): ")
        w1.deposit(amt, sig)

    elif choice == "2":
        amt = float(input("Enter amount to withdraw: "))
        sig = input("Enter signature (type VALID to accept): ")
        w1.withdraw(amt, sig)

    elif choice == "3":
        amt = float(input("Enter amount to transfer: "))
        sig = input("Enter signature (type VALID to accept): ")
        w1.transfer(w2, amt, sig)

    elif choice == "4":
        w1.show_balance()

    elif choice == "5":
        print("👍 Exiting ...")
        break

    else:
        print("❌ Invalid option. Try again.")
