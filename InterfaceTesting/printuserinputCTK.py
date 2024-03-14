from customtkinter import *

app = CTk()
app.geometry("600x600")
app.resizable(1,1)

def login_button():
    user_input = username_input.get()
    print(user_input)
    textdisplay = CTkLabel(master=frame,text=user_input+",\nhello!", width=250, height=100, fg_color="#EbEbEb")
    textdisplay.pack(anchor="w", pady=(25), padx=(35,20))

frame = CTkFrame(master=app, width=600, height=600, fg_color="#FFFFFF")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

username_input = CTkEntry(master=frame, width=250, fg_color="#EEEEEE", border_color="#601E88", border_width=1,
        text_color="#000000")
username_input.pack(anchor="w",pady=(25), padx=(35,20))
#login button
CTkButton(master=frame, command=login_button, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=250).pack(anchor="w", pady=(40), padx=(35,20))

app.mainloop()

