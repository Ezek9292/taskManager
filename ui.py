import tkinter as tk
from functools import partial
from tkinter import messagebox
import commands

def handle_update (id, title, app):
    if not title:
        messagebox.showerror(title="Edit task", message="Cannot update with Empty task!", parent=app)
    else:
        commands.update_task(id, {"title": title})
        show_all_tasks_frame(app)

def handle_delete(id, app):
    commands.delete_task(id)
    show_all_tasks_frame(app)


def submit_task(title, app):
    if not title:
        messagebox.showerror(title="Add Task", message="Please Add task", parent=app)
    else:
        commands.save_task({"title": title})
        show_all_tasks_frame(app)


def show_edit_task_frame(task, app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10,)

    label = tk.Label(master=frame, text=f"Edit task: {task["title"]}")
    label.grid()

    # add and entry widget and show the task title
    entry = tk.Entry(master=frame)
    entry.insert(0, task["title"])
    entry.grid()

    # add a button with text update for saving the changes

    update_btn = tk.Button(master=frame, text="Update", command=lambda:handle_update(task["_id"], entry.get(),app))
    update_btn.grid(row=2, column=2)

    # add a button with the text Back / Return / cancel to remove the frame

    cancel_btn = tk.Button(master=frame, text="Back", command=lambda: frame.destroy())
    cancel_btn.grid(row=2, column=0)

    frame.tkraise()


def show_add_task_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)
    
    label = tk.Label(master=frame, text="What do you want to add?")
    label.grid()
    entry = tk.Entry(master=frame)
    entry.grid()
    btn = tk.Button(master=frame, text="Submit", command=lambda:submit_task(entry.get(),app))
    btn.grid() 

    

    frame.tkraise()

def show_all_tasks_frame(app):
    frame = tk.Frame(master=app)
    frame.grid(row=0, column=0, sticky="nsew", padx=10, pady=10)


    tasks = commands.get_tasks().to_list()
    for task in tasks:
        checkbtn = tk.Checkbutton(master=frame, text=task["title"])
        checkbtn.grid(row=tasks.index(task), column=0)


        edit_btn = tk.Button(master=frame, text="Edit", command=partial(show_edit_task_frame, task, app))
        edit_btn.grid(row=tasks.index(task), column=1)

        btn = tk.Button(master=frame, text="Delete", command=partial(handle_delete, task["_id"], app))
        btn.grid(row=tasks.index(task), column=2)

    btn = tk.Button(master=frame, text="Add Task", command=lambda: show_add_task_frame(app))
    btn.grid(row=len(tasks)+1, column=0)


    frame.tkraise()

