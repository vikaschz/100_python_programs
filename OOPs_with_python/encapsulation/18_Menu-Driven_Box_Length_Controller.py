'''3. Menu-Driven Box Length Controller
Class Box with private __length.
Menu:
1. Set new length
2. Get current length
3. Get volume
4. Exit
Length must be > 0.
'''

class Box:
    def __init__(self, width, height, length):
        self.width = width
        self.height = height
        self.__length = length      # private

    def set_length(self, new_length):
        if new_length > 0:
            self.__length = new_length
            print("Length updated successfully.")
        else:
            print("❌ Length must be greater than 0.")

    def get_length(self):
        print(f"Current Length: {self.__length}")

    def get_volume(self):
        volume = self.width * self.height * self.__length
        print(f"Volume of box: {volume}")


box = Box(3, 4, 5)

while True:
    print("\n--- Box Length Controller ---")
    print("1. Set New Length")
    print("2. Get Current Length")
    print("3. Get Volume")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        new_len = float(input("Enter length (> 0): "))
        box.set_length(new_len)

    elif choice == "2":
        box.get_length()

    elif choice == "3":
        box.get_volume()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Try again.")
