# enum.py
"""
    Provides different status for a given task.
    Example: OPEN, CLOSE
"""

from enum import Enum


class TaskStatus(Enum):
    """
        An enumeration of possible status of a task

        taskstatus = TaskStatus()
        task.set_task_status = taskstatus.OPEN
        task.set_task_statu = taskstatus.CLOSE

    """
    OPEN = 1
    COMPLETE = 2

    def __invert__(self):
        return TaskStatus.OPEN if self == TaskStatus.COMPLETE else TaskStatus.COMPLETE
