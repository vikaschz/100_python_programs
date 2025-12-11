"""5. Menu-Driven Library Book System
Class LibraryBook with private __is_available.
Menu:
1. Issue book
2. Return book
3. Check status
4. Exit
Issue only if available, return only if issued."""


class LibraryBook:

    def __init__(self, title):
        self.title = title
        self.__is_available = True  # private variable

    def issue_book(self):
        if self.__is_available:
            self.__is_available = False
            print(f"'{self.title}' has been issued.")
        else:
            print(f"'{self.title}' is already issued!")

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f"'{self.title}' has been returned.")
        else:
            print(f"'{self.title}' was not issued!")

    def check_status(self):
        if self.__is_available:
            print(f"'{self.title}' is AVAILABLE.")
        else:
            print(f"'{self.title}' is ISSUED to someone.")


book = LibraryBook("Python Programming Guide")

while True:
    print("\n----- Library Book Menu -----")
    print("1. Issue Book")
    print("2. Return Book")
    print("3. Check Status")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        book.issue_book()

    elif choice == "2":
        book.return_book()

    elif choice == "3":
        book.check_status()

    elif choice == "4":
        print("Exiting Library System.")
        break

    else:
        print("Invalid input! Please try again.")
