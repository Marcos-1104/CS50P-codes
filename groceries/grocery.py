def main():

    grocery_list = {}
    # counter = 1

    while True:
        try:
            key = input("").upper()
            value = 1
            if key in grocery_list:
                # value += 1
                grocery_list[key] = grocery_list[key] + value
            else:
                grocery_list[key] = value

        except KeyError:
            pass
        except EOFError:
            print()
            sorted_list = sorted(grocery_list.keys())
            for key in sorted_list:
                print(grocery_list[key], key, sep=" ")
            break


main()
