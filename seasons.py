import sys
import operator
import inflect
from datetime import date, timedelta


def main():
    birthday = get_bday()
    calculate(birthday)
    p = inflect.engine()
    num_to_words = p.number_to_words((calculate(birthday)), andword="").capitalize()
    print(f"{num_to_words} minutes")

def get_bday():
    your_birth = input("Date of Birth: ")
    if your_birth.isalpha() or your_birth.find("-") == -1:
        sys.exit("Invalid date")
    else:
        return your_birth

def calculate(a):
        a = date.fromisoformat(a)
        present = date.today()
        delta = operator.sub(present, a)
        delta = timedelta.total_seconds(delta) / 60
        delta = int(delta)
        return delta


if __name__ == "__main__":
    main()