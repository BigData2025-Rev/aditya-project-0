# csvfile.py
# Aditya Kishan Ankaraboyana
"""The main Csvfile object that helps parse and process CSVs."""
import pandas as pd
from pandas.api import types
import spacy
import matplotlib.pyplot as plt
# from langchain_openai import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

from blueprint.data import Data


class Csvfile(Data):
    """Csvfile class"""
    def __init__(self, datasource):
        super().__init__(datasource=datasource)
        self.parse_datafile()

    def parse_datafile(self, criteria=TODO):
        """Inherited from Data. Parses csv in this case."""
        try:
            with open(self.datasource, "r", encoding='utf-8') as csvfile:
                self.df = pd.read_csv(csvfile)
        except Exception as e:
            print(e)

    def print_menu(self):
        """Prints the menu."""
        print("What would you like to do ?")
        print("1. Generate summary report.")
        print("2. Create a custom query.")
        print("3. Create plots from columns.")
        print("4. Exit\n")

    def get_column_names(self):
        """This method get input from the user and sanitizes it.
           It also handles user input exceptions.
        """
        while True:
            user_input = input("Please enter column names as comma separated values: ").strip()

            if not user_input:
                print("Column values are required!\n")
                continue

            try:
                value_list = [value.strip() for value in user_input.split(',')]
                value_list = [str(value) for value in value_list]
                if len(value_list) != len(set(value_list)):
                    raise ValueError("Duplicate column names not allowed!")
                self.df.columns = value_list
                return
            except ValueError as e:
                print(f"Invalid input. Error: {e} Please enter valid values.")
                continue

    def generate_report(self):
        """This method generates a prelimnary report for the given dataframe."""
        print("Generate report function.\n")
        self.get_column_names()
        outputfilename = input("Enter file to generate report: ")
        with open(outputfilename, "w", encoding='utf-8') as file:
            for column in self.df.columns:
                file.write(f"For the column {column}, the highest occuring value\
                            is {self.df[column].mode()[0].to_string()}.\n")

    def print_data_columns(self):
        """Specialized to print data columns."""
        print("Print data function.")

    def create_plots(self):
        self.get_column_names()
        X = input("Please enter column in x-axis: ")
        Y = input("Please enter column in y-axis: ")
        print(f"Is type numeric: {types.is_numeric_dtype(self.df[X])}{types.is_numeric_dtype(self.df[Y])}")
        while X not in self.df.columns:
            print("Invalid column or non numberic type.\n")
            X = input("Please enter column in x-axis: ")
        while Y not in self.df.columns and types.is_numeric_dtype(self.df[X]):
            print("Invalid column or non numberic type.\n")
            Y = input("Please enter column in y-axis: ")
        self.df.plot(x=X, y=Y, kind='line')
        try:
            plt.show()
        except TypeError as e:
            print(f"Could not create plot: {e}\n Enter a numeric column that can be plotted.")


    def create_custom_query(self):
        """Use of custom queries to generate custom insights to data."""
        nlp = spacy.load('en_core_web_sm')
        query = input("Please enter the query you would like to get an answer for?\n>> ")
        doc = nlp(query)
        for token in doc:
            print(token.text, token.pos_)

    def menu(self):
        """Main menu for the Csvfile object. Handles input in REPL style."""
        while True:
            self.print_menu()
            user_input = input("Enter your input here: ")
            while user_input not in [str(i+1) for i in range(4)]:
                user_input = input("Incorrect option. Choose again: ")

            user_input = int(user_input)
            match user_input:
                case 1: self.generate_report()
                case 2: self.create_custom_query()
                case 3: self.create_plots()
                case 4:
                    print("Exiting...")
                    break
        # self.validate_user_input(user_input)
