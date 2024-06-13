import tkinter as tk
from tkinter import filedialog

def on_button_click():
    directory = filedialog.askdirectory()
    if directory:
        print(f"Selected directory: {directory}")


# Setup the GUI
root = tk.Tk()
root.title("File Counter")

# Create a button
button = tk.Button(root, text="Select Directory and Count Files", command=on_button_click)
button.pack(pady=20, padx=20)


# Run the application
root.mainloop()