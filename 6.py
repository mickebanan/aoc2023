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

# part 1
wins = []
for time, distance in zip(times, distances):
    time = int(time)
    distance = int(distance)
    w = 0
    for bt in range(1, time):
        if (time - bt) * bt > distance:
            w += 1
    wins.append(w)
print('part 1:', reduce(operator.mul, wins))

# part 2
time, distance = int(''.join(times)), int(''.join(distances))
w = 0
for bt in range(1, time):
    if (time - bt) * bt > distance:
        w += 1
print('part 2:', w)
