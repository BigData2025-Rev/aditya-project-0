# csvfile.py
# Aditya Kishan Ankaraboyana

"""The main Csvfile object that helps parse and process CSVs."""

import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)

# import pandas as pd
import csv
# from pandas.api import types
# import spacy
# import matplotlib.pyplot as plt
# from langchain_openai import OpenAI
# from langchain.prompts import PromptTemplate
# from langchain.chains import LLMChain

from blueprint.data import Data
from exception.csvexception import CSVContentException
from exception.csvexception import CSVFieldNameException
from todo.page import Page
from todo.task import Task


class CSV(Data):
    """Csvfile class"""
    def __init__(self, datasource=None):
        if datasource:
            super().__init__(False, datasource=datasource)
            self.validate_file_contents(Task.get_valid_task_fieldnames(Task))

    def validate_file_contents(self, expected_attributes):
        """This method checks to see if the data
        in the CSV is in the right format.
        """
        with open(self.datasource, "r") as file:
            try:
                reader = csv.DictReader(file)
                for fieldname in reader.fieldnames:
                    if fieldname not in expected_attributes:
                        raise CSVFieldNameException(f"Incorrect field name: {fieldname}")
                for row in reader:
                    if not row['task_name'] or not row['task_status']:
                        raise CSVContentException("Values for columns task_name and task_status are required.")
                    # for field
                    task_name = str(row['task_name'])
                    try:
                        task_status = int(row['task_status'])
                    except ValueError as ve:
                        raise CSVContentException("Incorrect value for attribute")

            except Exception as e:
                raise e

    def read(self):
        tasks = []
        page_name = self.datasource.split(".csv")[0]
        with open(self.datasource, "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                args = []
                for fieldname in Task.get_valid_task_fieldnames(Task):
                    args.append(row[fieldname])
                task = Task(*args)
                tasks.append(task)
        return Page(page_name, tasks)

    def write(self, page):
        fieldnames = page.tasks[0].get_valid_task_fieldnames(Task)
        taskdicts = []
        for task in page.tasks:
            taskdicts.append(task.__to__dict__())
        with open(page.page_name, "w") as file:
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(taskdicts)


if __name__=="__main__":
    from todo.task import Task
    from todo.taskstatus import TaskStatus as taskstatus
    try:
        CSV = CSV("./testsamples/sampleerror.csv")
        CSV.validate_file_contents(Task.get_valid_task_fieldnames(Task))

        CSV.read()

        tasks = [Task("Finish Project 0",  taskstatus.OPEN),
                Task("Practise SQL", taskstatus.OPEN),
                Task("Sign up for AWS", taskstatus.OPEN),
                Task("Tell me about yourself", taskstatus.OPEN)]

        page = Page("TODOd", tasks)


        CSV.write(page)
    except Exception as e:
        print(e)
