import json
from datetime import datetime


def print_order_history():
    try:
        with open("previous tesing/order_details.json", "r") as json_file:
            orders = json.load(json_file)
            print("Order History:")
            print("==============")
            for order_details in orders:
                if 'timestamp' in order_details:
                    print(f"Order Date: {order_details['timestamp']}")
                else:
                    print("Timestamp: Not available")  # Print a message if timestamp is missing
                print(f"Email: {order_details['email']}")
                print(f"Delivery Address: {order_details['address']}")
                print("Ordered Items:")
                for item, quantity in order_details['order'].items():
                    print(f"- {item}: {quantity}")
                print(f"Total Price: ${order_details['total_price']}")
                print("--------------")
    except FileNotFoundError:
        print("No order history found.")

def append_order(order_details):
    try:
        with open("previous tesing/order_details.json", "r+") as json_file:
            # Load existing orders
            orders = json.load(json_file)
            
            # Ensure orders is a list
            if not isinstance(orders, list):
                orders = []
            
            # Append new order
            orders.append(order_details)

            # Move the file pointer to the beginning to overwrite existing content
            json_file.seek(0)
            
            # Write the updated list of orders
            json.dump(orders, json_file, indent=4)
            json_file.truncate()  # Remove remaining content if new content is smaller
    except Exception as e:
        print(f"Error occurred while appending order: {e}")

def main():
    menu = {
        "dish1": 10.99,
        "dish2": 8.50,
        "dish3": 12.75,
        # Add more dishes as needed
    }

    order = {}

    print("Welcome to the restaurant!")
    print("Here's the menu:")
    for item, price in menu.items():
        print(f"{item}: ${price}")

    while True:
        choice = input("Enter the name of the dish you'd like to order (or 'done' to finish): ").strip()
        if choice.lower() == "done":
            break

        if choice in menu:
            quantity = int(input("Enter the quantity: "))
            order[choice] = order.get(choice, 0) + quantity
        else:
            print("Invalid choice. Please choose from the menu.")

    total_price = sum(menu[item] * quantity for item, quantity in order.items())
    total_price = "{:.2f}".format(total_price)

    print(f"Your total price is: ${total_price}")

    email = input("Enter your email: ").strip()
    address = input("Enter your delivery address: ").strip()

    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    order_details = {
        "order": order,
        "total_price": total_price,
        "email": email,
        "address": address,
        "timestamp": timestamp  # Add timestamp to order details
    }
    if (email != ""):
        # Save order details to a JSON file
        append_order(order_details)

        print("Your order has been saved. Thank you for ordering!")
    else:
        history = input("print history? y/n\n")
        if history == "y":
            print_order_history()


if __name__ == "__main__":
    main()
