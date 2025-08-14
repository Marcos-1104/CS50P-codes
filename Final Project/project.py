import emoji
import sys
import os

menu = {"Pizza" : 16.49, "Hamburger": 10.99,"French Fries": 2.00,"Soda": 1.00, "Ice Cream": 2.99 , "Caesar Salad": 5.99}


emojis = {
    "Pizza": ":pizza:",
    "Hamburger": ":hamburger:",
    "French Fries": ":french_fries:",
    "Soda": ":cup_with_straw:",
    "Ice Cream": ":ice_cream:",
    "Caesar Salad": ":green_salad:"
}


class Order:
    def __init__(self,menu,emojis_list):
        self._order = {}
        self.menu = menu
        self.emojis_list = emojis_list

    def add_item(self,s):
        #verify if the dict is empty
        if s in self._order:
            self._order[s] +=1
        else:
            self._order[s] = 1

    def get_summary(self):
        for i,n in self._order.items():
            if n > 0:
                print(handle_emoji(i,self.emojis_list)*self._order[i])

    @property
    def order(self):
        return self._order

def main():

    global menu
    order = Order(menu,emojis)

    while True:
        try:
            clear_screen()
            show_menu(menu)
            your_order = input("What would you like to order? ")
            if handle_order(your_order, menu):
                continue
            else:
                order.add_item(your_order.title())
                #order_list = sorted(order_list, key = lambda item: menu.index(item))
        except EOFError:
            print("\nHere is your order:")
            order.get_summary()
            cost = calculate_total(order.order, menu)
            print("Your order is: ", f"$ {cost}")
            receipt = input("Would you like your receipt: ")
            if receipt == 'yes':
                print_receipt(order,cost)
                sys.exit("Thank you for being here with us. Have a nice meal!")
            else:
                sys.exit("Thank you for being here with us. Have a nice meal!")

def handle_order(s, menu):
    if s.title() not in menu:
        print("Sorry! We don't have this item. Would you like to try another?")
        print()
        return True
    else:
        return False

def handle_emoji(emj, emojis):
    if emj in emojis:
        emj = emoji.emojize(emojis[emj], language='alias')
        return emj

def show_menu(menu):
    print("\nThis is our menu for today: ")
    for i in menu:
        emoji = handle_emoji(i,emojis)
        print(f"{i} {emoji}")
    print()

def calculate_total(dict,menu):

    total = 0
    for item,quantity in dict.items():
        if item in menu:
            total += quantity*menu[item]
    return round(total,2)

def print_receipt(order_object, total_cost):

    with open("receipt.txt", "w") as file:
        file.write("Your Order Receipt:\n")
        file.write("===================\n")

        for item,quantity in order_object.order.items():
            emoji_str = handle_emoji(item,emojis)
            file.write(f"{emoji_str * quantity}\n")

        file.write("===================\n")
        file.write(f"Total: ${total_cost:.2f}\n")

def clear_screen():
    if os.name == 'nt':
        _ = os.system('cls')
    else:
        _ = os.system('clear')


if __name__ == "__main__":
    main()
