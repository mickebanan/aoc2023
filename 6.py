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


def search(time, distance, right=False):
    # Binary search from the left (or from the right if right=True)
    lower, upper = 0, time
    while lower < upper:
        mid = (lower + upper) // 2
        value = (time - mid) * mid
        if right:
            if value <= distance:
                upper = mid
            else:
                lower = mid + 1
        else:
            if value <= distance:
                lower = mid + 1
            else:
                upper = mid
    return lower


def get_wins(time, distance):
    # The computed distances describe a bell curve, so it's enough to just find the winning start and end points.
    # Everything in between is automatically going to win too.
    start = search(time, distance)
    end = search(time, distance, right=True)
    return end - start


# part 1
wins = []
for time, distance in zip(times, distances):
    wins.append(get_wins(int(time), int(distance)))
print('part 1:', reduce(operator.mul, wins))

# part 2
time, distance = int(''.join(times)), int(''.join(distances))
print('part 2:', get_wins(time, distance))
