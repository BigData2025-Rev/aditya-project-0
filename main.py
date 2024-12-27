"""Main entry point of the application"""


import argparse
from dataobjects.csvfile import CSV


def process_csv(csv_file=""):
    """Processes csv, if source is csv."""
    dataobj = CSV(csv_file)
    data = dataobj.read()
    print(data)


def process_json(json_file=""):
    """TODO: """
    pass


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="CSV parser tool.")
    parser.add_argument("--csv-file", help="Please enter the path\
                         to a valid csv file.", default=None)

    args = parser.parse_args()
    if not args.csv_file and not args.json_file:
        print("Please select a csv file to process!")

    if args.csv_file:
        process_csv(args.csv_file)

