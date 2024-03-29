from customtkinter import *
from PIL import Image
import json
import os

current_error_label = None
order = []
payment_details = []
total_price = 0
app = CTk()
app.geometry("900x800")
app.resizable(0,0)

#load Images ----------------------------------------------------------------------------------------------------
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

#Fonts --------------------------------------------------------------------------------------------------------

HeaderFont = CTkFont("Segoe UI Black", 38)
buttonFont = CTkFont("Segoe UI Black", 24)
textFont = CTkFont("Poppins", 18)
orderFont = CTkFont("Poppins", 12)
errorFont = CTkFont("")

#Functions ----------------------------------------------------------------------------------------------------

#create the main menu ordering window
def create_main_window():

    global order_total
    header = CTkFrame(app, fg_color="#437B90",width=900, height=100, corner_radius=0)
    header.place(x=0,y=0)

    header_text = CTkLabel(master=header, text="Newcastle Diner Co.", font=HeaderFont, text_color="#E6EAEE")
    order_history_button = CTkButton(master=header, text="View Order History", font=buttonFont, bg_color="transparent",fg_color="#183540",
                                    hover_color="#2E6E87", corner_radius=5, command=order_history_window)
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
    global order_display
    order_display = CTkLabel(master=order_window, font=orderFont, text_color="#0C0705")
    order_display.grid(row=1)

    order_total = CTkLabel(master=order_summary, text="TOTAL: $0", font=HeaderFont, text_color="#183540")
    order_total.place(x=25, y=300)

    order_button = CTkButton(master=order_summary, text="COMPLETE ORDER", font=buttonFont, bg_color="transparent", fg_color="#183540",
                         hover_color="#2E6E87", corner_radius=5, command=lambda: complete_order(order_summary))
    order_button.place(x=25, y=350)

    # Define item data individually-----------------------------------------------------
    item1_data = {"title": "French Fries", "description": "crispy chips", "price": "$7"}
    item2_data = {"title": "Salad", "description": "Lettuce and tomato", "price": "$10"}
    item3_data = {"title": "Hot Dogs", "description": "crispy bun", "price": "$6"}
    item4_data = {"title": "Tea", "description": "Nice warm drink", "price": "$5"}
    item5_data = {"title": "Lemonade", "description": "Fresh lemonade", "price": "$4"}

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
    item1_plus_button = CTkButton(master=item1_frame, text="+",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: add_to_order(item1_data))
    item1_minus_button = CTkButton(master=item1_frame, text="-",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: remove_from_order(item1_data))
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
    item2_plus_button = CTkButton(master=item2_frame, text="+",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: add_to_order(item2_data))
    item2_minus_button = CTkButton(master=item2_frame, text="-",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: remove_from_order(item2_data))
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
    item3_plus_button = CTkButton(master=item3_frame, text="+",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: add_to_order(item3_data))
    item3_minus_button = CTkButton(master=item3_frame, text="-", fg_color="#437B90", hover_color="#2E6E87",width=50, height=30, command=lambda: remove_from_order(item3_data))
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
    item4_plus_button = CTkButton(master=item4_frame, text="+",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: add_to_order(item4_data))
    item4_minus_button = CTkButton(master=item4_frame, text="-",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: remove_from_order(item4_data))
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
    item5_plus_button = CTkButton(master=item5_frame, text="+",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: add_to_order(item5_data))
    item5_minus_button = CTkButton(master=item5_frame, text="-",fg_color="#437B90", hover_color="#2E6E87", width=50, height=30, command=lambda: remove_from_order(item5_data))
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

#check valid entry details before confirming order
def check_valid_order(name, address, cardNumber, expiry, cvc, totalCost, orderDetails):
    # Check if any parameter is missing or empty
    if not all([name, address, cardNumber, expiry, cvc]):
        display_invalid_details("Missing or empty parameter(s)")
        return False

    # Remove spaces from cardNumber
    cardNumber = cardNumber.replace(" ", "")

    if not isinstance(cardNumber, str) or len(cardNumber) != 16 or not cardNumber.isdigit():
        display_invalid_details("Invalid card number")
        return False
    
    if not isinstance(expiry, str) or expiry[2]!="/" or len(expiry) != 5 or "/" not in expiry:
        display_invalid_details("Invalid expiry date format")
        return False
    
    if not isinstance(cvc, str) or len(cvc) != 3 or not cvc.isdigit():
        display_invalid_details("Invalid CVC")
        return False

    # Assuming totalCost is a numeric value, you can add more specific checks if needed
    if not isinstance(totalCost, (int, float)):
        display_invalid_details("Invalid total cost")
        return False
    
    # Check if totalCost is zero, indicating no items were selected
    if totalCost == 0:
        display_invalid_details("No items selected")
        return False
    
    # If all checks pass, call confirm_order
    return True, confirm_order(name, address, cardNumber, expiry, cvc, totalCost, orderDetails),confirmation_window()

#confirm order storing all parsed data into a JSON file
def confirm_order(name, address, cardNumber, expiry, cvc, totalCost, orderDetails):
    global order
    file_path = 'ResturantGUI/OrderDetails.json'
    
    if os.path.exists(file_path) and os.path.getsize(file_path) > 0:
        with open(file_path, 'r') as file:
            data = json.load(file)
    else:
        data = []
    
    data.append({
        "name": name,
        "address": address,
        "cardNumber": cardNumber,
        "expiry": expiry,
        "cvc": cvc,
        "totalCost": totalCost,
        "orderDetails": orderDetails
    })
    
    with open(file_path, 'w') as file:
        json.dump(data, file, indent=4)
        
    print(f"Order for {name} has been added to {file_path}.")
    order = []
    update_order_display()
    update_total_price()
    update_total_price_display()

#takes all orders from JSON file and converts to a string to display in order history
def format_orders_to_string(file_path):
    try:
        with open(file_path, 'r') as file:
            orders = json.load(file)
            
        order_strings = []
        for order in orders:
            order_string = f"""\nOrder for: {order["name"]}
Address: {order["address"]}
Card Number: {order["cardNumber"]}
Expiry Date: {order["expiry"]}
CVC: {order["cvc"]}
Total Cost: ${order["totalCost"]}
Order Details:\n{order["orderDetails"]}
"""
            order_strings.append(order_string)
        
        # Join the individual order strings with a "-------" separator
        formatted_string = "------------------\n".join(order_strings)
        return formatted_string
    except FileNotFoundError:
        return "File not found."
    except json.decoder.JSONDecodeError:
        return "No previous orders found."
    except Exception as e:
        return f"An error occurred: {e}"

#Create a string representation of the current order to display
def create_order_string():
    order_string = ""
    for item in order:
        order_string += f"{item['title']} - ({item['price']})\n"
    return order_string

#Calculate the total price of the order
def calculate_total_price():
    total_price = 0
    for item in order:
        total_price += int(item['price'][1:])  # Extracting the price without the "$" sign and summing it up
    return total_price

#Update the GUI with the current order whenever an item is added
def update_order_display():
    order_text = create_order_string()
    order_display.configure(text=order_text)

#Update the total price whenever an item is added or removed from the order
def update_total_price():
    global total_price
    total_price = calculate_total_price()
    order_total.configure(text=f"TOTAL: ${total_price}")

#Add an item to the order, calling GUI updates after adding
def add_to_order(item_data):
    order.append(item_data)
    update_order_display()
    update_total_price_display()

#Remove an item from the order, calling GUI updates after adding
def remove_from_order(item_data):
    if item_data in order:
        order.remove(item_data)
        update_order_display()
        update_total_price_display()

#Update the GUI with the current total price
def update_total_price_display():
    update_total_price()

#Create and display the complete order screen, parsing the order summary to display
def complete_order(order_summary):
    global app, complete_order_window, payment_details_frame
    app.withdraw()
    complete_order_window = CTkToplevel(app)
    complete_order_window.geometry("600x800")
    complete_order_window.resizable(0,0)
    
    #header -----
    order_header = CTkFrame(complete_order_window, fg_color="#437B90", width=800, height=100, corner_radius=0)
    order_header.place(x=0, y=0)
    order_header_text = CTkLabel(master=order_header, text="Newcastle Diner Co.", font=HeaderFont, text_color="#E6EAEE")
    order_header_text.place(x=25, y=25)
    go_back_button = CTkButton(master=order_header, text="Go Back", font=buttonFont, bg_color="transparent", fg_color="#183540",
                               hover_color="#2E6E87", corner_radius=5, command=lambda: reopen_main_window(complete_order_window))
    go_back_button.place(x=430, y=30)
    
    #main frame ----
    order_window_main = CTkFrame(complete_order_window, fg_color="#A9CEDE", width=800, height=700, corner_radius=0)
    order_window_main.place(x=0, y=100)
    
    #payment details frame ------
    payment_details_frame = CTkFrame(order_window_main, fg_color="#DEEDF2", width=550, height=630, corner_radius=25)
    payment_details_frame.place(x=25, y=25)
    
    order_summary_text = CTkLabel(payment_details_frame, text="ORDER SUMMARY", font=buttonFont, text_color="#183540")
    order_summary_text.place(x=10, y=40)
    
    order_summary_window = CTkScrollableFrame(master=payment_details_frame, width=215, corner_radius=25, fg_color="#DEEDF2", scrollbar_fg_color="#DEEDF2", scrollbar_button_color="#183540")
    order_summary_window.place(x=10, y=80)
    
    order_summary = CTkLabel(master=order_summary_window, text=create_order_string(), font=orderFont, text_color="#0C0705")
    order_summary.grid(row=1)
    
    update_total_price()  
    order_total = CTkLabel(master=payment_details_frame, text=f"TOTAL: ${total_price}", font=HeaderFont, text_color="#183540")
    order_total.place(x=25, y=300)

    name_input_label = CTkLabel(master=payment_details_frame, text="Name", font=buttonFont,text_color="#183540")
    name_input_label.place(x=315,y=30)
    name_input = CTkEntry(master=payment_details_frame, placeholder_text="Full Name", fg_color="#A9CEDE",text_color="#183540")
    name_input.place(x=315,y=70)

    delivery_adress_label = CTkLabel(master=payment_details_frame, text="Delivery Adress",text_color="#183540", font=buttonFont)
    delivery_adress_label.place(x=315,y=100)
    delivery_adress_input = CTkEntry(master=payment_details_frame, placeholder_text="Delivery Adress", width=220,fg_color="#A9CEDE",text_color="#183540" )
    delivery_adress_input.place(x=315,y=140)

    card_details_label = CTkLabel(master=payment_details_frame, text="Card Number",text_color="#183540", font=buttonFont)
    card_details_label.place(x=315,y=170)
    card_details_input = CTkEntry(master=payment_details_frame, placeholder_text="1234 1234 1234 1234", width=220,fg_color="#A9CEDE",text_color="#183540")
    card_details_input.place(x=315,y=210)

    expiry_date_label = CTkLabel(master=payment_details_frame,text="Expiry Date",text_color="#183540", font=buttonFont)
    expiry_date_label.place(x=315, y=240)
    expiry_date_input = CTkEntry(master=payment_details_frame, placeholder_text="12/34",fg_color="#A9CEDE", width=80,text_color="#183540")
    expiry_date_input.place(x=315,y=280)

    cvc_label = CTkLabel(master=payment_details_frame,text="CVC",text_color="#183540", font=buttonFont )
    cvc_label.place(x=315,y=310)
    cvc_input = CTkEntry(master=payment_details_frame, width=80,fg_color="#A9CEDE",placeholder_text="123",text_color="#183540")
    cvc_input.place(x=315,y=340)

    confirm_button = CTkButton(master=payment_details_frame, text="Confirm Order",font=buttonFont, bg_color="transparent", fg_color="#183540",
                                hover_color="#2E6E87", corner_radius=5,
                                command=lambda: check_valid_order(name_input.get(),delivery_adress_input.get(),card_details_input.get(),expiry_date_input.get(),cvc_input.get(),calculate_total_price(),create_order_string()))
    confirm_button.place(x=315,y=400)
    
    complete_order_window.protocol("WM_DELETE_WINDOW", lambda: reopen_main_window(complete_order_window))

#Create and display the order history window, displaying all the JSON data in a formatted scrollable window
def order_history_window():
    app.withdraw()
    order_history_window = CTkToplevel(app)
    order_history_window.geometry("600x800")
    order_history_window.resizable(0,0)
    #header -----
    history_header = CTkFrame(order_history_window, fg_color="#437B90", width=800, height=100, corner_radius=0)
    history_header.place(x=0, y=0)
    history_header_text = CTkLabel(master=history_header, text="Newcastle Diner Co.", font=HeaderFont, text_color="#E6EAEE")
    history_header_text.place(x=25, y=25)
    go_back_button = CTkButton(master=history_header, text="Go Back", font=buttonFont, bg_color="transparent", fg_color="#183540",
                               hover_color="#2E6E87", corner_radius=5, command=lambda: reopen_main_window(order_history_window))
    go_back_button.place(x=430, y=30)

    history_window_main = CTkFrame(order_history_window, fg_color="#A9CEDE", width=800, height=700, corner_radius=0)
    history_window_main.place(x=0, y=100)

    order_history = CTkLabel(history_window_main, text="ORDER HISTORY", font=HeaderFont, text_color="#183540")
    order_history.place(x=45,y=15)

    history_scrollable = CTkScrollableFrame(master=history_window_main,fg_color="#DEEDF2",scrollbar_button_color="#183540", width=470, height=530, corner_radius=25)
    history_scrollable.place(x=45,y=70)

    formatted_history = format_orders_to_string("ResturantGUI/OrderDetails.json")
    order_history_label = CTkLabel(master=history_scrollable,  text=formatted_history, font=textFont, text_color="#183540")
    order_history_label.pack()

    order_history_window.protocol("WM_DELETE_WINDOW", lambda: reopen_main_window(order_history_window))

def confirmation_window():
    global confirmation_window, complete_order_window
    complete_order_window.withdraw()
    app.withdraw()
    confirmation_window_instance = CTkToplevel(app)  # Renamed variable
    confirmation_window_instance.geometry("600x400")
    confirmation_window_instance.resizable(0,0)
    confirmation_header = CTkFrame(confirmation_window_instance, fg_color="#437B90", width=600, height=100, corner_radius=0)
    confirmation_header.place(x=0, y=0)
    confirmation_header_text = CTkLabel(confirmation_header, text="Newcastle Diner Co.", font=HeaderFont, text_color="#E6EAEE", bg_color="transparent", fg_color="transparent")
    confirmation_header_text.place(x=25, y=25)

    confirmation_window_main = CTkFrame(confirmation_window_instance, fg_color="#A9CEDE", width=600, height=300, corner_radius=0)
    confirmation_window_main.place(x=0, y=100)
    confirmation_message = CTkLabel(confirmation_window_main, text="Order Confirmed", font=buttonFont)
    confirmation_message.place(x=200,y=100)
    close_button = CTkButton(confirmation_window_main, text="Back to Main Menu", font=buttonFont, command=lambda: reopen_main_window(confirmation_window_instance, complete_order_window))
    close_button.place(x=200,y=200)

    confirmation_window_instance.protocol("WM_DELETE_WINDOW", lambda: reopen_main_window(confirmation_window_instance, complete_order_window))

#reopen main window after subwindow is closed, pasrsing the subwindow name as the variable to destroy
def reopen_main_window(*windows):
    global confirmation_window, order_history_window
    for window in windows:  # Iterate over each window passed to the function
        window.destroy()    # Close each window
    app.deiconify()          # Re-show the main window

def display_invalid_details(error):
    global current_error_label
    # Hide or destroy the current error label if it exists
    if current_error_label is not None:
        current_error_label.destroy()
    
    # Create a new label for the error message
    current_error_label = CTkLabel(master=payment_details_frame, text="Invalid details: " + error, text_color="#183540", font=buttonFont)
    current_error_label.place(x=10, y=450)

create_main_window()