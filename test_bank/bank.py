def main():

    greetings = input("Greeting:\n")

    if value(greetings) == 0:
        print("$0")
    if value(greetings) == 20:
        print("$20")
    if value(greetings) == 100:
        print("$100")


def value(greeting):

    greeting = greeting.strip().lower()

    if greeting[:5] == "hello":
        return 0
    if greeting[:1] == "h":
        return 20
    else:
        return 100

if __name__ == "__main__":
    main()
