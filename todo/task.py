class Task:
    def __init__(self, task_name, task_status, task_deadline=None, task_tag=None, task_category=None, task_severity=None):
        self.task_name = task_name
        self.task_deadline = task_deadline
        self.task_tag = task_tag
        self.task_status = task_status
        self.task_category = task_category
        self.task_severity = task_severity

    def get_task_name(self):
        return self.task_name

    def get_task_status(self):
        return self.task_status

    def get_task_deadline(self):
        return self.task_deadline

    def get_task_tag(self):
        return self.task_tag

    def get_task_category(self):
        return self.task_category

    def get_task_severity(self):
        return self.task_severity

    def set_task_name(self, task_name):
        self.task_name = task_name

    def set_task_status(self, task_status):
        self.task_status = task_status

    def set_task_deadline(self, task_deadline):
        self.task_deadline = task_deadline

    def set_task_tag(self, task_tag):
        self.task_tag = task_tag

    def set_task_category(self, task_category):
        self.task_category = task_category

    def set_task_severity(self, task_severity):
        self.task_severity = task_severity

    def __repr__(self):
        return (
            f"Task(\n"
            f"  task_name: {self.get_task_name()},\n"
            f"  task_tatus: {self.get_task_status()},\n"
            f"  task_deadline: {self.get_task_deadline()},\n"
            f"  task_tag: {self.get_task_tag()},\n"
            f"  task_category: {self.get_task_category()},\n"
            f"  task_severity: {self.get_task_severity()}\n"
            f")"
        )