import dataclasses

class todo:
    task_name: str
    task_description: str
    task_priority: int # maybe have a corresponding color for different priorities
    start_time: int # unix timestamp on construction
    finish_time: int # unix timestamp when finish_task is called

tasks = {}
finished_tasks = {}

# Todo
# task name
# task description
# priority
# started timestamp
# finished timestamp



def add_task():
    task_name = input("Task name: ")
    task_description = input("Task description: ")
    tasks[task_name] = task_description

def list_tasks():
    print(tasks)

def finish_task():
    list_tasks()
    task_name = input("Which task have you finished? press enter to go back")
    if task_name:
        finished_tasks[task_name] = tasks.pop(task_name)
        print(f"DONE!\n{finished_tasks}")

while True:
    user_choice = input("What to do?\n(1): Add Task\n(2): List Tasks\n(3): Finish Task")
    if (user_choice == "1"):
        add_task()
    elif (user_choice == "2"):
        list_tasks()
    elif (user_choice == "3"):
        finish_task()
    