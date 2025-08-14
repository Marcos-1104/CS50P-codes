def main():

    def Percentage(n1, n2):

        if n1 > n2:
            return
        else:
            percentage = int(round((n1/n2)*100))
            return percentage

    while True:
        try:
            x, y = input("Fraction: ").split("/")
            x = int(x)
            y = int(y)

            percen = Percentage(x, y)

            if percen >= 99:
                print("F")
                break
            elif percen <= 1:
                print("E")
                break
            else:
                print(f"{percen}%")
                break

        except ValueError:
            pass
        except ZeroDivisionError:
            pass
        except TypeError:
            pass


main()
