from customtkinter import *
from PIL import Image


#set app dimensions and make a un-resizeable screen
app = CTk()
app.geometry("900x800")
app.resizable(0,0)

placeholder_image = Image.open("InterfaceTesting\\food_placeholder.jpg")
placeholder_image = CTkImage(dark_image=placeholder_image, light_image=placeholder_image, size=(200, 160))

def view_order_history():
    print("order history button pressed")

#header frame
header = CTkFrame(app, fg_color="#437B90",width=900, height=100, corner_radius=0)
header.place(x=0,y=0)

HeaderFont = CTkFont("Segoe UI Black", 38)
buttonFont = CTkFont("Segoe UI Black", 24)
textFont = CTkFont("Segoe UI Black", 18)

header_text = CTkLabel(master=header, text="Newcastle Diner Co.", font=HeaderFont)
order_history_button = CTkButton(master=header, text="View Order History", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                 hover_color="#2E6E87", corner_radius=5, command=view_order_history)

#main body frame
menu = CTkFrame(app, fg_color="#AAAAAA", width=900, height=700, corner_radius=0)
menu.place(x=0,y=100)

#menu items frame
menu_items = CTkScrollableFrame(master=menu,fg_color="#DEEDF2",width=470, height=500, corner_radius=25)
menu_items.place(x=45,y=100)

#total frame
order_summary = CTkFrame(menu, fg_color="#183540",bg_color="transparent", width=300, height=400, corner_radius=25)
order_summary.place(x=580,y=70)

menu_image1 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=placeholder_image)
menu_image2 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=placeholder_image)
menu_image3 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=placeholder_image)
menu_image1.grid(row=2, column=1, pady=25)
menu_image2.grid(row=3, column=1,pady=25)
menu_image3.grid(row=4, column=1,pady=25)

menu_textframe1 = CTkFrame(master=menu_items, fg_color="#AAAAAA")
menu_text1 = CTkLabel(master= menu_textframe1, text="testing", font=buttonFont, text_color="#0C0705")
menu_textframe2 = CTkFrame(master=menu_items, fg_color="#AAAAAA")
menu_textframe3 = CTkFrame(master=menu_items, fg_color="#AAAAAA")
menu_textframe1.grid(row=2, column=2, pady=25,padx=10)
menu_text1.place(x=10,y=10)
menu_textframe2.grid(row=3, column=2, pady=25,padx=10)
menu_textframe3.grid(row=4, column=2, pady=25,padx=10)

#menu_description=CTkLabel(master=menu_textframe1, text="menu description", font=textFont, fg_color="#0C0705",bg_color="transparent")
#menu_description.grid(row=2,column=1)

menu_button1 = CTkButton(master=menu_items, text="+", width=10)
menu_button2 = CTkButton(master=menu_items, text="+", width=10)
menu_button3 = CTkButton(master=menu_items, text="+", width=10)
menu_button1.grid(row=2, column=3, pady=25, padx=5)
menu_button2.grid(row=3, column=3, pady=25, padx=5)
menu_button3.grid(row=4, column=3, pady=25, padx=5)


header_text.place(relx=0.01,rely=0.3)
order_history_button.place(relx=0.7, rely=0.4)


app.mainloop()
