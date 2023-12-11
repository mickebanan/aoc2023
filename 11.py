import queue

data = [
    '...#......',
    '.......#..',
    '#.........',
    '..........',
    '......#...',
    '.#........',
    '.........#',
    '..........',
    '.......#..',
    '#...#.....',
]
with open('11.dat') as f:
    data = [row.strip() for row in f.readlines()]


def transpose(m):
    _m = []
    for i in range(len(m[0])):
        r = []
        for row in m:
            r.append(row[i])
        _m.append(''.join(r))
    return _m


def expand(data):
    empty = set()
    for y, row in enumerate(data):
        if not any(1 for c in row if c == '#'):
            empty.add(y)
    return empty


# expand
empty_ys = expand(data)
data = transpose(data)
empty_xs = expand(data)
data = transpose(data)
galaxies = set()
ymax = len(data)
xmax = len(data[0])
for y, row in enumerate(data):
    for x, col in enumerate(row):
        if col == '#':
            galaxies.add((y, x))


def get_neighbors(y, x):
    if x:
        yield y, x - 1
    if x < xmax:
        yield y, x + 1
    if y:
        yield y - 1, x
    if y < ymax:
        yield y + 1, x


def walk(pos, part_1=True):
    if part_1:
        empty_space = 1
    else:
        empty_space = 999_999
    distances = {}
    pq = queue.PriorityQueue()
    unvisited = set()
    for y in range(ymax + 1):
        for x in range(xmax + 1):
            n = (y, x)
            distances[n] = 1e8
            unvisited.add(n)
    distances[pos] = 0
    pq.put((0, pos))
    while unvisited:
        u = pq.get()[1]
        unvisited.remove(u)
        for yy, xx in get_neighbors(*u):
            if (yy, xx) in unvisited:
                diff = 1
                if yy in empty_ys:
                    diff += empty_space
                if xx in empty_xs:
                    diff += empty_space
                alt = distances[u] + diff
                if alt < distances[(yy, xx)]:
                    distances[(yy, xx)] = alt
                    pq.put((alt, (yy, xx)))
    return distances


def p1():
    shortest = 0
    for galaxy in galaxies:
        d = walk(galaxy)
        for g in galaxies:
            if g == galaxy:
                continue
            shortest += d[g]
    print('part 1:', int(shortest / 2))


def p2():
    shortest = 0
    for galaxy in galaxies:
        d = walk(galaxy, part_1=False)
        for g in galaxies:
            if g == galaxy:
                continue
            shortest += d[g]
    print('part 2:', int(shortest / 2))


p1()
p2()
