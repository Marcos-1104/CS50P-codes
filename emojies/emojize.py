import emoji


def handling_string(string):

    str = emoji.emojize(string, language='alias')
    print("Output: ", f"{str}")


def main():

    s = input("Input: ")
    handling_string(s)


if __name__ == "__main__":
    main()
