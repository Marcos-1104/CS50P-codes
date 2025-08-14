def main():

    m = 1
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    def manipulating_string(s):

        if '/' in s:
            month, day, year = s.split('/')
            month = int(month)
            day = int(day)
            year = int(year)
            return month, day, year
        elif ',' in s:
            s = s.replace(',', '')
            month, day, year = s.split(' ')
            day = int(day)
            year = int(year)
            return month, day, year
        else:
            return False

    while True:
        try:
            string = input("Date: ").title()
            month, day, year = manipulating_string(string)

            for m in months:
                if m == month and day <= 31:
                    month = months.index(m) + 1
                    print(f"{year}-{month:02}-{day:02}")
                    break

                if months.index(m) == month and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break

            else:
                continue
            break

        except ValueError:
            pass
        except TypeError:
            pass
        except EOFError:
            break


main()
