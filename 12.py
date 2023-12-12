import itertools
import re

data = [
    # '???.### 1,1,3',
    # '.??..??...?##. 1,1,3',
    # '?#?#?#?#?#?#?#? 1,3,1,6',
    # '????.#...#... 4,1,1',
    # '????.######..#####. 1,6,5',
    # '?###???????? 3,2,1',
]
with open('12.dat') as f:
    data = [row.strip() for row in f.readlines()]


def parse2(s, pos, ret, checksum):
    # print('parsing (%s; %s; %s)' % (s, ret, checksum))
    if not checksum and '#' not in s:
        # print('returning', ret + s[pos:])
        yield ret + s[pos:]
    for ck in checksum[:1]:
        # print('CHECKING', ck, checksum)
        for i, c in enumerate(s[pos:]):
            if c == '.':
                continue
            a = s[pos + i:pos + i + ck]
            # try:
            #     following = s[pos + i + ck]
            # except IndexError:
            #     following = ''
            # if pos + i > 0:
            #     preceding = s[pos + i - 1]
            # else:
            #     preceding = ''
            if len(a) < ck:
                break
            # print(' current a:', a, len(a))
            if re.match(r'(?<!#)[#?]{%s}(?!#)' % ck, a):
                current = pos + i + ck
                _ret = ret + '.' * i + '#' * ck
                if current + 1 <= len(s):
                    _ret += '.'
                _s = s[:pos + i] + s[pos + i:current].replace('#', 'x') + s[current:]
                yield from parse2(_s, pos + i + ck + 1, _ret, checksum[1:])

            # funkar men duger inte för p2
            # for p in itertools.product('?#', repeat=ck):
            #     p = ''.join(p)
            #     print(' i: %s, p: %s, following: %s, preceding: %s' % (i, p, following, preceding))
            #     if (p == a
            #             and (not following or following != '#')
            #             and (not preceding or preceding != '#')):
            #         print(' MATCH!')
            #         current = pos + i + ck
            #         _ret = ret + '.' * i + '#' * ck
            #         if current + 1 <= len(s):
            #             _ret += '.'
            #         _s = s[:pos + i] + s[pos + i:current].replace('#', 'x') + s[current:]
            #         yield from parse2(_s, pos + i + ck + 1, _ret, checksum[1:])


s = 0
for j, row in enumerate(data):
    value, checksum = row.split()
    _value = ''
    _checksum = ''
    # part 2
    # for i in range(5):
    #     _value += value
    #     _checksum += checksum
    #     if i < 4:
    #         _value += '?'
    #         _checksum += ','
    # value = _value
    # checksum = _checksum
    # print(value, checksum)
    checksum = [int(a) for a in checksum.split(',')]
    res = set()
    for i, a in enumerate(parse2(value, 0, '', checksum)):
        # print('derp:', i, a)
        res.add(a)
    s += len(res)
    print(j, len(res))
    # print('>>', row)
    # print('total:', len(res))
    # for r in sorted(res):
    #     print(r)
print(s)

# 12114 too high
# 9759 too high
# 9284 too high

