import tkinter as tk
from time import strftime

def time():
    current_time = strftime('%H:%M:%S %p')
    label.config(text=current_time)
    label.after(1000, time)

root = tk.Tk()
root.title("🕒 Digital Clock")

label = tk.Label(root, font=('Arial', 50), background='black', foreground='lime')
label.pack(anchor='center')

time()
root.mainloop()
