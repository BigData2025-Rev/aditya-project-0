import time

from views.baseview import BaseView
from todo.page import Page
from dataobjects.csvfile import CSV


class TaskView(BaseView):
    menu_items = 5

    def __init__(self, page):
        self.page = page

    def print_menu(self):
        print("\033[H\033[J", end="")
        print("Please select an option from below.\n", flush=True)
        print("\t1. Edit Page.\n")
        print("\t2. View Page.\n")
        print("\t3. Add Task.\n")
        print("\t4. Remove Task.\n")
        print("\t5. Go back to main menu.\n")

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
                    return 'edittaskview', self.page
                case 2:
                    return 'viewtask', self.page
                case 3:
                    return 'addtask', self.page
                case 4:
                    return 'removetask', self.page
                case 5:
                    break

        return 'return_to_main_menu'
