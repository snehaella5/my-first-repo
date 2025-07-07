import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Oops!", "Please enter a task.")

def delete_task():
    selected = task_listbox.curselection()
    if selected:
        task_listbox.delete(selected)
    else:
        messagebox.showwarning("Oops!", "Please select a task to delete.")

def clear_all():
    task_listbox.delete(0, tk.END)

# GUI Setup
root = tk.Tk()
root.title("📝 To-Do List")
root.geometry("400x400")

# Entry Field
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=10)

# Buttons
add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack()

clear_btn = tk.Button(root, text="Clear All", command=clear_all)
clear_btn.pack()

# Task List
task_listbox = tk.Listbox(root, font=("Arial", 14), height=10)
task_listbox.pack(pady=10, fill=tk.BOTH, expand=True)

root.mainloop()
