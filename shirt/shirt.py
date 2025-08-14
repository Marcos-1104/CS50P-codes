from PIL import Image, ImageOps
import sys
import os
from pathlib import Path

def main():

    if len(sys.argv)> 3:
        sys.exit("Too many command-line arguments")
    if len(sys.argv)<3:
        sys.exit("Too few command-line arguments")

    first_input = sys.argv[1].lower()
    second_input = sys.argv[2].lower()

    try:

        path_1, extension_1 = os.path.splitext(first_input)
        path_2, extension_2 = os.path.splitext(second_input)

        format = ['.jpeg', '.jpg', '.png']

        if extension_1 not in format:
            sys.exit("Invalid output")

        if extension_2 not in format:
            sys.exit("Invalid output")

        if not extension_1 == extension_2:
            sys.exit("Input and output have different extensions")


        with Image.open(first_input) as img:

            shirt = Image.open("shirt.png")
            size = shirt.size
            img = ImageOps.fit(img,size)
            img.paste(shirt,shirt)
            img.save(second_input)


    except IndexError:
        sys.exit("Invalid Input")
    except FileNotFoundError:
        sys.exit("Input does not exist")

if __name__ == "__main__":
    main()
