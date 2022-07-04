# # - * - coding: utf - 8 -
# # tabliczka mnozenia
#
# cyfry = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # tupla nie zmiene wartosci
# for a in cyfry:
#     for b in cyfry:
#         print(a,"*",b, " = ", a * b)  # taki archaiczny zapis dla poczatkujacego"""
#         print('%s x %s = %s' % (a, b, a * b))  # clean code
#         # example
#         print('%s x %s =%s' % (6, 5, 30))
#
# class Osoba:
#     def __init__(self, imie):
#         self.imie = imie
#         self.przywitajsie()
#
#     def przywitajsie(self):
#         print(f"hello all {self.imie}")
#
# o = Osoba("Tomasz")
#
# class Robot:
#     def __init__(self, name):
#         self.name = name
#         print(f'Inicjalizacja %s' % self.name)
#
#     def __str__(self):
#         return (f'Hello my name is {self.name}')
#
#
# droid = Robot('R2d2')
# print(droid)
# droid2 = Robot('C-3PO')
# print(droid2)

# multiplication table
numbers = (0, 1, 2, 3, 4, 5, 6, 7, 8, 9)
for a in numbers:
    for b in numbers:
        print('%s x %s = %s' % (a, b, a * b))

# example
print("example")
print('%s x %s = %s' % (4, 5, 20))
