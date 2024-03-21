import customtkinter
from PIL import Image

image1 = Image.open("ResturantGUI/French_Fries.png")
image1 = customtkinter.CTkImage(dark_image=image1, light_image=image1, size=(200, 160))

def open_second_window():
    global root, second_window
    root.withdraw()  # Hide the main window
    second_window = customtkinter.CTkToplevel(root)
    second_window.geometry("400x300")

    label = customtkinter.CTkLabel(second_window, text="Second Window")
    label.pack(padx=20, pady=20)

    # Set the callback to reopen the main window when the second window is closed
    second_window.protocol("WM_DELETE_WINDOW", reopen_main_window)

def reopen_main_window():
    global root, second_window
    root.deiconify()  # Reopen the main window
    second_window.destroy()  # Close the second window

root = customtkinter.CTk()
root.geometry("500x400")

button_1 = customtkinter.CTkButton(root,text="",image=image1, command=open_second_window, bg_color="transparent",
                                    fg_color="transparent", hover_color="#848484")
button_1.pack(side="top", padx=20, pady=20)

root.mainloop()
