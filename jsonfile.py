import json

from data import Data


class Jsonfile(Data):
    def __init__(self, datasource):
        super.__init__(datasource)

    def parse_datafile(self):
        return super().parse_datafile()

    def menu(self):
        pass
