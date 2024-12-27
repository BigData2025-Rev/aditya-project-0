# data.py
# Aditya Kishan Ankaraboyana

"""
    This class defines the expected behavior of data input files.
"""

import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)

from abc import abstractmethod
from pathlib import Path
from exception.pathexception import ParentDirectoryNotFound


class Data:
    """This class is the parent class for different types of data files
       Formats allowed are json and csv.
    """

    def __init__(self, datasource):
        self.datasource = datasource
        self.validate_path()

    def validate_path(self):
        """
        This method checks to see if path is valid and
        if the parent directories exist.
        """
        path = Path(self.datasource)
        if not path.parent.exists():
            raise ParentDirectoryNotFound("Parent Directory not found.")

    @abstractmethod
    def validate_file_contents(self):
        """
        This method ensures that the data within the specific file
        format is valid.
        Example: csv has comma separated values and valid column names.
                 json has the right nested values, if any error exists,
                 user is notified.
        """
        pass

    @abstractmethod
    def read(self):
        pass

    @abstractmethod
    def write(self):
        pass


if __name__=="__main__":
    correct_but_parent = "../testsamples/sample.csv"


    data = Data(correct_but_parent)
    print(data)
