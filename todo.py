tasks = {}

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
        print(f"{tasks[task_name]} --> DONE!")
        tasks.pop(task_name)

while True:
    user_choice = input("What to do?\n(1): Add Task\n(2): List Tasks\n")
    if (user_choice == "1"):
        add_task()
    elif (user_choice == "2"):
        list_tasks()
    