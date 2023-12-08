import itertools
import math
import re

import helpers

data = [
    'RL',
    '',
    'AAA = (BBB, CCC)',
    'BBB = (DDD, EEE)',
    'CCC = (ZZZ, GGG)',
    'DDD = (DDD, DDD)',
    'EEE = (EEE, EEE)',
    'GGG = (GGG, GGG)',
    'ZZZ = (ZZZ, ZZZ)',
]
data = [
    'LLR',
    '',
    'AAA = (BBB, BBB)',
    'BBB = (AAA, ZZZ)',
    'ZZZ = (ZZZ, ZZZ)',
]
data = [
    'LR',
    '',
    '11A = (11B, XXX)',
    '11B = (XXX, 11Z)',
    '11Z = (11B, XXX)',
    '22A = (22B, XXX)',
    '22B = (22C, 22C)',
    '22C = (22Z, 22Z)',
    '22Z = (22B, 22B)',
    'XXX = (XXX, XXX)',
]
with open('8.dat') as f:
    data = [row.strip() for row in f.readlines()]
moves = {}
for row in data[2:]:
    m = re.match(r'(\w+) = \((\w+), (\w+)\)', row)
    moves[m[1]] = (m[2], m[3])


def work(where, instructions):
    steps = 0
    while not where.endswith('Z'):
        steps += 1
        i = next(instructions)
        where = get_next(where, i)
    return steps


def get_next(where, direction):
    if direction == 'L':
        where = moves[where][0]
    else:
        where = moves[where][1]
    return where


def p1():
    start = 'AAA'
    steps = work(start, itertools.cycle(data[0]))
    print('part 1:', steps)


@helpers.timer
def p2():
    locations = [k for k in moves if k.endswith('A')]
    instructions = itertools.cycle(data[0])
    steps = 0
    ends = []
    while not all(loc.endswith('Z') for loc in locations):
        inst = next(instructions)
        to_remove = []
        steps += 1
        for i, loc in enumerate(locations):
            n = get_next(loc, inst)
            locations[i] = n
            if n.endswith('Z'):
                to_remove.append(n)
                ends.append(steps)
        for r in to_remove:
            locations.remove(r)
    print('part 2:', math.lcm(*ends))


p1()
p2()
