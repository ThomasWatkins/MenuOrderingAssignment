from customtkinter import *
from PIL import Image


#set app dimensions and make a un-resizeable screen
app = CTk()
app.geometry("900x800")
app.resizable(0,0)

#load Images -------------------------------------------------------------
image1 = Image.open("ResturantGUI/food_placeholder.jpg")
image1 = CTkImage(dark_image=image1, light_image=image1, size=(200, 160))

image2 = Image.open("ResturantGUI/food_placeholder2.jpg")
image2 = CTkImage(dark_image=image2, light_image=image2, size=(200, 160))

image3 = Image.open("ResturantGUI/food_placeholder3.jpg")
image3 = CTkImage(dark_image=image3, light_image=image3, size=(200, 160))

image4 = Image.open("ResturantGUI/drink.png")
image4 = CTkImage(dark_image=image4, light_image=image4, size=(200,160))
#-------------------------------------------------------------------------

#functions----------------------------------------------------------------
def view_order_history():
    print("order history button pressed")

def increase_quantity(item_index):
    print("order added", item_index)
    item_index = CTkLabel(master=order_summary, text="test", font=buttonFont, text_color="#0C0705")
    item_index.place(x=10,y=0)

def decrease_quantity(item_index):
    print("order removed", item_index)
    
    
def create_decrease_function(item_index):
    print("Decrease index is", item_index)
    def decrease():
        decrease_quantity(item_index)
    return decrease

def create_increase_function(item_index):
    print("Increase index is", item_index)
    def increase():
        increase_quantity(item_index)
    return increase

    


#header frame
header = CTkFrame(app, fg_color="#437B90",width=900, height=100, corner_radius=0)
header.place(x=0,y=0)


HeaderFont = CTkFont("Segoe UI Black", 38)
buttonFont = CTkFont("Segoe UI Black", 24)
textFont = CTkFont("Arial", 18)

header_text = CTkLabel(master=header, text="Newcastle Diner Co.", font=HeaderFont)
order_history_button = CTkButton(master=header, text="View Order History", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                 hover_color="#2E6E87", corner_radius=5, command=view_order_history)

header_text.place(relx=0.01,rely=0.3)
order_history_button.place(relx=0.7, rely=0.4)

#main frame
Main_menu = CTkFrame(app, fg_color="#A9CEDE", width=900, height=700, corner_radius=0)
Main_menu.place(x=0,y=100)

#menu items frame
menu_items = CTkScrollableFrame(master=Main_menu,fg_color="#DEEDF2", width=470, height=530, corner_radius=25)
menu_items.place(x=45,y=70)

#total frame
order_summary = CTkFrame(Main_menu, fg_color="#183540",bg_color="transparent", width=300, height=400, corner_radius=25)
order_summary.place(x=580,y=70)



items_data = [
    {"title": "Item 1", "description": "A big burrito", "price": "$105"},
    {"title": "Item 2", "description": "A big burger", "price": "$18"},
    {"title": "Item 3", "description": "small burger", "price": "$15"},
    {"title": "Item 4", "description": "drink", "price": "$10"}
]

item_images = [image1, image2, image3, image4]  # Assuming you have image1, image2, and image3

menu_images = []

for i, (item_data, item_image) in enumerate(zip(items_data, item_images), start=1):
    item_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
    item_title = CTkLabel(master=item_frame, text=item_data["title"], font=buttonFont, text_color="#0C0705")
    item_description = CTkLabel(master=item_frame, text=item_data["description"], font=textFont, text_color="#0C0705")
    item_price = CTkLabel(master=item_frame, text=item_data["price"], font=textFont, text_color="#0C0705")
    item_plus_button = CTkButton(master=item_frame, text="+", width=50, height=30, command=create_increase_function(i))
    item_minus_button = CTkButton(master=item_frame, text="-", width=50, height=30, command=create_decrease_function(i))
    item_frame.grid(row=i+1, column=2, pady=25, padx=10)
    item_title.place(x=10, y=10)
    item_description.place(x=10, y=50)
    item_price.place(x=10,y=80)
    item_minus_button.place(x=10, y=150)
    item_plus_button.place(x=140, y=150)
    
    # Create menu images with different images for each iteration
    menu_image = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item_image)
    menu_image.grid(row=i+1, column=1, pady=25)
    menu_images.append(menu_image)
    
app.mainloop()