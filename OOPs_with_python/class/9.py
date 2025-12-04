"""
9. Create a class Laptop with brand, RAM, and price. 
Add a method to print full specifications.
"""

class Laptop:

    def __init__(self, brand, RAM, price):
        self.brand = brand
        self.ram = RAM
        self.price = price

    def laptop_specs(self):

        print(f"Laptop Brand: {self.brand}")
        print(f"Laptop RAM: {self.ram}")
        print(f"Laptop Price: ₹{self.price}")

#object 1  
l1 = Laptop("Lenevo", "12GB RAM", 63000)
l1.laptop_specs()

#object 2  
l2 = Laptop("Asus tuff", "16GB RAM", 75000)
l2.laptop_specs()