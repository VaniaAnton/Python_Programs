import tkinter as tk
from tkinter import messagebox

result = 0
def add():
    global result
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = a+b
        result_label.config(text=f"{result}")
    except ValueError:
        messagebox.showerror("ERROR", "write a correct number!")

def sub():
    global result
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = a-b
        result_label.config(text=f"{result}")
    except ValueError:
        messagebox.showerror("ERROR", "write a correct number!")

def mul():
    global result
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        result = a*b
        result_label.config(text=f"{result}")
    except ValueError:
        messagebox.showerror("ERROR", "write a correct number!")

def div():
    global result
    try:
        a = float(entry_a.get())
        b = float(entry_b.get())
        if b > 0:
            result = a/b
            result_label.config(text=f"{result}")
        else:
            messagebox.showerror("ERROR", "Cannot divide to zero")
    except ValueError:
        messagebox.showerror("ERROR", "write a correct number!")

def reset():
    global result
    result =0
    result_label.config(text=f"{result}")
# GUI
root = tk.Tk()
root.title("Calculator")
root.geometry("600x700")

tk.Label(root, text="Enter first number")
entry_a = tk.Entry(root)
entry_a.grid(row=1, column=5, columnspan=2)

tk.Label(root, text="Enter second number")
entry_b = tk.Entry(root)
entry_b.grid(row=2, column=5, columnspan=2)
button1=tk.Button(root, text="+", command=add)
button1.grid(row=4,column=5)
button2=tk.Button(root, text="-", command=sub)
button2.grid(row=5,column=5)
button3=tk.Button(root, text="*", command=mul)
button3.grid(row=6,column=5)
button4=tk.Button(root, text="/", command=div)
button4.grid(row=7,column=5)
button5=tk.Button(root, text="Reset", command=reset)
button5.grid(row=8,column=5)

result_label = tk.Label(root, text="")
result_label.grid(row=3, column=5, columnspan=2)
root.mainloop()