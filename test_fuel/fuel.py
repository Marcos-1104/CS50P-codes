def main():

    while True:
        try:
             string = input("Fraction: ")
             percent = convert(string)
             print(convert(string))
             print(gauge(percent))
             break

        except(ValueError, ZeroDivisionError, TypeError):
            continue


def convert(fraction):

     try:
        x,y = fraction.split("/")
        x = int(x)
        y = int(y)

        if y == 0:
            raise ZeroDivisionError

        if x > y:
            raise ValueError
        else:
            percentage = round((x/y)*100)
            return percentage

     except ValueError:
        raise ValueError


def gauge(percentage):

    if percentage >= 99:
        return "F"
    if percentage <= 1:
        return "E"
    else:
        return f"{percentage}%"


if __name__ == "__main__":
    main()
