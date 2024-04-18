from app.domain.entities.task import Task


class TaskService:
    def __init__(self):
        self.tasks = []

    def create_task(self, task_id, title, description, user_assigned=None):
        task = Task(task_id, title, description, user_assigned)
        self.tasks.append(task)
        return task

    def assign_user_to_task(self, task, user):
        task.user_assigned = user

    def mark_task_as_completed(self, task):
        task.completed = True

    def get_all_tasks(self):
        return self.tasks