import collections

import helpers

data = [
    '32T3K 765',
    'T55J5 684',
    'KK677 28',
    'KTJJT 220',
    'QQQJA 483',
]
with open('7.dat') as f:
    data = [row.strip() for row in f.readlines()]


class Hand:
    bid = None
    hand = None
    type = None
    card_ranks = ('2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A')

    def __init__(self, hand, bid):
        self.hand = hand
        self.bid = int(bid)
        counts = collections.defaultdict(int)
        for card in hand:
            counts[card] += 1
        if next((card for card, count in counts.items() if count == 5), None):
            self.type = 'five-of-a-kind'
        elif next((card for card, count in counts.items() if count == 4), None):
            self.type = 'four-of-a-kind'
        elif c1 := next((card for card, count in sorted(counts.items(), key=lambda k: self.card_ranks.index(k[0]))
                         if count == 3), None):
            if next((card for card, count in counts.items() if card != c1 and count == 2), None):
                self.type = 'full-house'
            else:
                self.type = 'three-of-a-kind'
        elif c1 := next((card for card, count in sorted(counts.items(), key=lambda k: self.card_ranks.index(k[0]))
                         if count == 2), None):
            if next((card for card, count in counts.items() if card != c1 and count == 2), None):
                self.type = 'two-pairs'
            else:
                self.type = 'pair'
        else:
            self.type = 'no-type'

    def __lt__(self, other):
        order = ('no-type', 'pair', 'two-pairs', 'three-of-a-kind', 'full-house', 'four-of-a-kind', 'five-of-a-kind')
        t1 = self.type
        t2 = other.type
        if t1 == t2:
            for c1, c2 in zip(self.hand, other.hand):
                if c1 == c2:
                    continue
                return self.card_ranks.index(c1) < self.card_ranks.index(c2)
        else:
            return order.index(t1) < order.index(t2)

    def __str__(self):
        return '%s (%s)' % (self.hand, self.bid)


@helpers.timer
def p1():
    # 250602641
    hands = []
    for row in data:
        hand, bid = row.split()
        h = Hand(hand, bid)
        hands.append(h)
    hands.sort()
    s = 0
    for i, h in enumerate(hands, start=1):
        print(h.hand, h.bid)
        s += i * h.bid
    print('score:', s)


p1()
