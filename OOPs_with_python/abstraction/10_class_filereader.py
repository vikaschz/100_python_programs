"""
Create an abstract class FileReader with read_file(). Implement TextReader and PDFReader.
"""
from abc import ABC, abstractmethod

class FileReader(ABC):

    @abstractmethod
    def read_file(self):
        pass


class TextReader(FileReader):
    def read_file(self):
        print("Reading content from a text file...")


class PDFReader(FileReader):
    def read_file(self):
        print("Reading content from a PDF file...")

text = TextReader()
pdf = PDFReader()

text.read_file()
pdf.read_file()
