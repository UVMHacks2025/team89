# # v1

# import dataclasses

# class todo:
#     task_name: str
#     task_description: str
#     task_priority: int # maybe have a corresponding color for different priorities
#     start_time: int # unix timestamp on construction
#     finish_time: int # unix timestamp when finish_task is called

# tasks = {}
# finished_tasks = {}

# # Todo
# # task name
# # task description
# # priority
# # started timestamp
# # finished timestamp

# def add_task(task_name: str, task_description):
#     task_name = input("Task name: ")
#     task_description = input("Task description: ")
#     tasks[task_name] = task_description

# def list_tasks():
#     print(tasks)

# def finish_task(task_name: str):
#     if task_name:
#         finished_tasks[task_name] = tasks.pop(task_name)
#         print(f"DONE!\n{finished_tasks}")

# while True:
#     user_choice = input("What to do?\n(1): Add Task\n(2): List Tasks\n(3): Finish Task")
#     if (user_choice == "1"):
#         task_name = input("Task name: ")
#         task_description = input("Task description: ")
#         add_task(task_name, task_description)
#     elif (user_choice == "2"):
#         list_tasks()
#     elif (user_choice == "3"):
#         list_tasks()
#         task_name = input("Which task have you finished? press enter to go back")
#         finish_task(task_name)
    
import dataclasses
import time

class Todo:
    task_name: str
    task_description: str
    task_priority: int # maybe have a corresponding color for different priorities
    start_time: int # unix timestamp on construction
    finish_time: int # unix timestamp when finish_task is called

DEFAULT_PRIORITY = 1

tasks = {}
finished_tasks = {}

# Todo
# task name
# task description
# priority
# started timestamp
# finished timestamp

def add_task(task_name: str, task_description, priority: int):
    start_time = int(time.time())
    finish_time = None

    tasks[task_name] = Todo(task_name, task_description, priority, start_time, finish_time)

def list_tasks():
    print(tasks)

def finish_task(task_name: str):
    finished_tasks[task_name] = tasks.pop(task_name)
    finished_tasks[task_name].finish_time = int(time.time())

if __name__ == "__main__":
    add_task("test task", "This is a test!", 1)
    

# while True:
#     print()
#     user_choice = input("What to do?\n(1): Add Task\n(2): List Tasks\n(3): Finish Task")
#     if (user_choice == "1"):
#         task_name = input("Task name: ")
#         task_description = input("Task description: ")
#         add_task(task_name, task_description)
#     elif (user_choice == "2"):
#         list_tasks()
#     elif (user_choice == "3"):
#         list_tasks()
#         task_name = input("Which task have you finished? press enter to go back")
#         finish_task(task_name)
    