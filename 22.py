import time
import pprint

data = """
1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9
"""
data = open('22.dat').read()
bricks = []


def sorted_input(v):
    a, _ = v.split('~')
    return int(a.split(',')[-1])


def sorted_list(v):
    return min(z for x, y, z in v)


for row in sorted(data.strip().split('\n'), key=sorted_input):
    brick = set()
    c1, c2 = row.split('~')
    c1, c2 = c1.split(','), c2.split(',')
    xrange = {x for x in range(int(c1[0]), int(c2[0]) + 1)}
    yrange = {y for y in range(int(c1[1]), int(c2[1]) + 1)}
    zrange = {z for z in range(int(c1[2]), int(c2[2]) + 1)}
    for z in zrange:
        for y in yrange:
            for x in xrange:
                brick.add((x, y, z))
    bricks.append(brick)
# print(bricks)


def p(b):
    pprint.pprint(sorted(b, key=sorted_list))


def collapse(bricks):
    def check(brick, prev_bricks):
        # print('checking:', brick)
        while True:
            # time.sleep(0.1)
            if min(z for (x, y, z) in brick) == 1:
                # print(' at bottom')
                return brick
            candidate = {(x, y, z - 1) for x, y, z in brick}
            # print('candidate:', candidate)
            for prev_brick in prev_bricks:
                # print('comparing:', prev_brick, prev_brick & candidate)
                if prev_brick & candidate:
                    # print('cannot fit, returning', brick)
                    return brick
                # else:
                #     print('fits')
            else:
                # print('new candidate:', candidate)
                brick = candidate

    falling_bricks = iter(bricks)
    settled_bricks = []
    while brick := next(falling_bricks, False):
        b = check(brick, settled_bricks)
        settled_bricks.insert(0, b)
    return list(reversed(settled_bricks))


bricks = collapse(bricks)
p(bricks)
print('amount of bricks:', len(bricks))


def compare(b1, b2):
    return {tuple(e) for e in b1} - {tuple(e) for e in b2}


p1 = p2 = 0
for brick in bricks:
    print('removing', brick)
    new_bricks = bricks[:]
    new_bricks.remove(brick)
    # print('investigating')
    # p(new_bricks)
    bb = collapse(new_bricks)
    # print('--')
    # p(bb)
    if v := compare(bb, new_bricks):
        print(len(v), 'bricks would fall')
        p(v)
        p2 += len(v)
    else:
        # print('unchanged, can remove')
        p1 += 1
print('part 1:', p1)
print('part 2:', p2)


# 56911 too low
# 57728 too low
# 58545?