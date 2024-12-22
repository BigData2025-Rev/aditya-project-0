import csv
import pandas as pd

from data import Data


class Csvfile(Data):
    def __init__(self, datasource):
        super().__init__(datasource=datasource)
        self.parse_datafile()

    def parse_datafile(self):
        try:
            with open(self.datasource, "r") as csvfile:
                reader = csv.reader(csvfile)
                self.df = pd.DataFrame(reader)
        except Exception as e:
            print(e)

    def menu(self):
        print(self.df.head())
