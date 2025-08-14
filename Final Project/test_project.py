from project import menu, emojis,handle_order, handle_emoji,calculate_total,Order
import emoji

def test_handle_order():
    assert handle_order("Cake", menu) == True
    assert handle_order("ice cream", menu) == False
    assert handle_order("cake", menu) == True
    assert handle_order("caesar Salad", menu) == False


def test_handle_emoji():
    assert handle_emoji("Pizza", emojis) == emoji.emojize(":pizza:")
    assert handle_emoji("Hamburger", emojis) == emoji.emojize(":hamburger:")
    assert handle_emoji("French Fries", emojis) == emoji.emojize(":french_fries:")
    assert handle_emoji("Soda", emojis) == emoji.emojize(":cup_with_straw:")
    assert handle_emoji("Ice Cream", emojis) == emoji.emojize(":ice_cream:")
    assert handle_emoji("Caesar Salad", emojis) == emoji.emojize(":green_salad:")
    assert handle_emoji("Cake", emojis) == None



def test_calculate_total():

    order = Order(menu,emojis)
    order.add_item("Soda")
    order.add_item("Soda")
    order.add_item("Soda")
    order.add_item("Pizza")
    order.add_item("Pizza")
    assert calculate_total(order.order,menu) == 35.98

    order2 = Order(menu,emojis)
    order2.add_item("")
    assert calculate_total(order2.order,menu) == 0

