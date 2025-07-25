import json
import sys
import os

com = input() # command input

tasksFile = "tasks.json"

def loadTasks():
    if not os.path.exists(tasksFile):
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

while com != "":
    command = com.split('')