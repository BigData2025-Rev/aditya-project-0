import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)

import copy
from tabulate import tabulate

from views.baseview import BaseView
from todo.task import Task
from todo.taskstatus import TaskStatus


class RemoveTaskView(BaseView):
    menu_items = 2
    def __init__(self, page):
        self.page = page
    
    def print_menu(self):
        print("\033[H\033[J", end="")
        dict_tasks = copy.deepcopy(self.page.get_tasks())
        task_lookup = {1: 'OPEN', 2: 'COMPLETE'}
        tasks = [task.__to__dict__() for task in dict_tasks]
        for task in tasks:
            task['task_status'] = task_lookup[task['task_status']]
        table = tabulate(tasks, headers='keys', tablefmt='pretty')
        lines = table.splitlines()
        lines_with_padding = [("\t" * 2 + line) for line in lines]

        indented_lines = "\n".join(lines_with_padding)
        print(indented_lines, flush=True)
        print("\n\n", flush=True)
        
        print("Please select an option from below.\n", flush=True)
        print("\t1. Remove task name.\n", flush=True)
        print("\t2. Go back.\n", flush=True)

    def process_user_input(self):
        while True:
            self.print_menu()
            user_input = input("Enter your choice: ")
            while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
                print("Incorrect choice\n")
                print("Please select a valid choice.\n")
                self.print_menu()
                user_input = input("Enter your choice: ")
        
            user_input = int(user_input)
            match user_input:
                case 1:
                    old_task_name = input("Enter task name to remove: ")
                    while not self.page.get_task(old_task_name):
                        print("Task not found.")
                        old_task_name = input("Enter task name to remove: ")
                    self.page.remove_task(old_task_name)
                case 2:
                    return 'back_taskview', self.page


if __name__=='__main__':
    from todo.page import create_sample_page
    page = create_sample_page()
    removeview = RemoveTaskView(page)
    method, arg = removeview.process_user_input()
    print(*arg.get_tasks())