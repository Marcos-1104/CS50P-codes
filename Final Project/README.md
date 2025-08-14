# Python Command-Line Cafe

## Video Demo: <https://youtu.be/AvRMWyH2uE4> 

## Description:
This project is a command-line restaurant ordering system implemented in Python. The main goal was to create an interactive and user-friendly terminal application where a user can view a menu, place an order for multiple items, and receive a final bill and a receipt. The program is designed to be robust, handling user input gracefully and providing a clean interface by clearing the screen after each action. The project uses the emoji library to make the menu and the final order summary more visually appealing.

The program starts by displaying a menu of food items, complete with prices and corresponding emojis. It then enters a loop, prompting the user to add items to their order one by one. The application is case-insensitive and validates the user's input against the available menu items. If a user types an item that is not on the menu, the program informs them of the error and prompts them again, ensuring that only valid items are added to the order. When the user is finished ordering, they can signal the end of their input (using Ctrl+D), at which point the program displays a final summary of all the items ordered, calculates the total cost, and asks the user if they would like a text file receipt.

## Design Choices and Code Structure

The project is structured into one main class, Order, and several helper functions that each handle a specific part of the program's logic. This design was chosen to separate concerns and make the code more modular and readable.

## The project.py file contains the following components:

* class Order: This class is the core of the project. I chose to use a class to manage the state of a customer's order. This is a better design than using global variables because it encapsulates all the data and related behaviors in one place.

* __init__(self, menu, emojis_list): The constructor initializes an empty dictionary, self._order, which will store the items and their quantities. The underscore indicates that this is an internal attribute.

* add_item(self, s): This instance method is responsible for adding an item to the _order dictionary. It correctly handles cases where an item is added for the first time versus when an existing item's quantity is incremented.

* get_summary(self): This method prints the final order to the console, using emojis to represent the items. It does not return any value; its only job is to display the summary.

* @property def order(self): This is a getter property that provides safe, read-only access to the internal _order dictionary. This was a key design choice, as it allows other functions (like calculate_total and print_receipt) to read the order data without being able to accidentally modify it.

## Helper Functions:

* main(): This is the main function that drives the program. It contains the main while True loop that handles user interaction, calls other functions to display the menu and process input, and manages the overall flow of the application.

* handle_order(s, menu): This function validates the user's input. It returns False for a valid order item and True for an invalid one, which is used to control the flow of the main loop.

* handle_emoji(emj, emojis): A simple utility function that takes an item name and returns its corresponding emoji string.

* show_menu(menu): This function is responsible for printing the formatted menu to the screen.

* calculate_total(dict, menu): This function takes the order dictionary and the menu dictionary to calculate the final cost of the order. It iterates through the items and correctly multiplies the quantity by the price.

* print_receipt(order_object, total_cost): If the user requests a receipt, this function is called. It uses the order_object.order property to access the order data and writes a clean, formatted receipt to a file named receipt.txt.

* clear_screen(): A small utility function that clears the terminal screen to provide a better user experience. It checks the operating system to use the correct command (cls or clear).

This structure allowed me to build the program step-by-step and will make it easier to add new features in the future.
