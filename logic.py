import json
import os

FILE_NAME = "tasks.json"


# Load tasks from file
def load_tasks():
    if not os.path.exists(FILE_NAME):
        return []

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []   # corrupted JSON handled safely


# Save tasks
def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file, indent=4)


# Add task
def add_task(tasks, text):
    tasks.append({"task": text, "done": False})
    return tasks


# Delete task
def delete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return tasks


# Mark task complete
def complete_task(tasks, index):
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
    return tasks