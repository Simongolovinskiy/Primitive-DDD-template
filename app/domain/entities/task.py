class Task:
    def __init__(self, task_id, title, description, user_assigned=None, completed=False):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.user_assigned = user_assigned
        self.completed = completed
