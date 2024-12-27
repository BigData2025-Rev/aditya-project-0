import os
import sys
import time

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)


from views import introview, taskview, loadtaskview
from collections import deque
registry = {
    'introview': introview.IntroView,
    'taskview': taskview.TaskView,
    'loadtaskview': loadtaskview.LoadTaskView,
    'return_to_main_menu': None
}

if __name__=="__main__":
    print("Welcome to TaskRev\n")
    views = deque([(introview.IntroView, [None])])

    while views:
        current_view, args = views[-1]
        if len(args) == 1 and not args[0]:
            return_val, *returned_args = current_view().process_user_input()
        else:
            return_val, *returned_args = current_view(*args).process_user_input()
        
        if return_val in registry:
            if not registry[return_val]:
                views.pop()
            else:
                views.append((registry[return_val], returned_args))
        else:
            if return_val == 'exit':
                while views:
                    views.pop()
            else:
                while views[-1][0] != introview.IntroView:
                    views.pop()
        if not views:
            print("\n\n\t\t\t\t\tExiting...\n\n", flush=True)
            time.sleep(2)
            print("\033[H\033[J", end="")
            
            

