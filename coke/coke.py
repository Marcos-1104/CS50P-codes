def main():

    amount_due = 50
    while (amount_due > 0):
        print("Amount Due:", amount_due)
        cents = int(input("Insert a coin: ").strip())
        if cents != 25 and cents != 10 and cents != 5:
            print(end="")
        else:
            change_owed = abs(amount_due - cents)
            amount_due = amount_due - cents
    print("Change Owed:", change_owed)


main()
