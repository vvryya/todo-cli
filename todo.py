import json
import sys
import os

com = input() # command inputrem

tasksFile = "tasks.json"

def loadTasks():
    if not os.path.exists(tasksFile):
        print("NO FILE")
        return []
    with open(tasksFile, "r") as f:
        return json.load(f)
    
def saveTasks(tasks):
    with open(tasksFile, "w") as f:
        json.dump(tasks, f, indent=2)

def addTask(description):
    tasks = loadTasks()
    tasks.append({"description": description})
    saveTasks(tasks)
    print(f"Task added: {description}")
    
def removeTask(index):
    tasks = loadTasks()
    try:
        removed = tasks.pop(index - 1)
        saveTasks(tasks)
        print(f"Task removed: {removed['description']}")
    except IndexError:
        print("Invalid task number.")

def listTasks():
    tasks = loadTasks()
    if not tasks:
        print("No tasks found.")
        return
    print("Tasks:")
    for idx, task in enumerate(tasks, start=1):
        print(f"{idx}. {task['description']}")

def helpPage():
    print("""
ToDo CLI - simple task manager
Commands:
"add 'task description'" - add task
"list" - list all tasks
"remove task_number" - remove task at index
"stop" - stop""")
    
while com != "stop":
    command = com.split(' ')

    if command[0] == "list":
        listTasks()
    elif command[0] == "add" and len(command) > 1:
        addTask(" ".join(command[1:]))
    elif command[0] == "remove" and len(command) == 2:
        removeTask(int(command[1]) - 1)
    else: 
        helpPage()

    print()
    com = input()