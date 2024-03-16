from customtkinter import *
from PIL import Image
from tkinter import font

app = CTk()
app.geometry("920x870")
app.resizable(0,0)


def login_button():
    user_input = username_input.get()
    print(user_input)

#loading image data via PIl
side_img_data = Image.open("InterfaceTesting/side-img.png")
email_icon_data = Image.open("InterfaceTesting/email-icon.png")
password_icon_data = Image.open("InterfaceTesting/password-icon.png")
google_icon_data = Image.open("InterfaceTesting/google-icon.png")

#turning PIL image data into CTkImages
side_img = CTkImage(dark_image=side_img_data, light_image=side_img_data, size=(300, 480))
email_icon = CTkImage(dark_image=email_icon_data, light_image=email_icon_data, size=(20,20))
password_icon = CTkImage(dark_image=password_icon_data, light_image=password_icon_data, size=(17,17))

#load the custom font families
custom_font = font.Font(family="MATROSKA", size=30)
custom_font2 = font.Font(family="Cerotta Personal Use Only", size=30)

#pack the left side imagze into a label
CTkLabel(master=app, text="", image=side_img).pack(expand=True, side="left")

#create a frame for the right side of the login screen
frame = CTkFrame(master=app, width=300, height=1080, fg_color="#FFFFFF")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

#welcome back label
CTkLabel(master=frame, text="Welcome Back!", text_color="#601E88", anchor="w", justify="left",
         font=("Riffic Free Medium", 25)).pack(anchor="w", pady=(20,0), padx=(30, 0))
#sign into your account label
CTkLabel(master=frame, text="Sign in to your account", text_color="#7E7E7E", anchor="w", justify="left",
         font=("Riffic Free Medium", 20)).pack(anchor=("w"), padx=(30,0))
#email label
CTkLabel(master=frame, text="  Email:", text_color="#601E88", anchor="w", justify="left",
         font=(custom_font2, 14), image=email_icon, compound="left").pack(anchor="w", pady=(38, 0), padx=(25, 0))
#email text input field
username_input = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, 
        text_color="#000000")
username_input.pack(anchor="w", padx=(25, 0))
#password label
CTkLabel(master=frame, text="  Password:", text_color="#601E88", anchor="w", justify="left",
         font=("Arial Bold", 14), image=password_icon, compound="left").pack(anchor="w", pady=(21, 0), padx=(25, 0))
#password text input field, keys hidden with *
CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
         text_color="#000000", show="*").pack(anchor="w", padx=(25, 0))
#login button
CTkButton(master=frame, command=login_button, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

CTkButton(master=frame, text="Create Account", fg_color="#EEEEEE", hover_color="#cfcfcf", font=("Arial Bold", 12),
          text_color="#601E88", width=225).pack(anchor="w", pady=(20, 0), padx=(25, 0))


app.mainloop()