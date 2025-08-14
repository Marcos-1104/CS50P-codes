import inflect


def add_names(s, list=[]):
    list.append(s)
    return list


def main():

    inf = inflect.engine()
    # names_list = []

    while True:
        try:
            name = input("Name: ")
            names_list = add_names(name)
            to_print = inf.join(names_list)
        except EOFError:
            print()
            print("Adieu, adieu, to " + to_print)
            break


if __name__ == "__main__":
    main()
