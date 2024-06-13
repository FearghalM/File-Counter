import tkinter as tk

# Setup the GUI
root = tk.Tk()
root.title("File Counter")

# Create a button
button = tk.Button(root, text="Select Directory and Count Files")
button.pack(pady=20, padx=20)


# Run the application
root.mainloop()