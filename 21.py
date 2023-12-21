data = """
...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........
"""
garden = set()
rocks = set()
start = None
# data = open('21.dat').read()
data = data.strip().split('\n')
ymax = len(data)
xmax = len(data[0])
for y, row in enumerate(data):
    xmax = len(row)
    for x, c in enumerate(row):
        if c == '.':
            garden.add((y, x))
        elif c == '#':
            rocks.add((y, x))
        else:
            start = (y, x)
            garden.add((y, x))


def move(y, x):
    for d in ((y - 1, x), (y + 1, x), (y, x - 1), (y, x + 1)):
        if d in garden:
            yield d


positions = {start}
for i in range(40):
    new_positions = set()
    for pos in positions:
        for m in move(*pos):
            new_positions.add(m)
    positions = new_positions
print(len(positions))


def viz():
    for y in range(ymax):
        for x in range(xmax):
            if (y, x) in positions:
                print('O', end='')
            elif (y, x) == start:
                print('S', end='')
            elif (y, x) in garden:
                print('.', end='')
            elif (y, x) in rocks:
                print('#', end='')
        print()
# viz()