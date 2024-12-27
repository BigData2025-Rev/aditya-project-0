# page.py

"""This module provides a blueprint for the Page within a todo application.
   A page could be thought of as a list, just like a todo list.
"""

class Page:
    """
        Used to create a Page within the application.

        page_name (str): Name of the Page.
        tasks (list): List of all tasks within a Page.

        Methods:
            get_tasks: Used to retrive all tasks in a page.
            add_task: Used to add a task to a page object.
            reorder_task: Used to reorder a task within the page.
            print_tasks: prints all the tasks in a page to the console.
        
        Example:
            page = Page("Example")
            page.add_task(task1)
            page.add_task(task2)
            page.reorder_task(task1, 1)
            page.remove_task(task1)
            page.print_tasks()
            tasks = page.get_tasks()

    """

    def __init__(self, page_name, tasks=[]):
        """Initialize object"""
        self.page_name = page_name
        self.tasks = tasks

    def get_tasks(self):
        """Get all tasks for a page."""
        return self.tasks

    def add_task(self, task):
        """Add task to a page."""
        self.tasks.append(task)

    def remove_task(self, task):
        """Remove task from a page."""
        self.tasks.remove(task)

    def reorder_task(self, task, position):
        """Change the task order in the page."""
        removed_task = self.tasks.pop(task)
        self.tasks.insert(position-1, removed_task)

    def print_tasks(self):
        """Print all tasks within the page."""
        for task in self.tasks:
            print(task)
