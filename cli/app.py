import os
import sys

root_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))

sys.path.append(root_dir)


from views import introview, taskview, loadtaskview, edittaskview, viewtask

from collections import deque
import time

registry = {
    'introview': introview.IntroView,
    'taskview': taskview.TaskView,
    'loadtaskview': loadtaskview.LoadTaskView,
    'edittaskview': edittaskview.EditTaskView,
    'viewtask': viewtask.ViewTask,
    'return_to_main_menu': None
}

navigate_registry = {
    'backto': 1
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
        
        # process back navigation.
        if '_' in return_val:
            commands = return_val.split("_")
            while registry[commands[1]] != views[-1][0]:
                views.pop()
            continue

        # only main menu doesn't have args.
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
            print("\033[H\033[J", end="")
            print("\n\n\nExiting...\n\n", flush=True)
            time.sleep(0.5)
            print("\033[H\033[J", end="")
