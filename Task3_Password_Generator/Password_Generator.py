import random
import string
import tkinter as tk
from tkinter import Label, Entry, Button
import pyperclip

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

def generate_password_and_display():
    try:
        length = int(entry_length.get())
    except ValueError:
        result_label.config(text="Please enter a valid integer.")
        return

    if length > 0:
        password = generate_password(length)
        result_label.config(text="Generated Password: " + password)
        generated_password.set(password)  # Store the password for copying
    else:
        result_label.config(text="Please enter a valid password length greater than 0.")

def copy_to_clipboard():
    password_to_copy = generated_password.get()
    if password_to_copy:
        pyperclip.copy(password_to_copy)
        result_label.config(text="Password copied to clipboard!")
    else:
        result_label.config(text="No password to copy. Generate one first.")

# Create main window
window = tk.Tk()
window.title("Password Generator")

# Create and place widgets
Label(window, text="Enter the desired length of the password:").pack(pady=10)
entry_length = Entry(window, width=10)
entry_length.pack(pady=10)

result_label = Label(window, text="")
result_label.pack(pady=10)

generate_button = Button(window, text="Generate Password", command=generate_password_and_display)
generate_button.pack(pady=10)

copy_button = Button(window, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Variable to store the generated password
generated_password = tk.StringVar()

# Run GUI loop
window.mainloop()
