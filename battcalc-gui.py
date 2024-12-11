#!/usr/bin/env python3

try:
    import tkinter as tk
except ImportError:
    print("Python-Tk is not installed. Please install it using your package manager (e.g., 'pip install tk') or system package manager (e.g., 'sudo apt install python3-tk')")
    exit(1)

def calculate():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        num3 = float(entry3.get())
        result = (100 - num1) * num2 / num3 / 100
        result_label.config(text="Total Time in Hours: " + str(result))
    except ValueError:
        result_label.config(text="Invalid input. Please enter numbers only.")

def close_window():
    window.destroy()

# Create the main window
window = tk.Tk()
window.title("Gobytego Battery Charge Time Calculator")
window.geometry("444x145")

# Configure grid layout
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=1)
window.rowconfigure(2, weight=1)
window.rowconfigure(3, weight=1)
window.rowconfigure(4, weight=1)

# Create labels and entry fields
label1 = tk.Label(window, text="Enter the Remaining Battery %:")
label1.grid(row=0, column=0, sticky="e")
entry1 = tk.Entry(window)
entry1.grid(row=0, column=1)

label2 = tk.Label(window, text="Enter the Battery Capacity (Ah):")
label2.grid(row=1, column=0, sticky="e")
entry2 = tk.Entry(window)
entry2.grid(row=1, column=1)

label3 = tk.Label(window, text="Enter the Charge Rate in Amps:")
label3.grid(row=2, column=0, sticky="e")
entry3 = tk.Entry(window)
entry3.grid(row=2, column=1)

# Create a frame for the buttons
button_frame = tk.Frame(window)
button_frame.grid(row=3, columnspan=2)

# Create and pack the buttons
calculate_button = tk.Button(button_frame, text="Calculate", command=calculate)
calculate_button.pack(side=tk.LEFT)
close_button = tk.Button(button_frame, text="Close", command=close_window)
close_button.pack(side=tk.LEFT)

# Create a label to display the result
result_label = tk.Label(window, text="Total Time in Hours: ")
result_label.grid(row=4, columnspan=2)

window.mainloop()
