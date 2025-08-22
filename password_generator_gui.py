import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length < 4:
            messagebox.showerror("Error", "Password must be at least 4 characters long.")
            return

        chars = string.ascii_letters + string.digits + string.punctuation
        password = ''.join(random.choice(chars) for _ in range(length))
        result_entry.delete(0, tk.END)
        result_entry.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number.")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(result_entry.get())
    messagebox.showinfo("Copied", "Password copied to clipboard!")

# GUI setup
root = tk.Tk()
root.title("🔐 Password Generator")
root.geometry("400x200")
root.resizable(False, False)

# Widgets
title = tk.Label(root, text="Password Generator", font=("Arial", 16))
title.pack(pady=10)

length_label = tk.Label(root, text="Password length:")
length_label.pack()

length_entry = tk.Entry(root, width=10)
length_entry.pack()

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.pack(pady=5)

result_entry = tk.Entry(root, width=30)
result_entry.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()
