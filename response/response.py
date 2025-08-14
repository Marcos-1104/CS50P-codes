import validators

def main():

    e_mail = input("What's your e-mail address? ")

    if not validators.email(e_mail):
        print("Invalid")
    else:
        print ("Valid")


if __name__ == "__main__":
    main()
