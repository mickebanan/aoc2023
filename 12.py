import functools
import itertools
import regex as re

import helpers

data = [
    # '???.### 1,1,3',
    # '.??..??...?##. 1,1,3',
    # '?#?#?#?#?#?#?#? 1,3,1,6',
    # '????.#...#... 4,1,1',
    # '????.######..#####. 1,6,5',
    # '?###???????? 3,2,1',',
    # '???#.????#?? 1,1,1,1',
]
with open('12.dat') as f:
    data = [row.strip() for row in f.readlines()]


def parse(s, pos, ret, checksum):
    # print('parsing (%s; %d; %s; %s)' % (s, pos, ret, checksum))
    if not checksum and '#' not in s:
        # print('returning', ret + s[pos:])
        # yield ret + s[pos:]
        yield 1
    elif '#' not in s[:pos] and checksum:
        ck = checksum[0]
        # if (sum(checksum) + len(checksum) - 1) > len(s[pos:]):
        #     # print(' derp')
        #     yield 0
        # else:
        for m in re.finditer(r'(?<!#)[#?]{%s}(?!#)' % ck, s[pos:], overlapped=True):
            start, stop = m.span()
            current = pos + stop
            _ret = ret + '.' * start + '#' * ck
            if current + 1 <= len(s):
                _ret += '.'
            _s = s[:pos + start] + s[pos + start:current].replace('#', 'x') + s[current:]
            yield from parse(_s, pos + stop + 1, _ret, tuple(checksum)[1:])
    else:
        yield 0

s = 0
import time
for j, row in enumerate(data):
    t = time.time()
    value, checksum = row.split()
    _value = ''
    _checksum = ''
    # part 2
    for i in range(5):
        _value += value
        _checksum += checksum
        if i < 4:
            _value += '?'
            _checksum += ','
    value = _value
    checksum = _checksum
    checksum = [int(a) for a in checksum.split(',')]
    ss = 0
    for a in parse(value, 0, '', tuple(checksum)):
        # print('derp:', i, a)
        # res.add(a)
        # print(a)
        ss += a
    s += ss
    print(j, ss)
    # print(s)
    # print('>>', row)
    # print('total:', len(res))
    # for r in sorted(res):
    #     print(r)
    # print(time.time() - t)
print(s)

