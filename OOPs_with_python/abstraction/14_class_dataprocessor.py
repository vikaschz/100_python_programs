"""
Create an abstract class DataProcessor with process_data(). Implement CSVProcessor, JSONProcessor, XMLProcessor.
"""

from abc import ABC, abstractmethod


class DataProcessor(ABC):

    @abstractmethod
    def process_data(self):
        pass


class CSVProcessor(DataProcessor):
    def process_data(self):
        print("Processing CSV data...")


class JSONProcessor(DataProcessor):
    def process_data(self):
        print("Processing JSON data...")


class XMLProcessor(DataProcessor):
    def process_data(self):
        print("Processing XML data...")


processors = [CSVProcessor(), JSONProcessor(), XMLProcessor()]

for processor in processors:
    processor.process_data()
