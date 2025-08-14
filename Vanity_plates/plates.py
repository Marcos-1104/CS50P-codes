def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    valid = False
    # invalid = False
    # counter = 1
    string = len(s)

    for c in s:
        if c in ',. :;':
            return False

    if 2 <= string <= 6:
        valid = True
    else:
        return False

    for c in s[0:2]:
        if c not in '0123456789':
            valid = True
        else:
            return False

    number = []

    for c in s:
        if c in '0123456789':
            number.append(c)

    if number:
        if number[0] == "0":
            valid = False
        if s[-1] not in '0123456789' or s[-2] not in '0123456789':
            valid = False

    if valid == True:
        return True
    else:
        return False


main()
