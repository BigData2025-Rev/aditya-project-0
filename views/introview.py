from views.baseview import BaseView

class IntroView(BaseView):
    menu_items = 2

    def print_menu(self):
        print("\033[H\033[J", end="")
        print("Please select an option from below.\n", flush=True)
        print("\t1. Load task from file.\n", flush=True)
        print("\t2. Exit\n", flush=True)

    def process_user_input(self):
        self.print_menu()
        user_input = input("Enter your choice: ")
        while user_input not in [str(i) for i in range(1, self.menu_items+1)]:
            print("Incorrect choice\n", flush=True)
            print("Please select a valid choice.\n", flush=True)
            self.print_menu()
            user_input = input("Enter your choice: ")

        user_input = int(user_input)
        match user_input:
            case 1:
                user_input = None
                return 'loadtaskview', None
            case 2:
                return 'exit', None
