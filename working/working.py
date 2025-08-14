import re
import sys


def main():
    print(convert(input("Hours: ")))

def convert(s):

    if re.search(r'(1[0-2]|[1-9])(?::([0-5][0-9]))? ([AP]M) to (1[0-2]|[1-9])(?::([0-5][0-9]))? ([AP]M)', s):
        times = re.search(r'(1[0-2]|[1-9])(?::([0-5][0-9]))? ([AP]M) to (1[0-2]|[1-9])(?::([0-5][0-9]))? ([AP]M)', s)
        return execute(times)
    else:
        raise ValueError

def execute(t):

    minutes1 = t.group(2)
    minutes2 = t.group(5)

    if minutes1 is not None and minutes2 is not None:
        a = int(minutes1)
        b = int(minutes2)

        if a > 59 or a < 0:
            raise ValueError('1')
        elif b > 59 or b < 0:
            raise ValueError('2')

        time1 = t.group(1)
        time2 = t.group(4)
        from_hour = int(time1.strip())
        to_hour = int(time2.strip())
        meridiem1 = t.group(3)
        meridiem2 = t.group(6)
        begin = handle_hours(from_hour, meridiem1)
        end = handle_hours(to_hour, meridiem2)
        return f"{begin}:{minutes1} to {end}:{minutes2}"

    elif minutes1 is not None and minutes2 is None:
        a = int(minutes1)

        if a > 59 or a < 0:
            raise ValueError

        time1 = t.group(1)
        time2 = t.group(4)
        from_hour = int(time1.strip())
        to_hour = int(time2.strip())
        meridiem1 = t.group(3)
        meridiem2 = t.group(6)
        begin = handle_hours(from_hour, meridiem1)
        end = handle_hours(to_hour, meridiem2)
        return f"{begin}:{minutes1} to {end}:00"

    elif minutes1 is None and minutes2 is not None:
        b = int(minutes2)

        if b > 59 or b < 0:
            raise ValueError

        time1 = t.group(1)
        time2 = t.group(4)
        from_hour = int(time1.strip())
        to_hour = int(time2.strip())
        meridiem1 = t.group(3)
        meridiem2 = t.group(6)
        begin = handle_hours(from_hour, meridiem1)
        end = handle_hours(to_hour, meridiem2)
        return f"{begin}:00 to {end}:{minutes2}"

    else:
        time1 = t.group(1)
        time2 = t.group(4)
        from_hour = int(time1.strip())
        to_hour = int(time2.strip())
        meridiem1 = t.group(3)
        meridiem2 = t.group(6)
        begin = handle_hours(from_hour, meridiem1)
        end = handle_hours(to_hour, meridiem2)
        return f"{begin}:00 to {end}:00"

def handle_hours(d,t):

    n = int(d)
    if t == 'PM' and n != 12:
        n =  n + 12
        return n
    elif t == 'PM' and n == 12:
        return f"{n}"
    elif t == 'AM' and n == 12:
        n = n - 12
        return f"{n:02}"
    else:
        return f"{n:02}"


if __name__ == "__main__":
    main()
