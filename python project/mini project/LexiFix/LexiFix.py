import tkinter as tk
from textblob import TextBlob
from tkinter import messagebox

def check_spelling():
    text = entry.get("1.0", tk.END)
    blob = TextBlob(text)
    corrected_text = str(blob.correct())
    result.delete("1.0", tk.END)
    result.insert(tk.END, corrected_text)
    messagebox.showinfo("SpellGenius", "Spelling check complete! ✅")

# GUI Setup
root = tk.Tk()
root.title("🧠 SpellGenius - Smart Spell Checker")
root.geometry("600x500")

# Input Label and Box
tk.Label(root, text="Enter your text:", font=("Arial", 14)).pack(pady=5)
entry = tk.Text(root, font=("Arial", 14), height=8)
entry.pack(pady=10)

# Button
tk.Button(root, text="🔍 Check Spelling", font=("Arial", 12), command=check_spelling).pack(pady=10)

# Result Box
tk.Label(root, text="Corrected text:", font=("Arial", 14)).pack(pady=5)
result = tk.Text(root, font=("Arial", 14), height=8, bg="#f0f0f0")
result.pack(pady=10)

root.mainloop()
# This is a simple spell checker application using Tkinter and TextBlob.
# It allows users to enter text, check for spelling errors, and see the corrected text.