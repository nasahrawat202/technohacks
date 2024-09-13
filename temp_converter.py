import tkinter as tk
from tkinter import ttk

def celsius_to_fahrenheit(celsius):
    return celsius * 9/5 + 32

def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9

def update_result():
    try:
        if var.get() == "Celsius to Fahrenheit":
            celsius = float(entry.get())
            result = celsius_to_fahrenheit(celsius)
            result_label.config(text=f"{celsius} °C = {result:.2f} °F")
        elif var.get() == "Fahrenheit to Celsius":
            fahrenheit = float(entry.get())
            result = fahrenheit_to_celsius(fahrenheit)
            result_label.config(text=f"{fahrenheit} °F = {result:.2f} °C")
    except ValueError:
        result_label.config(text="Invalid input")
root = tk.Tk()
root.title("Temperature Converter")

entry_label = ttk.Label(root, text="Enter temperature:")
entry_label.grid(column=0, row=0, padx=10, pady=10)
entry = ttk.Entry(root)
entry.grid(column=1, row=0, padx=10, pady=10)

var = tk.StringVar(value="Celsius to Fahrenheit")
conversion_options = ["Celsius to Fahrenheit", "Fahrenheit to Celsius"]
conversion_menu = ttk.Combobox(root, textvariable=var, values=conversion_options)
conversion_menu.grid(column=0, row=1, columnspan=2, padx=20, pady=10)

convert_button = ttk.Button(root, text="Convert", command=update_result)
convert_button.grid(column=0, row=2, columnspan=2, padx=10, pady=20)

result_label = ttk.Label(root, text="")
result_label.grid(column=0, row=3, columnspan=2, padx=20, pady=10)

root.mainloop()
