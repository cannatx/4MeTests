import datetime
import random

from dateutil.relativedelta import relativedelta


def make_highlighted(func):
    annotations = ["-", "*", "+"]
    annotate = random.choice(annotations)

    def highlight(*args):
        print(annotate * 50)
        func(*args)
        print(annotate * 50)

    return highlight


@make_highlighted
def print_any_message(message=""):
    print(message)


print_any_message("now i undestand decorators")
print_any_message("maybe")


class Person:
    def __init__(self, **args):
        self.name = args.get("name")
        self.surname = args.get("surname")
        # self.years = args.get("years")
        self.birth_date = args.get("birth_date")
        if self.birth_date:
            self.get_old()

    def get_old(self):
        self.birth_date = datetime.datetime.strptime(self.birth_date, "%d/%m/%y")
        self.today = datetime.datetime.today()
        self.delta = relativedelta(self.today, self.birth_date)
        self.years_old = self.delta.years


nacho = Person(name="Nacho", birth_date="01/07/79")
print(nacho.years_old)
