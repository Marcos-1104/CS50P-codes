import datetime
from datetime import date
import inflect
import sys

class Person:
    def __init__(self,birthdate):
       self.birthdate = birthdate

    @classmethod
    def handle_date(cls,s):

        try:
            year, month, day = s.strip().split("-")
            year, month, day = map(int,[year, month, day])
            date = datetime.date(year, month, day)
        except ValueError:
            sys.exit("Invalid date")
        except IndexError:
            sys.exit("Invalid date")
        return cls(date)


    def age_in_minutes(self, today=None):
            if today is None:
                today = date.today()
            days_of_birth = today - self.birthdate
            return round(days_of_birth.days*24*60)


def main():

    person = Person.handle_date(input("Date of Birth: "))
    p = inflect.engine()
    print(f"{p.number_to_words(person.age_in_minutes()).replace(" and", '').capitalize()} minutes" )

if __name__ == "__main__":
    main()
