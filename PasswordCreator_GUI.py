import random
import string
import tkinter as tk
from tkinter import messagebox

# function to generate the password
def password_creator():
    try:
        length = int(entry_length.get())
        if length < 4:
            messagebox.showerror("ERROR, tne number could not be less than 4 symbols")
            return
        
        symbols =  string.ascii_letters  + string.digits + string.punctuation
        password = ''.join(random.choice(symbols) for _ in range(length))
        
        entry_password.delete(0, tk.END) #clear the field
        entry_password.insert(0, password) #setting the password
        
    except ValueError:
        messagebox.showerror("ERROR", "Enter the number for length!")

# Function to cope the password
def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("COPIED", "Password copied to the clipboard")

root = tk.Tk()
root.title("Password Creator")
root.geometry("300x200")
root.resizable(False, False)

tk.Label(root, text="Enter the length of password:").pack()
entry_length = tk.Entry(root)
entry_length.pack()

btn_generate = tk.Button(root, text="Generate", command=password_creator)
btn_generate.pack()

entry_password = tk.Entry(root, font=("Times New Roman", 12), justify="center")
entry_password.pack()

btn_copy = tk.Button(root, text="Copy", command=copy_to_clipboard)
btn_copy.pack()

root.mainloop()

