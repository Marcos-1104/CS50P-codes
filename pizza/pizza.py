import sys
import csv
from tabulate import tabulate

def check_archive(type_archive):

    #checked_archive = type_archive

    if type_archive.endswith(".csv"):
        return type_archive
    else:
        sys.exit("It is no a .csv file")


def main():

    while True:
        try:
            if len(sys.argv) > 2:
                sys.exit("Too many command-line arguments")
            archive = sys.argv[1]
            table = []
            with open(check_archive(archive)) as file:
                reader = csv.DictReader(file)
                header = reader.fieldnames[:3]

                for row in reader:
                    table.append({header[0]: row[header[0]], header[1]: row[header[1]], header[2]: row[header[2]]})
                print(tabulate(table, headers = "keys", tablefmt="grid"))
            break

        except IndexError:
            if len(sys.argv) < 2:
                sys.exit("Too few command-line arguments")
        except FileNotFoundError:
                sys.exit("File does not found")

if __name__ == "__main__":
    main()
