import tkinter as tk
from tkinter import messagebox
from logic import load_tasks, save_tasks, add_task, delete_task, complete_task

tasks = load_tasks()


def refresh():
    listbox.delete(0, tk.END)
    for t in tasks:
        mark = "✔ " if t["done"] else "✘ "
        listbox.insert(tk.END, mark + t["task"])


def add():
    text = entry.get()
    if text == "":
        messagebox.showwarning("Warning", "Enter task")
        return

    add_task(tasks, text)
    entry.delete(0, tk.END)
    save_tasks(tasks)
    refresh()


def delete():
    try:
        index = listbox.curselection()[0]
        delete_task(tasks, index)
        save_tasks(tasks)
        refresh()
    except:
        messagebox.showwarning("Warning", "Select task")


def complete():
    try:
        index = listbox.curselection()[0]
        complete_task(tasks, index)
        save_tasks(tasks)
        refresh()
    except:
        messagebox.showwarning("Warning", "Select task")


# -------- GUI --------
root = tk.Tk()
root.title("To-Do App")
root.geometry("350x400")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

tk.Button(root, text="Add Task", command=add).pack()

listbox = tk.Listbox(root, width=40, height=12)
listbox.pack(pady=10)

tk.Button(root, text="Mark Complete", command=complete).pack(pady=2)
tk.Button(root, text="Delete Task", command=delete).pack(pady=2)

refresh()
root.mainloop()