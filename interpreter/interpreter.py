def main():

    def interpreter(word):
        x, y, z = word.split()
        x = int(x.strip())
        y = y.strip()
        z = int(z.strip())

        if y == "/" and z == 0:
            print("The division cannot be posible")
        elif y == "/":
            print(round(float(x/z), 1))
        elif y == "+":
            print(round(float(x+z), 1))
        elif y == "-":
            print(round(float(x-z), 1))
        else:
            print(round(float(x*z), 1))

    expression = input("Write a numerical expression: ex.(1 + 1)\n")
    interpreter(expression)


main()
