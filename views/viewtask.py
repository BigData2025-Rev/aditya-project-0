import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)

import copy

from views.baseview import BaseView

from tabulate import tabulate

class ViewTask(BaseView):
    menu_items = 1

    def __init__(self, page):
        self.page = page

    def print_card(self):
        plist_path = self.page.page_name+".plist"

        dict_tasks = copy.deepcopy(self.page.get_tasks())
        tasks = [task.__to__dict__() for task in dict_tasks]
        table = tabulate(tasks, headers='keys', tablefmt='pretty')
        lines = table.splitlines()
        lines_with_padding = [("\t" * 2 + line) for line in lines]

        indented_lines = "\n".join(lines_with_padding)
        print(indented_lines)
        print("\n\n")
        # with open(plist_path, 'wb') as f:
        #     plistlib.dump(tasks, f)
        # import subprocess
        # try:
        #     subprocess.run(['open', '-a', 'Xcode', plist_path], check=True)
        #     print(f"Successfully opened: {plist_path}")
        # except subprocess.CalledProcessError as e:
        #     print(f"Error occurred while opening the plist: {e}")
        

    def print_menu(self):
        print("\033[H\033[J", end="")
        self.print_card()
        print("Please select an option from below.\n", flush=True)
        print("\t1. Back to main menu.\n")

    def process_user_input(self):
        self.print_menu()
        user_input = input("Enter your choice: ")
        while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
                print("Incorrect choice\n")
                print("Please select a valid choice.")
                self.print_menu()
                user_input = input("Enter your choice: ")
        
        user_input = int(user_input)
        match user_input:
            case 1:
                return 'back_taskview', self.page

if __name__=='__main__':
    from todo.page import create_sample_page
    page = create_sample_page()
    print(page.get_tasks())
    viewtask = ViewTask(page)
    methodname, arg = viewtask.process_user_input()

    print(arg.get_tasks())