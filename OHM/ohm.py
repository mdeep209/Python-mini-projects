import tkinter as tk
from tkinter import ttk, messagebox

def calculate():
    voltage = voltage_entry.get()
    current = current_entry.get()
    resistance = resistance_entry.get()
    
    try:
        if voltage and current:
            result = float(voltage) / float(current)
            resistance_entry.delete(0, tk.END)
            resistance_entry.insert(0, result)
            calculate_power()
        elif voltage and resistance:
            result = float(voltage) / float(resistance)
            current_entry.delete(0, tk.END)
            current_entry.insert(0, result)
            calculate_power()
        elif current and resistance:
            result = float(current) * float(resistance)
            voltage_entry.delete(0, tk.END)
            voltage_entry.insert(0, result)
            calculate_power()
        else:
            raise ValueError
    except ValueError:
        messagebox.showerror("Error", "Please enter at least two values")
    except ZeroDivisionError:
        messagebox.showerror("Error", "Cannot divide by zero")

def calculate_power():
    try:
        voltage = float(voltage_entry.get()) if voltage_entry.get() else 0
        current = float(current_entry.get()) if current_entry.get() else 0
        resistance = float(resistance_entry.get()) if resistance_entry.get() else 0

        if voltage and current:
            power = voltage * current
                power = voltage * current
            power = current ** 2 * resistance
        elif voltage and resistance:
            power = voltage ** 2 / resistance
        else:
            power = 0

        power_entry.config(state='normal')  # Make the entry writable
        power_entry.delete(0, tk.END)
        power_entry.insert(0, power)
        power_entry.config(state='readonly')  # Set back to readonly
    except ValueError:
        messagebox.showerror("Error", "Invalid input values")

def clear_entries():
    voltage_entry.delete(0, tk.END)
    current_entry.delete(0, tk.END)
    resistance_entry.delete(0, tk.END)
    power_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Ohm's Law Calculator")

frame = ttk.Frame(root, padding="20")
frame.grid(row=0, column=0, columnspan=3, sticky=tk.W)

ttk.Label(frame, text="Voltage (Volt):").grid(row=0, column=0)
voltage_entry = ttk.Entry(frame)
voltage_entry.grid(row=0, column=1)

ttk.Label(frame, text="Current (Amps):").grid(row=1, column=0)
current_entry = ttk.Entry(frame)
current_entry.grid(row=1, column=1)

ttk.Label(frame, text="Resistance (Ohm):").grid(row=2, column=0)
resistance_entry = ttk.Entry(frame)
resistance_entry.grid(row=2, column=1)

ttk.Label(frame, text="Power (P):").grid(row=3, column=0)
power_entry = ttk.Entry(frame, state="readonly")
power_entry.grid(row=3, column=1)

calculate_button = ttk.Button(frame, text="Calculate", command=calculate)
calculate_button.grid(row=4, column=0)

power_button = ttk.Button(frame, text="Calculate Power", command=calculate_power)
power_button.grid(row=4, column=1)

clear_button = ttk.Button(frame, text="Clear", command=clear_entries)
clear_button.grid(row=4, column=2)

root.mainloop()