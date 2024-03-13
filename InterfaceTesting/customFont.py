import tkinter as tk
from tkinter import font

root = tk.Tk()

root.title("Using Custom Fonts")
root.resizable(1,0)
root.geometry("800x200")

# Load the custom fonts
custom_font = font.Font(family="MATROSKA", size=30)
custom_font2 = font.Font(family="Cerotta Personal Use Only", size=30)

# Create labels with the custom fonts
label1 = tk.Label(root, text="Hello, Custom Font!", font=custom_font)
label1.pack(padx=10, pady=10, anchor="e")

label2 = tk.Label(root, text="Hello, Another Custom Font!", font=custom_font2)
label2.pack(padx=10, pady=10, anchor="w")

root.mainloop()
