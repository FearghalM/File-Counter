import tkinter as tk
import os
from tkinter import filedialog, messagebox

def on_button_click():
    directory = filedialog.askdirectory()
    if directory:
        file_count = count_files_in_directory(directory)
        messagebox.showinfo("File Count", f"There are {file_count} files in the selected directory.")

def count_files_in_directory(directory):
    try:
        files = [f for f in os.listdir(directory) if os.path.isfile(os.path.join(directory, f))]
        return len(files)
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")
        return 0
    
# Setup the GUI
root = tk.Tk()
root.title("File Counter")

# Create a button
button = tk.Button(root, text="Select Directory and Count Files", command=on_button_click)
button.pack(pady=20, padx=20)


# Run the application
root.mainloop()