data = """
19, 13, 30 @ -2,  1, -2
18, 19, 22 @ -1, -1, -2
20, 25, 34 @ -2, -2, -4
12, 31, 28 @ -1, -2, -1
20, 19, 15 @  1, -5, -3
"""
hail = []
start = 7
stop = 27
start = 200000000000000
stop = 400000000000000
data = open('input/24.dat').read()
for row in data.strip().splitlines():
    p, v = row.split('@')
    hail.append((tuple(int(a) for a in p.split(',')), tuple(int(a) for a in v.split(','))))


def get_sign(value):
    if value < 0:
        return -1
    return 1


s = 0
for i, ((x1, y1, _), (vx1, vy1, _)) in enumerate(hail, start=1):
    (x2, y2) = (x1 + vx1, y1 + vy1)
    for (x3, y3, _), (vx3, vy3, _) in hail[i:]:
        (x4, y4) = (x3 + vx3, y3 + vy3)
        # Calculating the determinant as explained here:
        # https://en.wikipedia.org/wiki/Line%E2%80%93line_intersection
        denominator = (x1 - x2)*(y3 - y4) - (y1 - y2)*(x3 - x4)
        if not denominator:
            continue
        detx = ((x1*y2 - y1*x2)*(x3 - x4) - (x1 - x2)*(x3*y4 - y3*x4)) / denominator
        dety = ((x1*y2 - y1*x2)*(y3 - y4) - (y1 - y2)*(x3*y4 - y3*x4)) / denominator
        direction1 = get_sign(detx - x1) == get_sign(vx1)
        direction2 = get_sign(detx - x3) == get_sign(vx3)
        if direction1 and direction2 and start <= detx <= stop and start <= dety <= stop:
            s += 1
print('part 1:', s)
