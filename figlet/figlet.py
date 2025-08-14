from pyfiglet import Figlet
import sys
import random


def main():

    figlet = Figlet()
    fonts_list = figlet.getFonts()

    try:
        if len(sys.argv) < 2:
            string = input("Input: ")
            figlet.setFont(font=random.choice(fonts_list))
            print("Output:")
            print(figlet.renderText(string))
        elif (sys.argv[1] == '-f' or sys.argv[1] == '--font') and sys.argv[2] in fonts_list:
            string = input("Input: ")
            figlet.setFont(font=sys.argv[2])
            print("Output:")
            print(figlet.renderText(string))
        else:
            sys.exit("Invalid usage")

    except IndexError:
        print("Too less arguments")


if __name__ == "__main__":
    main()
