import collections
import itertools

data = [  # part 1 test
    '1abc2',
    'pqr3stu8vwx',
    'a1b2c3d4e5f',
    'treb7uchet',
]
data = [  # part 2 test
    'two1nine',
    'eightwothree',
    'abcone2threexyz',
    'xtwone3four',
    '4nineeightseven2',
    'zoneight234',
    '7pqrstsixteen',
]
with open('1.dat') as f:
    data = [line.strip() for line in f.readlines()]

numbers = {
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9',
}
reversed_numbers = {''.join(reversed(n)): a for n, a in numbers.items()}

def sliding_window(iterable, n):
    # sliding_window('ABCDEFG', 4) --> ABCD BCDE CDEF DEFG
    it = iter(iterable)
    window = collections.deque(itertools.islice(it, n - 1), maxlen=n)
    for x in it:
        window.append(x)
        yield ''.join(window)


def check(input, reverse=False, part_2=False):
    for chars in sliding_window(input, 5):
        if chars[0].isnumeric():
            return chars[0]
        if part_2:
            nums = numbers
            if reverse:
                nums = reversed_numbers
            for number in nums:
                if chars.startswith(number):
                    return nums[number]


# part 1
s = []
for line in data:
    row = [check(line + '    '), check(''.join(reversed('    ' + line)), reverse=True)]
    s.append(''.join(row))
print(sum(int(a) for a in s))

# part 2
s = []
for line in data:
    row = [check(line + '    ', part_2=True), check(''.join(reversed('    ' + line)), reverse=True, part_2=True)]
    s.append(''.join(row))
print(sum(int(a) for a in s))
