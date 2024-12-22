import argparse
from csvfile import Csvfile
from jsonfile import Jsonfile


def process_csv(csv_file=""):
    dataobj = Csvfile(csv_file)
    dataobj.menu()


def process_json(json_file=""):
    dataobj = Jsonfile(json_file)


if __name__=='__main__':
    parser = argparse.ArgumentParser(description="CSV parser tool.")
    parser.add_argument("--csv-file", help="Please enter the path to a valid csv file.", default=None)
    parser.add_argument("--json-file", help="Please enter the path to a valid json file.", default=None)

    args = parser.parse_args()
    if not args.csv_file and not args.json_file:
        print("Please select a csv or a json file to process!")

    if args.csv_file:
        process_csv(args.csv_file)

    if args.json_file:
        process_json(args.json_file)
