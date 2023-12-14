from bisect import insort

data = """
O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....
"""
data = open('14.dat').read()
d = []
for row in data.split('\n'):
    if not row:
        continue
    d.append([c for c in row])
data = d
ymax = len(data)
xmax = len(data[0])


def tilt_vertical(data, yrange, get_free):
    for x in range(xmax):
        free = []
        for y in yrange:
            c = data[y][x]
            if c == '#':
                free = []
            elif c == 'O' and free:
                pos, free = get_free(free)
                data[pos][x] = 'O'
                data[y][x] = '.'
                insort(free, y)
            elif c == '.':
                insort(free, y)
    return data


def tilt_horizontal(data, xrange, get_free):
    for y in range(ymax):
        free = []
        for x in xrange:
            c = data[y][x]
            if c == '#':
                free = []
            elif c == 'O' and free:
                pos, free = get_free(free)
                data[y][pos] = 'O'
                data[y][x] = '.'
                insort(free, x)
            elif c == '.':
                insort(free, x)
    return data


def tilt_north(data):
    return tilt_vertical(data, range(ymax), lambda free: (free[0], free[1:]))


def tilt_south(data):
    return tilt_vertical(data, range(ymax - 1, -1, -1), lambda free: (free[-1], free[:-1]))


def tilt_west(data):
    return tilt_horizontal(data, range(xmax), lambda free: (free[0], free[1:]))


def tilt_east(data):
    return tilt_horizontal(data, range(xmax - 1, -1, -1), lambda free: (free[-1], free[:-1]))


def serialize(data):
    return tuple(tuple(row) for row in data)


def spin(data, part_1=True):
    if part_1:
        return calc(tilt_north(data))
    else:
        cache = {}
        loads = []
        orig_data = None
        n = 0
        for n in range(1_000_000_000):
            orig_data = serialize(data)
            if orig_data in cache:
                break
            data = tilt_north(data)
            data = tilt_west(data)
            data = tilt_south(data)
            data = tilt_east(data)
            loads.append(calc(data))
            cache[orig_data] = n
        cycle = n - cache[orig_data]
        ix = cache[orig_data] + (1_000_000_000 - cache[orig_data]) % cycle
        return loads[ix - 1]


def calc(data):
    return sum(i * row.count('O') for i, row in enumerate(reversed(data), start=1))


print('part 1:', spin(data[:]))
print('part 2:', spin(data[:], part_1=False))