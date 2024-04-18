from app.application.user_service import UserService
from app.application.task_service import TaskService
from app.presentation.main_window import run_application


def some_business_logic():
    user_service = UserService()
    task_service = TaskService()

    user1 = user_service.create_user(user_id="user_1", name="Alice", email="alice@example.com", age=30)
    user2 = user_service.create_user(user_id="user_2", name="Bob", email="bob@example.com", age=25)

    task1 = task_service.create_task(task_id="task_1", title="Task 1", description="Description of Task 1")
    task2 = task_service.create_task(task_id="task_2", title="Task 2", description="Description of Task 2")

    task_service.assign_user_to_task(task1, user1)
    task_service.assign_user_to_task(task2, user2)

    all_tasks = task_service.get_all_tasks()
    output_text = ""
    for task in all_tasks:
        if task.user_assigned:
            output_text += f"Task '{task.title}' assigned to {task.user_assigned.name}\n"
        else:
            output_text += f"Task '{task.title}' not assigned to any user\n"

    return output_text


if __name__ == "__main__":
    run_application(some_business_logic)
