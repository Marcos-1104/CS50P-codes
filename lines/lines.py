import sys
import csv

def main():

    while True:
        try:
            file = sys.argv[1]

            if len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            if file.endswith(".py"):
                new_file = file

                with open(new_file, "r") as python_file:
                    lines = python_file.readlines()
                    no_line = 0
                    number = 0


                    for line in lines:
                        if line.lstrip().startswith("#") or line.isspace():
                            no_line = no_line + 1
                        else:
                            number = number + 1

                    print(number)
                    break

            else:
                sys.exit("Not a pyhton file")

        except IndexError:
            sys.exit("Too few command-line arguments")
        except FileNotFoundError:
            sys.exit("File does not found")

if __name__ == "__main__":
    main()
