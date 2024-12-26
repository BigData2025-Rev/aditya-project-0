# data.py
# Aditya Kishan Ankaraboyana
from abc import abstractmethod


class Data:
    """This class is the parent class for different types of data files
       Formats allowed are json and csv.
    """

    def __init__(self, datasource):
        self.datasource = datasource

    @abstractmethod
    def parse_datafile(self):
        pass

    @abstractmethod
    def menu(self):
        pass
