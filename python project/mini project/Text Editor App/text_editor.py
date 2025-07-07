import tkinter as tk
from tkinter import filedialog, messagebox

def new_file():
    text_area.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            content = file.read()
            text_area.delete(1.0, tk.END)
            text_area.insert(tk.END, content)

def save_file():
    file_path = filedialog.asksaveasfilename(defaultextension=".txt",
                                             filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w") as file:
            content = text_area.get(1.0, tk.END)
            file.write(content)
            messagebox.showinfo("Saved", "File saved successfully!")

# GUI Setup
ShellWrite = tk.Tk()
ShellWrite.title(" Mini Text Editor")
ShellWrite.geometry("600x400")

# Text Area
text_area = tk.Text(ShellWrite, font=("Arial", 12))
text_area.pack(expand=True, fill="both")

# Menu Bar
menu_bar = tk.Menu(ShellWrite)
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=ShellWrite.quit)

menu_bar.add_cascade(label="File", menu=file_menu)
ShellWrite.config(menu=menu_bar)

ShellWrite.mainloop()
# This is a simple text editor application using Tkinter.
# It allows users to create, open, and save text files.