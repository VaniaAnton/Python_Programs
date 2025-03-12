import time
import tkinter as tk
from tkinter import messagebox

# Timer
def start_timer():
    try:
        total_seconds =int(entry_time.get())
        if total_seconds >0:
            countdown(total_seconds)
        else:
            messagebox.showerror("ERROR", "Enter the time more than 0!")
    except ValueError:
        messagebox.showerror("ERROR", "Enter the number")

def countdown(seconds):
    if seconds>= 0:
        hrs, remainder = divmod(seconds, 3600)
        mins, secs = divmod(remainder, 60)
        label_timer.config(text=f"{hrs:02}:{mins:02}:{secs:02}") #format 00:00:00
        root.after(1000, countdown, seconds-1)
    else:
        messagebox.showerror("The Time is over!", "Timer has been finished")

def stop_timer():
    label_timer.config(text="00:00:00")
# Stopwatch

running = False
start_time = 0
elapsed_time = 0 

def update_stopwatch():
    if running:
        elapsed = time.time() - start_time
        hrs, remainder = divmod(int(elapsed), 3600)
        mins, secs = divmod(remainder, 60)
        label_stopwatch.config(text=f"{hrs:02}{mins:02}:{secs:02}")
        root.after(1000, update_stopwatch)

def start_stopwatch():
    global running, elapsed_time
    if not running:
        running = True
        start_time = time.time() - elapsed_time
        update_stopwatch()

def stop_stopwatch():
    global running, elapsed_time
    running = False
    elapsed_time = time.time() - start_time

def reset_stopwatch():
    global running, start_time, elapsed_time
    running = False
    start_time = 0
    elapsed_time = 0
    label_stopwatch.config(text="00:00:00")

# GUI
root = tk.Tk()
root.title("Timer and Stopwatch")
root.geometry("600x700")
# Timer
tk.Label(root, text="Enter the timer time: (seconds)").pack()
entry_time = tk.Entry(root)
entry_time.pack()

btn_start= tk.Button(root, text="Start", command=start_timer)
btn_start.pack()
btn_stop= tk.Button(root, text="Stop", command=stop_timer)
btn_stop.pack()

label_timer =tk.Label(root, text="00:00:00", font=("Arial", 40))
label_timer.pack()
tk.Label(root, text="----------------------").pack()
# Stopwatch
tk.Label(root, text="Start the stopwatch").pack()
label_stopwatch = tk.Label(root, text="00:00:00", font=("Arial", 40))
label_stopwatch.pack()
btn_startwatch= tk.Button(root, text="Start", command=start_stopwatch)
btn_startwatch.pack()
btn_stopwatch= tk.Button(root, text="Stop", command=start_stopwatch)
btn_stopwatch.pack()
btn_resetwatch= tk.Button(root, text="Reset", command=reset_stopwatch)
btn_resetwatch.pack()
root.mainloop()