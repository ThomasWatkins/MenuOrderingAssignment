from customtkinter import *
from PIL import Image


#set app dimensions and make a un-resizeable screen
app = CTk()
app.geometry("900x800")
app.resizable(0,0)


#load Images -------------------------------------------------------------
image1 = Image.open("ResturantGUI/French_Fries.png")
image1 = CTkImage(dark_image=image1, light_image=image1, size=(200, 160))

image2 = Image.open("ResturantGUI/salad.png")
image2 = CTkImage(dark_image=image2, light_image=image2, size=(200, 160))

image3 = Image.open("ResturantGUI/Hot_dog.png")
image3 = CTkImage(dark_image=image3, light_image=image3, size=(200, 160))

image4 = Image.open("ResturantGUI/tea_cup.png")
image4 = CTkImage(dark_image=image4, light_image=image4, size=(200,160))

image5 = Image.open("ResturantGUI/lemonade.png")
image5 = CTkImage(dark_image=image5, light_image=image5, size=(200,160))

#Fonts -------------------------------------------------------------------
HeaderFont = CTkFont("Segoe UI Black", 38)
buttonFont = CTkFont("Segoe UI Black", 24)
textFont = CTkFont("Poppins", 18)
orderFont = CTkFont("Poppins", 12)


#functions----------------------------------------------------------------
order = []

def view_order_history():
    print("order history button pressed")
    print(order)

# Function to add an item to the order
def add_to_order(item_data):
    order.append(item_data)
    update_order_display()
    update_total_price_display()

# Function to remove an item from the order
def remove_from_order(item_data):
    if item_data in order:
        order.remove(item_data)
        update_order_display()
        update_total_price_display()

# Function to create a string representation of the order
def create_order_string():
    order_string = ""
    for item in order:
        order_string += f"{item['title']} - ({item['price']})\n"
    print(order_string)
    return order_string

# Function to calculate the total price of the order
def calculate_total_price():
    total_price = 0
    for item in order:
        total_price += int(item['price'][1:])  # Extracting the price without the "$" sign and summing it up
    return total_price

# Function to update the GUI with the current order
def update_order_display():
    order_text = create_order_string()
    order_display.configure(text=order_text)
# Function to update the GUI with the current total price
def update_total_price_display():
    total_price = calculate_total_price()
    order_total.configure(text="TOTAL: $" + str(total_price)) 
     # Convert total price to string "TOTAL: $"

def complete_order():
    global app, complete_order_window
    app.withdraw()
    print(update_total_price_display())
    complete_order_window = CTkToplevel(app)
    complete_order_window.geometry("600x800")
    #header -----
    order_header = CTkFrame(complete_order_window, fg_color="#437B90", width=800,height=100, corner_radius=0)
    order_header.place(x=0,y=0)
    order_header_text = CTkLabel(master=order_header, text="Newcastle Diner Co.", font=HeaderFont)
    order_header_text.place(x=25 ,y=25)
    go_back_button = CTkButton(master=order_header, text="Go Back", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                 hover_color="#2E6E87", corner_radius=5, command=reopen_main_window)
    go_back_button.place(x=430,y=30)
    #main frame ----
    order_window_main = CTkFrame(complete_order_window, fg_color="#A9CEDE", width=800, height=700, corner_radius=0)
    order_window_main.place(x=0,y=100)
    #payment details frame ------
    payment_details_frame = CTkFrame(order_window_main, fg_color="#DEEDF2",width=550, height=630, corner_radius=25)
    payment_details_frame.place(x=25,y=25)
    order_summary_text = CTkLabel(payment_details_frame, text="ORDER SUMMARY", font=buttonFont, text_color="#183540")
    order_summary_text.place(x=10,y=40)
    order_summary_window = CTkScrollableFrame(master=payment_details_frame,width=215,corner_radius=25, fg_color="#DEEDF2",scrollbar_fg_color="#DEEDF2", scrollbar_button_color="#183540")
    order_summary_window.place(x=10,y=80)
    order_summary = CTkLabel(master=order_summary_window,text=create_order_string(), font=orderFont, text_color="#0C0705")
    order_summary.grid(row=1)



    complete_order_window.protocol("WM_DELETE_WINDOW", reopen_main_window)

def reopen_main_window():
    global app, complete_order_window
    app.deiconify()  # Reopen the main window
    complete_order_window.destroy()  # Close the second window

#GUI Begin ---------------------------------------------------------------------------

#Header Frame ----------------------------------------

header = CTkFrame(app, fg_color="#437B90",width=900, height=100, corner_radius=0)
header.place(x=0,y=0)

header_text = CTkLabel(master=header, text="Newcastle Diner Co.", font=HeaderFont, text_color="#E6EAEE")
order_history_button = CTkButton(master=header, text="View Order History", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                 hover_color="#2E6E87", corner_radius=5, command=view_order_history)
header_text.place(relx=0.01,rely=0.3)
order_history_button.place(relx=0.7, rely=0.4)

#main frame-----------------------------------------------------
Main_menu = CTkFrame(app, fg_color="#A9CEDE", width=900, height=700, corner_radius=0)
Main_menu.place(x=0,y=100)

#menu items frame-----------------------------------------------------
menu_items = CTkScrollableFrame(master=Main_menu,fg_color="#DEEDF2",scrollbar_button_color="#183540", width=470, height=530, corner_radius=25)
menu_items.place(x=45,y=70)

#total frame-----------------------------------------------------
order_summary = CTkFrame(Main_menu, fg_color="#DEEDF2", bg_color="transparent", width=300, height=400, corner_radius=25)
order_summary.place(x=580, y=70)

current_order = CTkLabel(order_summary, text="CURRENT ORDER", font=buttonFont, text_color="#183540")
current_order.place(x=25,y=10)

order_window = CTkScrollableFrame(master=order_summary,width=215,corner_radius=25, fg_color="#DEEDF2",scrollbar_fg_color="#DEEDF2", scrollbar_button_color="#183540")
order_window.place(x=25,y=40)

order_display = CTkLabel(master=order_window, font=orderFont, text_color="#0C0705")
order_display.grid(row=1)

order_total = CTkLabel(master=order_summary, text="TOTAL: $0", font=HeaderFont, text_color="#183540")
order_total.place(x=25, y=300)

order_button = CTkButton(master=order_summary, text="COMPLETE ORDER", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                 hover_color="#2E6E87", corner_radius=5, command=complete_order)
order_button.place(x=25,y=350)

# Define item data individually-----------------------------------------------------
item1_data = {"title": "French Fries", "description": "Extra hot sauce with chicken", "price": "$15"}
item2_data = {"title": "Salad", "description": "Pasta and tomato combo", "price": "$18"}
item3_data = {"title": "Hot Dogs", "description": "Perfect Dog with Sauce", "price": "$15"}
item4_data = {"title": "Tea", "description": "A very nice drink", "price": "$10"}
item5_data = {"title": "Lemonade", "description": "Classic fresh lemonade", "price": "$6"}

# Define item images individually
item1_image = image1
item2_image = image2
item3_image = image3
item4_image = image4
item5_image = image5

# Create menu images list
menu_images = []

# Create item 1
item1_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
item1_title = CTkLabel(master=item1_frame, text=item1_data["title"], font=buttonFont, text_color="#0C0705")
item1_description = CTkLabel(master=item1_frame, text=item1_data["description"], font=textFont, text_color="#0C0705")
item1_price = CTkLabel(master=item1_frame, text=item1_data["price"], font=textFont, text_color="#0C0705")
item1_plus_button = CTkButton(master=item1_frame, text="+", width=50, height=30, command=lambda: add_to_order(item1_data))
item1_minus_button = CTkButton(master=item1_frame, text="-", width=50, height=30, command=lambda: remove_from_order(item1_data))
item1_frame.grid(row=2, column=2, pady=25, padx=10)
item1_title.place(x=10, y=10)
item1_description.place(x=10, y=50)
item1_price.place(x=10, y=80)
item1_minus_button.place(x=10, y=150)
item1_plus_button.place(x=140, y=150)
# Create menu image for item 1
menu_image1 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item1_image)
menu_image1.grid(row=2, column=1, pady=25)
menu_images.append(menu_image1)

# Create item 2
item2_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
item2_title = CTkLabel(master=item2_frame, text=item2_data["title"], font=buttonFont, text_color="#0C0705")
item2_description = CTkLabel(master=item2_frame, text=item2_data["description"], font=textFont, text_color="#0C0705")
item2_price = CTkLabel(master=item2_frame, text=item2_data["price"], font=textFont, text_color="#0C0705")
item2_plus_button = CTkButton(master=item2_frame, text="+", width=50, height=30, command=lambda: add_to_order(item2_data))
item2_minus_button = CTkButton(master=item2_frame, text="-", width=50, height=30, command=lambda: remove_from_order(item2_data))
item2_frame.grid(row=3, column=2, pady=25, padx=10)
item2_title.place(x=10, y=10)
item2_description.place(x=10, y=50)
item2_price.place(x=10, y=80)
item2_minus_button.place(x=10, y=150)
item2_plus_button.place(x=140, y=150)
# Create menu image for item 2
menu_image2 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item2_image)
menu_image2.grid(row=3, column=1, pady=25)
menu_images.append(menu_image2)

# Create item 3
item3_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
item3_title = CTkLabel(master=item3_frame, text=item3_data["title"], font=buttonFont, text_color="#0C0705")
item3_description = CTkLabel(master=item3_frame, text=item3_data["description"], font=textFont, text_color="#0C0705")
item3_price = CTkLabel(master=item3_frame, text=item3_data["price"], font=textFont, text_color="#0C0705")
item3_plus_button = CTkButton(master=item3_frame, text="+", width=50, height=30, command=lambda: add_to_order(item3_data))
item3_minus_button = CTkButton(master=item3_frame, text="-", width=50, height=30, command=lambda: remove_from_order(item3_data))
item3_frame.grid(row=4, column=2, pady=25, padx=10)
item3_title.place(x=10, y=10)
item3_description.place(x=10, y=50)
item3_price.place(x=10, y=80)
item3_minus_button.place(x=10, y=150)
item3_plus_button.place(x=140, y=150)
# Create menu image for item 3
menu_image3 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item3_image)
menu_image3.grid(row=4, column=1, pady=25)
menu_images.append(menu_image3)

# Create item 4
item4_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
item4_title = CTkLabel(master=item4_frame, text=item4_data["title"], font=buttonFont, text_color="#0C0705")
item4_description = CTkLabel(master=item4_frame, text=item4_data["description"], font=textFont, text_color="#0C0705")
item4_price = CTkLabel(master=item4_frame, text=item4_data["price"], font=textFont, text_color="#0C0705")
item4_plus_button = CTkButton(master=item4_frame, text="+", width=50, height=30, command=lambda: add_to_order(item4_data))
item4_minus_button = CTkButton(master=item4_frame, text="-", width=50, height=30, command=lambda: remove_from_order(item4_data))
item4_frame.grid(row=5, column=2, pady=25, padx=10)
item4_title.place(x=10, y=10)
item4_description.place(x=10, y=50)
item4_price.place(x=10, y=80)
item4_minus_button.place(x=10, y=150)
item4_plus_button.place(x=140, y=150)
# Create menu image for item 4
menu_image4 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item4_image)
menu_image4.grid(row=5, column=1, pady=25)
menu_images.append(menu_image4)

# Create item 5
item5_frame = CTkFrame(master=menu_items, fg_color="#DEEDF2")
item5_title = CTkLabel(master=item5_frame, text=item5_data["title"], font=buttonFont, text_color="#0C0705")
item5_description = CTkLabel(master=item5_frame, text=item5_data["description"], font=textFont, text_color="#0C0705")
item5_price = CTkLabel(master=item5_frame, text=item5_data["price"], font=textFont, text_color="#0C0705")
item5_plus_button = CTkButton(master=item5_frame, text="+", width=50, height=30, command=lambda: add_to_order(item5_data))
item5_minus_button = CTkButton(master=item5_frame, text="-", width=50, height=30, command=lambda: remove_from_order(item5_data))
item5_frame.grid(row=6, column=2, pady=25, padx=10)
item5_title.place(x=10, y=10)
item5_description.place(x=10, y=50)
item5_price.place(x=10, y=80)
item5_minus_button.place(x=10, y=150)
item5_plus_button.place(x=140, y=150)
# Create menu image for item 5
menu_image5 = CTkLabel(master=menu_items, text="", text_color="#0C0705", image=item5_image)
menu_image5.grid(row=6, column=1, pady=25)
menu_images.append(menu_image5)

update_order_display()
update_total_price_display()

app.mainloop()