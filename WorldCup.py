'''
How does it work ?
Well, the "cs" list beneath contains the 50 best
countries (ordered by rank) on 2nd July 2022.
You can change the list if you want (but know
that the rank has an importance later).

8 groups of 6 countries are generated randomly,
no matter the rank, so that 2 countries are
rejected.

----------Groups phase----------
Only 4 countries per group are selected for the
Round of 16 (countries with higher rank have
more chances to be selected)

----------Round of 16----------
Matches are generated like so :
A1 - E3
B1 - F3
C1 - G3
D1 - H3
E1 - A3
F1 - B3
G1 - C3
H1 - D3
A2 - E4
B2 - F4
C2 - G4
D2 - H4
E2 - A4
F2 - B4
G2 - C4
H2 - D4
Countries with higher rank have more chances to
win

----------Round of 8----------
Winners play matches (same rule)

----------Quarter-finals----------
Winners play matches (same rule)

----------Semi-finals----------
Winners play matches (same rule)

----------Third-place play-off----------
Losers from Semi-finals try to get the Bronze
Medal by playing a match (same rule)

----------Final----------
Winners from Semi-finals fight for the Gold
Medal by playing a match (same rule). The loser
gets the Silver Medal
'''

# ----------Modules----------

import random as r
import math

# ----------Varible(s) & List(s)----------

cs = ['Brazil', 'Belgium', 'Argentina', 'France', 'England', 'Spain', 'Italy', 'Netherlands', 'Portugal', 'Denmark',
      'Germany', 'Mexico', 'Uruguay', 'USA', 'Croatia', 'Switzerland', 'Colombia', 'Senegal', 'Wales', 'Sweden', 'Peru',
      'Morocco', 'Iran', 'Japan', 'Serbia', 'Poland', 'Ukraine', 'South Korea', 'Chile', 'Tunisia', 'Nigeria',
      'Czechia', 'Austria', 'Costa Rica', 'Russia', 'Norway', 'Hungary', 'Cameroon', 'Australia', 'Egypt', 'Algeria',
      'Türkiye', 'Canada', 'Ecuador', 'Scotland', 'Mali', 'Ireland', 'Greece', 'Qatar', 'Paraguay']

countries = cs.copy()

gr = 'ABCDEFGH'

goals = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2,
         2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 3, 4, 4, 4, 4, 4, 4, 4, 5, 5, 5, 6, 6, 7]


# ----------Function(s)----------

def groupPhase(group):
    chance = []
    for c in group:
        for i in range((50 - cs.index(c)) ** 2):
            chance.append(c)

    r.shuffle(chance)

    index = r.randint(0, len(chance) - 1)
    first = chance[index]
    while first in chance:
        chance.remove(first)

    index = r.randint(0, len(chance) - 1)
    second = chance[index]
    while second in chance:
        chance.remove(second)

    index = r.randint(0, len(chance) - 1)
    third = chance[index]
    while third in chance:
        chance.remove(third)

    index = r.randint(0, len(chance) - 1)
    fourth = chance[index]

    return (first, second, third, fourth)


def outGroupPhase(f, s, t, f4, gr):
    # /!\ Should be used with groupPhase as argument
    print('\nGroup', gr, ':')
    print('  1.', f)
    print('  2.', s)
    print('  3.', t)
    print('  4.', f4)


def match(c1, c2):
    chance = []
    ch = (100 - (cs.index(c1) - cs.index(c2))) / 2
    if cs.index(c1) < cs.index(c2):
        ch = math.ceil(ch)
    else:
        ch = math.floor(ch)

    for i in range(ch):
        chance.append(c1)
    for i in range(100 - ch):
        chance.append(c2)

    r.shuffle(chance)

    index = r.randint(0, 99)
    winner = chance[index]

    return (c1, c2, winner)


def outMatch(mResult):
    # /!\ Should be used with match() as argument
    c1, c2, winner = mResult
    goal1 = goals[r.randint(0, len(goals) - 1)]
    goal2 = goals[r.randint(0, len(goals) - 1)]

    if goal1 > goal2:
        goalW = goal1
        goalL = goal2
    elif goal2 > goal1:
        goalW = goal2
        goalL = goal1
    else:
        goalW = goal1 + 1
        goalL = goal2

    d1 = 17 - len(c1)
    d2 = 17 - len(c2)
    if winner == c1:
        print(c1 + ' ' * d1, goalW, '-', goalL, ' ' * d2 + c2)
    else:
        print(c1 + ' ' * d1, goalL, '-', goalW, ' ' * d2 + c2)


# ----------Code----------

# Creating groups (8) : countries chosen totally
# randomly
groups = []
for i in range(8):
    # 6 countries per group
    group = []
    for ii in range(6):
        c = countries[r.randint(0, len(countries) - 1)]
        group.append(c)
        countries.remove(c)
    groups.append(group)
del group, i, ii, c
print('-------------Groups are set--------------')

for g in groups:
    print('\nGroup', gr[groups.index(g)], ':')
    for c in g:
        print('  -', c)
print('\n' + countries[0], 'and', countries[1],
      'didn\'t qualify for the cup. They decided to play a friendly match instead :\n')

outMatch(match(countries[0], countries[1]))
del g, c, countries

print('\n---------------Groups phase---------------')
print('Qualified countries to Round of 16 :')
i = 0
q16 = []
for group in groups:
    currentGr = gr[i]
    f, s, t, f4 = groupPhase(group)
    q16.append(f)
    q16.append(s)
    q16.append(t)
    q16.append(f4)
    outGroupPhase(f, s, t, f4, currentGr)
    i += 1
del i, currentGr, f, s, t, f4

print('\n---------------Round of 16---------------\n')
q8 = []
A1 = q16[0]
A2 = q16[1]
A3 = q16[2]
A4 = q16[3]
B1 = q16[4]
B2 = q16[5]
B3 = q16[6]
B4 = q16[7]
C1 = q16[8]
C2 = q16[9]
C3 = q16[10]
C4 = q16[11]
D1 = q16[12]
D2 = q16[13]
D3 = q16[14]
D4 = q16[15]
E1 = q16[16]
E2 = q16[17]
E3 = q16[18]
E4 = q16[19]
F1 = q16[20]
F2 = q16[21]
F3 = q16[22]
F4 = q16[23]
G1 = q16[24]
G2 = q16[25]
G3 = q16[26]
G4 = q16[27]
H1 = q16[28]
H2 = q16[29]
H3 = q16[30]
H4 = q16[31]
del q16

rMatch = match(A1, E3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(B1, F3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(C1, G3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(D1, H3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(E1, A3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(F1, B3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(G1, C3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(H1, D3)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(A2, E4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(B2, F4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(C2, G4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(D2, H4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(E2, A4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(F2, B4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(G2, C4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

rMatch = match(H2, D4)
outMatch(rMatch)
c1, c2, winner = rMatch
q8.append(winner)
del rMatch, c1, c2, winner

print('\n---------------Round of 8----------------\n')
q4 = []
for i in range(0, 16, 2):
    rMatch = match(q8[i], q8[i + 1])
    outMatch(rMatch)
    c1, c2, winner = rMatch
    q4.append(winner)
del i, q8, rMatch, c1, c2, winner

print('\n--------------Quarter-finals-------------\n')
semi = []
for i in range(0, 8, 2):
    rMatch = match(q4[i], q4[i + 1])
    outMatch(rMatch)
    c1, c2, winner = rMatch
    semi.append(winner)
del i, q4, rMatch, c1, c2, winner

print('\n---------------Semi-finals---------------\n')
third_placePlay_off = []
final = []
for i in range(0, 4, 2):
    rMatch = match(semi[i], semi[i + 1])
    outMatch(rMatch)
    c1, c2, winner = rMatch
    final.append(winner)
    if c1 == winner:
        third_placePlay_off.append(c2)
    else:
        third_placePlay_off.append(c1)
del i, semi, rMatch, c1, c2, winner

print('\n-----------Third-place play-off----------\n')
rMatch = match(third_placePlay_off[0], third_placePlay_off[1])
outMatch(rMatch)
c1, c2, winner = rMatch
d = math.ceil((17 - len(winner)) / 2)
print('\n' + ' ' * d + winner, 'got the Bronze Medal !')
del third_placePlay_off, rMatch, c1, c2, winner, d

print('\n------------------Final------------------\n')
rMatch = match(final[0], final[1])
outMatch(rMatch)
c1, c2, winner = rMatch
d = math.ceil((17 - len(winner)) / 2)
print('\n' + ' ' * d + winner, 'got the Gold Medal !!!')
if c1 == winner:
    loser = c2
else:
    loser = c1
d = math.ceil((16 - len(loser)) / 2)
print('\n' + ' ' * d + loser, 'got the Silver Medal !!')