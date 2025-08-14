import random


def main():

    l = get_level()
    i = 0
    j = 0
    c = 0
    v = 0

    while True:
        try:
            x = generate_integer(l)
            y = generate_integer(l)
            z = x + y
            k = 0

            while k < 3:
                try:
                    sum = int(input(f"{x} + {y} = "))
                    if sum == z:
                        i += 1
                        break
                    else:
                        print("EEE")
                        k += 1

                except ValueError:
                    v += 1
                    print("EEE")
                    if v == 3:
                        j += 1
                        print(f"{x} + {y} = {z}")

                        break

            if k == 3:
                print(f"{x} + {y} = {z}")
                c += 1

            if i + (c+j) == 10:
                print("Score: ", i)
                break

        except ValueError:
            print("EEE")


def get_level():

    while True:
        try:
            level = int(input("Level: "))
            if level not in [1, 2, 3]:
                raise ValueError
            else:
                return level
        except (ValueError, TypeError):
            pass


def generate_integer(level):

    if level == 1:
        random_int = random.randrange(0, 10)
    elif level == 2:
        random_int = random.randrange(10, 100)
    elif level == 3:
        random_int = random.randrange(100, 1000)
    else:
        raise ValuError
    return random_int


if __name__ == "__main__":
    main()
