def main():

    meals_between = input("What time is it?\n").strip()
    if 7.0 <= convert(meals_between) <= 8.0:
        print("breakfast time")
    elif 12.0 <= convert(meals_between) <= 13.0:
        print("lunch time")
    elif 18.0 <= convert(meals_between) <= 19.0:
        print("dinner time")

def convert(time):
    hours, minutes = map(float, time.split(":"))
    time = hours + minutes/60
    return time


if __name__ == "__main__":
    main()
