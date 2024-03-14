from customtkinter import *

app = CTk()
app.geometry("600x480")
app.resizable(0,0)

def login_button():
    user_input = username_input.get()
    print(user_input)

frame = CTkFrame(master=app, width=300, height=1080, fg_color="#FFFFFF")
frame.pack_propagate(0)
frame.pack(expand=True, side="right")

username_input = CTkEntry(master=frame, width=225, fg_color="#EEEEEE", border_color="#601E88", border_width=1, 
        text_color="#000000")
username_input.pack(anchor="w", padx=(25, 0))
#login button
CTkButton(master=frame, command=login_button, text="Login", fg_color="#601E88", hover_color="#E44982", font=("Arial Bold", 12),
          text_color="#ffffff", width=225).pack(anchor="w", pady=(40, 0), padx=(25, 0))

app.mainloop()

