"""
Create a class LibraryBook with a private variable __is_available.
Add methods to issue and return the book, blocking invalid operations.
"""


class LibraryBook:
    def __init__(self, title):
        self.title = title
        self.__is_available = True

    def issue(self):
        if self.__is_available:
            self.__is_available = False
            print(f'"{self.title}" issued.')
        else:
            print(f'"{self.title}" is already issued.')

    def return_book(self):
        if not self.__is_available:
            self.__is_available = True
            print(f'"{self.title}" returned.')
        else:
            print(f'"{self.title}" was not issued.')

book = LibraryBook("The Song Of Ice And Fire")
book.issue()
book.issue()
book.return_book()
book.return_book()