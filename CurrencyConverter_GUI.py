import requests
import tkinter as tk
from tkinter import messagebox

def get_exchange_rate(base_currency, target_currency):
    url = f"https://api.exchangerate-api.com/v4/latest/{base_currency}"
    try:
        response = requests.get(url)
        data = response.json()
        return data['rates'].get(target_currency, None)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to fetch exchange rate: {e}")
        return None

def convert_currency():
    try:
        amount = float(amount_entry.get())
        base_currency = base_currency_entry.get().upper()
        target_currency = target_currency_entry.get().upper()

        rate = get_exchange_rate(base_currency, target_currency)
        if rate:
            converted_amount = amount * rate
            result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        else:
            messagebox.showerror("ERROR", "Invalid currency code or unable to fetch exchange rate")
    except ValueError:
        messagebox.showerror("ERROR", "Please enter a valid number for amount")

# GUI Setup
root = tk.Tk()
root.title("Currency Converter")

# Labels and input fields
tk.Label(root, text="Amount:").grid(row=0, column=0)
amount_entry = tk.Entry(root)
amount_entry.grid(row=0, column=1)

tk.Label(root, text="From (Currency Code):").grid(row=1, column=0)
base_currency_entry = tk.Entry(root)
base_currency_entry.grid(row=1, column=1)

tk.Label(root, text="To (Currency Code):").grid(row=2, column=0)
target_currency_entry = tk.Entry(root)
target_currency_entry.grid(row=2, column=1)

# Convert button
convert_button = tk.Button(root, text="Convert", command=convert_currency)
convert_button.grid(row=3, column=0, columnspan=2)

# Result label
result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

# Run application
root.mainloop()
