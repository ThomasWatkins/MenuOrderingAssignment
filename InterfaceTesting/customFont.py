from customtkinter import *

app = CTk()
app.geometry("900x800")


# Create labels with the custom fonts
header = CTkFrame(app, fg_color="#437B90",width=900, height=100, corner_radius=0)
header.place(x=0,y=10)

header_text = CTkLabel(master=header, text="Newcastle Diner Co.", font=CTkFont("Lucida Calligraphy", 32))
header_text.place(relx=0.01,rely=0.3)


app.mainloop()
