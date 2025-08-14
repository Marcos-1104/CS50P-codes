import sys
import csv

def main():
    students = []

    # Validate args once, outside loop
    if len(sys.argv) < 3:
        sys.exit("Too few command-line arguments")
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")

    old_file = sys.argv[1]
    new_file = sys.argv[2]

    # Ensure .csv and that file exists
    if not old_file.endswith(".csv"):
        sys.exit(f"Could not read {old_file}")
    try:
        f_file = open(old_file, "r", newline="")
    except FileNotFoundError:
        sys.exit(f"Could not read {old_file}")

    # Read and split names
    reader = csv.DictReader(f_file)
    for row in reader:
        name = row["name"]
        last_name, first_name = [n.strip() for n in name.split(",", 1)]
        students.append({
            "first": first_name,
            "last": last_name,
            "house": row["house"]
        })
    f_file.close()

    # Write out new CSV
    with open(new_file, "w", newline="") as csv_file:
        fieldnames = ['first', 'last', 'house']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()
        for row in students:
            writer.writerow(row)

if __name__ == "__main__":
    main()


