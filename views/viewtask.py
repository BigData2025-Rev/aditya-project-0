from views.baseview import BaseView

from colorama import Fore, Back, Style, init
import plistlib

# Initialize Colorama
init(autoreset=True)

class ViewTask(BaseView):
    menu_items = 1

    def __init__(self, page):
        self.page = page

    def print_card(self):
        plist_path = self.page.page_name+".plist"
        tasks = [task.__to__dict__() for task in self.page.tasks]
        with open(plist_path, 'wb') as f:
            plistlib.dump(tasks, f)
        import subprocess
        try:
            subprocess.run(['open', '-a', 'Xcode', plist_path], check=True)
            print(f"Successfully opened: {plist_path}")
        except subprocess.CalledProcessError as e:
            print(f"Error occurred while opening the plist: {e}")
        

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
