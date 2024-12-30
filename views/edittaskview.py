# edittaskview.py

import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)

import copy
from tabulate import tabulate

from views.baseview import BaseView
from todo.taskstatus import TaskStatus
from todo.page import Page
from dataobjects.csvfile import CSV


class EditTaskView(BaseView):
    menu_items = 4
    task_status_lookup = {TaskStatus.OPEN:'OPEN', TaskStatus.COMPLETE:'COMPLETE'}

    def __init__(self, page):
        self.page = page

    def print_menu(self):
        print("\033[H\033[J", end="")
        task_lookup = {1: 'OPEN', 2: 'COMPLETE'}
        dict_tasks = copy.deepcopy(self.page.get_tasks())
        tasks = [task.__to__dict__() for task in dict_tasks]
        for task in tasks:
            task['task_status'] = task_lookup[task['task_status']]
        table = tabulate(tasks, headers='keys', tablefmt='pretty')
        lines = table.splitlines()
        lines_with_padding = [("\t" * 2 + line) for line in lines]

        indented_lines = "\n".join(lines_with_padding)
        print(indented_lines)
        print("\n\n")

        print("Please select an option from below.\n", flush=True)
        print("\t1. Change task name.\n", flush=True)
        print("\t2. Change task status.\n", flush=True)
        print("\t3. Save page.\n", flush=True)
        print("\t4. Go back.\n", flush=True)

    def process_user_input(self):
        self.print_menu()
        user_input = input("Enter your choice: ")
        while True:
            while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
                print("Incorrect choice\n")
                print("Please select a valid choice.\n")
                self.print_menu()
                user_input = input("Enter your choice: ")

            user_input = int(user_input)
            match user_input:
                case 1:
                    old_task_name = input("Enter task name to change: ")
                    while not self.page.get_task(old_task_name):
                        print("Task not found.")
                        old_task_name = input("Enter task name to change: ")
                    new_task_name = (input("Enter new task name: "))
                    while True:
                        try:
                            new_task_name = str(new_task_name)
                        except ValueError:
                            print("Not a string value")
                            continue
                        break
                    self.page.get_task(old_task_name).set_task_name(new_task_name)
                case 2:
                    old_task_name = input("Enter task name to change: ")
                    task = self.page.get_task(old_task_name)
                    while not task:
                        old_task_name = input("Enter task name to change: ")
                        task = self.page.get_task(old_task_name)

                    print(f"Current task status is: {self.task_status_lookup[task.get_task_status()]}\nChange to {self.task_status_lookup[~task.get_task_status()]} ?\n")
                    new_task_status = input("Enter 1 for YES 2 for NO: ")
                    while new_task_status not in ['1', '2']:
                        print("Invalid input. Enter again.\n")
                        new_task_status = input("Enter 1 for YES 2 for NO: ")
                    new_task_status = int(new_task_status)
                    if new_task_status == 1:
                        self.page.get_task(old_task_name).set_task_status(~task.get_task_status())
                case 3:
                    page_name = input("Enter a page name: ")
                    invalid_input = False
                    for c in page_name:
                        if c in ['/', ' ', '\\']:
                            invalid_input = True
                    while invalid_input:
                        print("file name cannot contain / \\ or spaces")
                        page_name = input("Enter a page name: ")
                        invalid_input = False
                        for c in page_name:
                            if c in ['/', ' ', '\\']:
                                invalid_input = True
                    page = Page(page_name, copy.deepcopy(self.page.tasks))
                    csv = CSV()
                    csv.write(page)
                    continue
                case 4:
                    return 'back_taskview', self.page
                case default:
                    return 'back_taskview', self.page


if __name__=='__main__':
    from todo.page import create_sample_page
    page = create_sample_page()
    editview = EditTaskView(page)
    method, arg = editview.process_user_input()
