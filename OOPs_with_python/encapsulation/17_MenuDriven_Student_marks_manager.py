"""2. Menu-Driven Student Marks Manager
Make a class Student with private __marks.
Menu:
1. Add marks
2. Update marks
3. View marks
4. Exit
Marks must always stay between 0 and 100."""


class Student:
    def __init__(self):
        self.__marks = None  # private

    def add_marks(self, m):
        if 0 <= m <= 100:
            self.__marks = m
            print("Marks added successfully.")
        else:
            print("❌ Marks must be between 0 and 100.")

    def update_marks(self, m):
        if self.__marks is None:
            print("❌ No marks found. Add marks first.")
        elif 0 <= m <= 100:
            self.__marks = m
            print("Marks updated successfully.")
        else:
            print("❌ Invalid marks range.")

    def view_marks(self):
        if self.__marks is None:
            print("No marks available yet.")
        else:
            print(f"Current Marks: {self.__marks}")


student = Student()

while True:
    print("\n--- Student Marks Manager ---")
    print("1. Add Marks")
    print("2. Update Marks")
    print("3. View Marks")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        m = int(input("Enter marks (0-100): "))
        student.add_marks(m)

    elif choice == "2":
        m = int(input("Enter new marks (0-100): "))
        student.update_marks(m)

    elif choice == "3":
        student.view_marks()

    elif choice == "4":
        print("Exiting program...")
        break

    else:
        print("Invalid choice! Please try again.")
