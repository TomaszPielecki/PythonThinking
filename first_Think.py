# - * - coding: utf - 8 -
# tabliczka mnozenia

cyfry = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tupla nie zmiene wartosci
for a in cyfry:
    for b in cyfry:
        """ print(a,"*",b, " = ", a * b)  # taki archaiczny zapis dla poczatkujacego"""
        print('%s x %s = %s' % (a, b, a * b))  # clean code
        # example
        print('%s x %s =%s' % (6, 5, 30))


class Osoba:
    def __init__(self, imie):
        self.imie = imie
        self.przywitajsie()

    def przywitajsie(self):
        print(f"hello all {self.imie}")

o = Osoba("Tomasz")

