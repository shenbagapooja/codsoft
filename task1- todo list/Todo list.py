import tkinter as tk
from tkinter import messagebox

# --- Functions ---

def add_task():
    task = task_entry.get()
    if task == "" or task == "Enter your task here...":
        messagebox.showwarning("Warning", "Please enter a task first!")
    else:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)

def delete_task():
    try:
        selected = task_listbox.curselection()[0]
        task_listbox.delete(selected)
    except:
        messagebox.showwarning("Warning", "Please select a task to delete!")

def mark_done():
    try:
        selected = task_listbox.curselection()[0]
        task = task_listbox.get(selected)
        if "✔" not in task:
            task_listbox.delete(selected)
            task_listbox.insert(selected, "✔" + task)
        else:
            messagebox.showinfo("Info", "Task is already marked as done!")
    except:
        messagebox.showwarning("Warning", "Please select a task to mark as done!")

def clear_placeholder(event):
    if task_entry.get() == "Enter your task here...":
        task_entry.delete(0, tk.END)

def restore_placeholder(event):
    if task_entry.get() == "":
        task_entry.insert(0, "Enter your task here...")

# --- Main Window ---

root = tk.Tk()
root.title("My To-Do List App")
root.geometry("400x500")
root.resizable(False, False)

# Title label
title_label = tk.Label(root, text="To-Do List", font=("Arial", 20, "bold"))
title_label.pack(pady=10)

# Listbox to show tasks
task_listbox = tk.Listbox(root, width=40, height=12, font=("Arial", 12))
task_listbox.pack(pady=10)

# Add a default task
task_listbox.insert(tk.END, "Give the task to do")

# Entry field
task_entry = tk.Entry(root, width=30, font=("Arial", 12))
task_entry.insert(0, "Enter your task here...")
task_entry.bind("<FocusIn>", clear_placeholder)
task_entry.bind("<FocusOut>", restore_placeholder)
task_entry.pack(pady=5)

# Buttons
add_button = tk.Button(root, text="Add Task", width=20, bg="lightblue", command=add_task)
add_button.pack(pady=5)

done_button = tk.Button(root, text="Mark as Done", width=20, bg="pink", command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, bg="salmon", command=delete_task)
delete_button.pack(pady=5)

root.mainloop()
