import time

from views.baseview import BaseView
from dataobjects.csvfile import CSV
from exception.pathexception import ParentDirectoryNotFound
from exception.csvexception import CSVContentException, CSVFieldNameException

class LoadTaskView(BaseView):
    menu_items = 2

    def print_menu(self):
        print("\033[H\033[J", end="")
        print("Please select an option from below.\n", flush=True)
        print("\t1. Enter path to csv.\n", flush=True)
        print("\t2. Go back to main menu.\n", flush=True)

    def process_user_input(self):
        self.print_menu()
        user_input = input("Enter your choice: ")
        while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
            print("Incorrect choice\n", flush=True)
            print("Please select a valid choice.", flush=True)
            time.sleep(2)
            self.print_menu()
            user_input = input("Enter your choice: ")

        user_input = int(user_input)
        match user_input:
            case 1:
                while True:
                    csv_input_name = input("Enter csv file path >> ")
                    try:
                        csv = CSV(csv_input_name)
                    except ParentDirectoryNotFound as pdn:
                        print("Invalid path. Enter a valid file path.\n", flush=True)
                        continue
                    except CSVFieldNameException as cfn:
                        print("Invalid CSV field names. Provide a valid csv.\n", flush=True)
                        continue
                    except CSVContentException as cc:
                        print("Invalid values in CSV. Provide a valid csv.\n", flush=True)
                        continue
                    break
                page = csv.read()
                print(page)
                return 'taskview', page
            
            case 2:
                return 'return_to_main_menu'
                
