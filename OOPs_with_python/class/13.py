"""
13. Create a class ShoppingCart that:
Adds items (name + price)
Removes items
Calculates total bill
"""


class ShoppingCart:
    def __init__(self):
        self.items = {}   # item: price

    def add_items(self):
        count = int(input("Enter how many items to add: "))
        for i in range(count):
            item = input(f"Enter item {i+1}: ")
            price = float(input(f"Enter price for {item}: "))
            self.items[item] = price

    def remove_items(self):
        item = input("Enter item to remove: ")
        if item in self.items:
            del self.items[item]
            print(f"{item} removed from cart")
        else:
            print(f"{item} not found in cart")

    def print_items(self):
        if not self.items:
            print("Cart is empty")
            return
        print("Items in cart:")
        for name, price in self.items.items():
            print(f"- {name}: ₹{price}")

    def calculate_total_bill(self):
        total = sum(self.items.values())
        print(f"Total bill: ₹{total}")
        return total


s1 = ShoppingCart()
s1.add_items()
s1.print_items()
s1.remove_items()
s1.print_items()
s1.calculate_total_bill()
