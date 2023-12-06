import operator
from functools import reduce

data = [
    'Time:      7  15   30',
    'Distance:  9  40  200',
]
data = [
    'Time:        41     77     70     96',
    'Distance:   249   1362   1127   1011',
]

times = data[0].split()[1:]
distances = data[1].split()[1:]


def get_wins(time, distance):
    w = 0
    prev = 0
    descending = False
    for bt in range(1, time):
        value = (time - bt) * bt
        if value > distance:
            w += 1
            if value < prev:
                descending = True
            prev = value
        if descending and value < distance:
            break
    return w


# part 1
wins = []
for time, distance in zip(times, distances):
    wins.append(get_wins(int(time), int(distance)))
print('part 1:', reduce(operator.mul, wins))

# part 2
time, distance = int(''.join(times)), int(''.join(distances))
print('part 2:', get_wins(time, distance))