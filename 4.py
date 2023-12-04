import re

data = [
    'Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53',
    'Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19',
    'Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1',
    'Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83',
    'Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36',
    'Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11',
]
with open('4.dat') as f:
    data = [line.strip() for line in f.readlines()]

# part 1
s = 0
for row in data:
    m = re.match(r'Card\s+(\d+): ([\d ]+) \| ([\d ]+)', row)
    card, winning, hand = m.groups()
    winning = {w for w in winning.split()}
    hand = {h for h in hand.split()}
    points = 0
    if matches := len(hand & winning):
        points = 1
        for i in range(1, matches):
            points *= 2
    s += points
print('part 1:', s)

# part 2
copies = {c: 0 for c in range(1, len(data) + 1)}
for row in data:
    m = re.match(r'Card\s+(\d+): ([\d ]+) \| ([\d ]+)', row)
    card, winning, hand = m.groups()
    card = int(card)
    winning = {w for w in winning.split()}
    hand = {h for h in hand.split()}
    matches = len(hand & winning)
    copies[card] += 1
    c = copies[card]
    for next_card in range(card + 1, card + matches + 1):
        if next_card not in copies:
            break
        copies[next_card] += c
print('part 2:', sum(copies.values()))
