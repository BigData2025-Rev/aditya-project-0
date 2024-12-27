from page import Page
from taskstatus import TaskStatus
from task import Task

import datetime

class Todo:
    def __init__(self):
        self.pages = []

    def get_pages(self):
        return self.pages
    
    def add_page(self, page):
        self.pages.append(page)
    
    def remove_page(self, page):
        self.pages.remove(page)


if __name__=='__main__':
    todo_app = Todo()
    page = Page("To be done ASAP")
    taskstatus = TaskStatus
    tasks = [Task("Finish Project 0",  taskstatus.OPEN, datetime.datetime(2024, 12, 30, 6, 0, 0), task_tag="needs to be done"),
            Task("Practise SQL", taskstatus.OPEN, datetime.datetime(2024, 12, 26, 23, 59, 0), task_tag="improvement"),
            Task("Sign up for AWS", taskstatus.OPEN, datetime.datetime(2024, 12, 26, 18, 0, 0)),
            Task("Tell me about yourself", taskstatus.OPEN, datetime.datetime(2024, 12, 27, 23, 59, 0), task_tag="needs to be done")]

    for task in tasks:
        page.add_task(task)

    todo_app.add_page(page=page)
    print(todo_app)
    print(todo_app.get_pages())
    print(todo_app.get_pages()[0].print_tasks())
