import functools

from helpers import timer

data = r"""
.|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".strip().split('\n')
data = open('input/16.dat').read().strip().split('\n')
ymax = len(data)
xmax = len(data[0])
mirrors = {
    '\\': {'e': 's', 'w': 'n', 'n': 'w', 's': 'e'},
    '/': {'e': 'n', 'w': 's', 'n': 'e', 's': 'w'}
}


def shine(pos, direction, path, cache):
    def move():
        nonlocal pos
        y, x = pos
        if direction == 'e':
            pos = (y, x + 1)
        elif direction == 'w':
            pos = (y, x - 1)
        elif direction == 'n':
            pos = (y - 1, x)
        elif direction == 's':
            pos = (y + 1, x)

    while 0 <= pos[0] < ymax and 0 <= pos[1] < xmax:
        if (pos, direction) in cache:  # previously traversed
            yield cache[(pos, direction)]
            break
        elif (pos, direction) in path:  # loop detected
            cache[(pos, direction)] = path
            yield path
            break
        else:
            path.add((pos, direction))
            v = data[pos[0]][pos[1]]
            if v in mirrors:
                direction = mirrors[v][direction]
            elif v == '|' and direction in ('w', 'e'):
                direction = 's'
                yield from shine(pos, 'n', path, cache)
            elif v == '-' and direction in ('n', 's'):
                direction = 'w'
                yield from shine(pos, 'e', path, cache)
            move()
    yield path


def p1():
    return len({pos
                for path in shine((0, 0), 'e', set(), {})
                for pos, d in path})


@timer
def p2():
    maxtiles = 0
    cache = {}
    for y in range(ymax):
        for x, d in zip((0, xmax - 1), ('e', 'w')):
            pathlen = len({pos
                           for path in shine((y, x), d, set(), cache)
                           for pos, d in path})
            maxtiles = max(maxtiles, pathlen)
    for x in range(xmax):
        for y, d in zip((0, ymax - 1), ('s', 'n')):
            pathlen = len({pos
                           for path in shine((y, x), d, set(), cache)
                           for pos, d in path})
            maxtiles = max(maxtiles, pathlen)
    return maxtiles


print('part 1:', p1())
print('part 2:', p2())
