import random


def verifying_int(number):
    try:
        int(number)
        return True
    except ValueError:
        return False


def verifying_guess(user_guess):
    user_guess = int(user_guess)
    if user_guess <= 0:
        return True
    return False

def handling_level(level)


def main():

    while True:
        try:
            level = input("Level: ")

            while (verifying_int(level) == False):
                level = input("Level: ")

            if verifying_int(level):
                level = int(level)

            right_guess = random.randint(1, level)

            while True:
                try:
                    guess = input("Guess: ")
                    guess = int(guess)

                    if verifying_guess(guess):
                        continue

                    if guess < right_guess:
                        print("Too small!")
                    elif guess > right_guess:
                        print("Too large!")
                    else:
                        print("Just right!")
                        break

                except ValueError:
                    pass

            if guess == right_guess:
                break

        except ValueError:
            pass


if __name__ == "__main__":
    main()
