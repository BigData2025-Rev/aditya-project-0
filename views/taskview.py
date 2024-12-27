import time

from views.baseview import BaseView
from todo.page import Page
from dataobjects.csvfile import CSV


class TaskView(BaseView):
    menu_items = 3

    def __init__(self, page):
        self.page = page

    def print_menu(self):
        print("\033[H\033[J", end="")
        print("Please select an option from below.\n", flush=True)
        print("\t1. Edit Task.\n")
        print("\t2. Save Tasks to a Page.\n")
        print("\t3. Go back to main menu.\n")

    def process_user_input(self):
        self.print_menu()
        user_input = input("Enter your choice: ")
        while True:
            while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
                print("Incorrect choice\n")
                print("Please select a valid choice.")
                self.print_menu()
                user_input = input("Enter your choice: ")
        
            user_input = int(user_input)
            match user_input:
                case 1:
                    task_name = input("Enter task name: ")
                    while task_name not in [task.task_name for task in self.tasks]:
                        print("Could not find task_name.\n")
                        task_name = input("Enter task name: ")
                    
                    return 'edittask', task_name

                case 2:
                    page_name = input("Enter a page name: ")

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
                    page = Page(page_name, self.page.tasks)
                    csv = CSV()
                    csv.write(page)
                    continue
                case 3:
                    break

        return 'return_to_main_menu'
        

