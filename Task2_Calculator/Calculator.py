import tkinter as tk
from tkinter import messagebox
 
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        messagebox.showerror("Error", "Cannot divide by zero.")
        return None

def calculate():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter valid numbers.")
        return

    if choice.get() == 1:
        result = add(num1, num2)
    elif choice.get() == 2:
        result = subtract(num1, num2)
    elif choice.get() == 3:
        result = multiply(num1, num2)
    elif choice.get() == 4:
        result = divide(num1, num2)

    if result is not None:
        result_label.config(text=f"Result: {result}")

# Main window
window = tk.Tk()
window.title("Simple Calculator")

# GUI elements
choice = tk.IntVar()
choice.set(1)

label_num1 = tk.Label(window, text="Enter first number:")
entry_num1 = tk.Entry(window)

label_num2 = tk.Label(window, text="Enter second number:")
entry_num2 = tk.Entry(window)

operation_label = tk.Label(window, text="Choose operation:")
add_radio = tk.Radiobutton(window, text="Add", variable=choice, value=1)
subtract_radio = tk.Radiobutton(window, text="Subtract", variable=choice, value=2)
multiply_radio = tk.Radiobutton(window, text="Multiply", variable=choice, value=3)
divide_radio = tk.Radiobutton(window, text="Divide", variable=choice, value=4)

calculate_button = tk.Button(window, text="Calculate", command=calculate)
result_label = tk.Label(window, text="Result:")

# Arrange elements
label_num1.pack()
entry_num1.pack()

label_num2.pack()
entry_num2.pack()

operation_label.pack()
add_radio.pack()
subtract_radio.pack()
multiply_radio.pack()
divide_radio.pack()

calculate_button.pack()
result_label.pack()

# Start Tkinter event loop
window.mainloop()
