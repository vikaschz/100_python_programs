"""
5. Menu-Driven File Reader
Create a class FileReader with read(). Subclasses: TextReader, PDFReader.
Menu options:
1. Choose file type
2. Read file
3. Exit
"""

from abc import ABC, abstractmethod


class FileReader(ABC):
    @abstractmethod
    def read(self):
        pass


class TextReader(FileReader):
    def read(self):
        print("Reading Text File: Accessing raw string data... Done.")


class PDFReader(FileReader):
    def read(self):
        print("Reading PDF File: Extracting metadata and formatting text... Done.")


reader = None

while True:
    print("\n--- File Reader System ---")
    print("1. Choose File Type")
    print("2. Read File")
    print("3. Exit")

    choice = input("Select an option: ")

    if choice == "1":
        print("\nTypes: 1. Text (.txt) | 2. PDF (.pdf)")
        file_type = input("Choice: ")
        if file_type == "1":
            reader = TextReader()
            print("TextReader selected.")
        elif file_type == "2":
            reader = PDFReader()
            print("PDFReader selected.")
        else:
            print("Invalid selection.")

    elif choice == "2":
        if reader:
            reader.read()
        else:
            print("Error: Please select a file type first.")

    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("Invalid input, try again.")
